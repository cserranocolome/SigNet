
from concurrent.futures import ProcessPoolExecutor
import os
import sys

import numpy as np
import pandas as pd
import scipy
from scipy.optimize import minimize
import torch
from tqdm import tqdm
from scipy.optimize import nnls


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utilities.metrics import *


class YapsaInspiredBaseline:

    def __init__(self, signatures):
        self.signatures = torch.stack(signatures).t().cpu().detach().numpy()
        self.__weight_len = self.signatures.shape[1]

    def get_weights(self, normalized_mutations):
        h, rnorm = nnls(self.signatures, normalized_mutations, maxiter=5*self.__weight_len)
        return torch.from_numpy(h).float()

    def get_weights_batch(self, input_batch, n_workers=8):
        result = []
        input_as_list = input_batch.tolist()
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            for r in executor.map(self.get_weights, input_as_list):
                result.append(r)
        guessed_labels = torch.stack(result)
        return guessed_labels


if __name__ == "__main__":
    num_classes = 72
    training_data = torch.tensor(pd.read_csv(
        "../../data/train_input_w01.csv", header=None).values, dtype=torch.float)
    validation_data = torch.tensor(pd.read_csv(
        "../../data/validation_input_w01.csv", header=None).values, dtype=torch.float)
    test_data = torch.tensor(pd.read_csv(
        "../../data/test_input_w01.csv", header=None).values, dtype=torch.float)
    
    signatures_data = pd.read_excel("../../data/data.xlsx")
    signatures = [torch.tensor(signatures_data.iloc[:, i]).type(torch.float32)
                  for i in range(2, 74)][:num_classes]

    sf = YapsaInspiredBaseline(signatures)


    # h = torch.from_numpy(sf.get_weights(validation_data[:10, ...])).float()
    # import time
    # t = time.time()
    # h = sf.get_weights_batch(validation_data[:50, ...])
    # elapsed = time.time() - t
    # print("elapsed", elapsed)

    # validation_labels = torch.tensor(pd.read_csv(
    #     "../../data/validation_label_w01.csv", header=None).values, dtype=torch.float)[:, :-1]

    # print("mse:", get_MSE(h, validation_labels))
    # print("js:", get_jensen_shannon(h, validation_labels))

    print("Computing...")
    x = np.linspace(0, training_data.shape[0], num=10, dtype=int)
    sol = torch.empty((1,72))
    for i in range(len(x)-1):
        sol_i = sf.get_weights_batch(training_data[x[i]:x[i+1],:])
        sol = torch.cat((sol, sol_i), 0)
    sol = sol[1:, :]
    sol = sol.detach().numpy()
    df = pd.DataFrame(sol)
    df.to_csv("../../data/training_baseline_yapsa.csv", header=False, index=False)
    print("Training done!")
    # sol = sf.get_weights_batch(validation_data)
    # sol = sol.detach().numpy()
    # df = pd.DataFrame(sol)
    # df.to_csv("../../data/validation_baseline_yapsa.csv", header=False, index=False)
    # print("Validation done!")
    # sol = sf.get_weights_batch(test_data)
    # sol = sol.detach().numpy()
    # df = pd.DataFrame(sol)
    # df.to_csv("../../data/test_baseline_yapsa.csv", header=False, index=False)
    # print("Test done!")
