import pandas as pd
import torch

def read_data(device, data_folder="../data"):
    train_input = torch.tensor(pd.read_csv(
        data_folder + "/train_input_w01.csv", header=None).values, dtype=torch.float)
    train_input = train_input.to(device)
    train_guess_0 = torch.tensor(pd.read_csv(
        data_folder + "/train_w01_baseline_JS.csv", header=None).values, dtype=torch.float)
    train_guess_0 = train_guess_0.to(device)
    train_label = torch.tensor(pd.read_csv(
        data_folder + "/train_label_w01.csv", header=None).values, dtype=torch.float)
    train_label = train_label.to(device)

    val_input = torch.tensor(pd.read_csv(
        data_folder + "/validation_input_w01.csv", header=None).values, dtype=torch.float)
    val_input = val_input.to(device)
    val_guess_0 = torch.tensor(pd.read_csv(
        data_folder + "/validation_w01_baseline_JS.csv", header=None).values, dtype=torch.float)
    val_guess_0 = val_guess_0.to(device)
    val_label = torch.tensor(pd.read_csv(
        data_folder + "/validation_label_w01.csv", header=None).values, dtype=torch.float)
    val_label = val_label.to(device)
    return train_input, train_guess_0, train_label, val_input, val_guess_0, val_label

def read_data_yapsa(device, data_folder="../data"):
    train_input = torch.tensor(pd.read_csv(
        data_folder + "/train_input_w01.csv", header=None).values, dtype=torch.float)
    train_input = train_input.to(device)
    train_guess_0 = torch.tensor(pd.read_csv(
        data_folder + "/train_baseline_yapsa.csv", header=None).values, dtype=torch.float)
    train_guess_0 = train_guess_0.to(device)
    train_label = torch.tensor(pd.read_csv(
        data_folder + "/train_label_w01.csv", header=None).values, dtype=torch.float)
    train_label = train_label.to(device)

    val_input = torch.tensor(pd.read_csv(
        data_folder + "/validation_input_w01.csv", header=None).values, dtype=torch.float)
    val_input = val_input.to(device)
    val_guess_0 = torch.tensor(pd.read_csv(
        data_folder + "/validation_baseline_yapsa.csv", header=None).values, dtype=torch.float)
    val_guess_0 = val_guess_0.to(device)
    val_label = torch.tensor(pd.read_csv(
        data_folder + "/validation_label_w01.csv", header=None).values, dtype=torch.float)
    val_label = val_label.to(device)
    return train_input, train_guess_0, train_label, val_input, val_guess_0, val_label

def read_methods_random_data(device, data_folder="../data"):
    label = torch.tensor(pd.read_csv(
        data_folder + "/random_data/test_label_w01.csv", header=None).values, dtype=torch.float)
    label = label.to(device)
    decompTumor2Sig_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/decompTumor2Sig_random_test_guess.csv", header=None).values, dtype=torch.float)
    decompTumor2Sig_guess = decompTumor2Sig_guess.to(device)
    deconstructSigs_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/deconstructSigs_random_test_guess.csv", header=None).values, dtype=torch.float)
    deconstructSigs_guess = deconstructSigs_guess.to(device)
    MutationalPatterns_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/MutationalPatterns_random_test_guess.csv", header=None).values, dtype=torch.float)
    MutationalPatterns_guess = MutationalPatterns_guess.to(device)
    mutSignatures_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/mutSignatures_random_test_guess.csv", header=None).values, dtype=torch.float)
    mutSignatures_guess = mutSignatures_guess.to(device)
    SignatureEstimationQP_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/SignatureEstimationQP_random_test_guess.csv", header=None).values, dtype=torch.float)
    SignatureEstimationQP_guess = SignatureEstimationQP_guess.to(device)
    YAPSA_guess = torch.tensor(pd.read_csv(
        data_folder + "/random_data/methods/YAPSA_random_test_guess.csv", header=None).values, dtype=torch.float)
    YAPSA_guess = YAPSA_guess.to(device)
    return label, decompTumor2Sig_guess, deconstructSigs_guess, MutationalPatterns_guess, mutSignatures_guess, SignatureEstimationQP_guess, YAPSA_guess

def read_methods_realistic_data(device, data_folder="../data"):
    label = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/realistic_test_label.csv", header=None).values, dtype=torch.float)
    label = label.to(device)
    decompTumor2Sig_guess = torch.tensor(pd.read_csv(   
        data_folder + "/realistic_data/methods/decompTumor2Sig_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    decompTumor2Sig_guess = decompTumor2Sig_guess.to(device)
    deconstructSigs_guess = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/methods/deconstructSigs_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    deconstructSigs_guess = deconstructSigs_guess.to(device)
    MutationalPatterns_guess = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/methods/MutationalPatterns_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    MutationalPatterns_guess = MutationalPatterns_guess.to(device)
    mutSignatures_guess = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/methods/mutSignatures_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    mutSignatures_guess = mutSignatures_guess.to(device)
    SignatureEstimationQP_guess = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/methods/SignatureEstimationQP_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    SignatureEstimationQP_guess = SignatureEstimationQP_guess.to(device)
    YAPSA_guess = torch.tensor(pd.read_csv(
        data_folder + "/realistic_data/methods/YAPSA_realistic_test_guess.csv", header=None).values, dtype=torch.float)
    YAPSA_guess = YAPSA_guess.to(device)
    return label, decompTumor2Sig_guess, deconstructSigs_guess, MutationalPatterns_guess, mutSignatures_guess, SignatureEstimationQP_guess, YAPSA_guess