import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
import torch
# from utilities.io import read_methods_realistic_data, read_realistic_test_methods

from utilities.metrics import get_classification_metrics

def plot_signature(signature, labels):
    plt.bar(range(96), signature, tick_label=labels)
    plt.xticks(rotation=90)
    plt.show()


def plot_confusion_matrix(label_list, predicted_list, class_names):
    conf_mat = confusion_matrix(label_list.numpy(), predicted_list.numpy())
    plt.figure(figsize=(15, 10))

    df_cm = pd.DataFrame(conf_mat, index=class_names,
                         columns=class_names).astype(int)
    heatmap = sns.heatmap(df_cm, annot=True, fmt="d")

    heatmap.yaxis.set_ticklabels(
        heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=15)
    heatmap.xaxis.set_ticklabels(
        heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=15)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    return conf_mat

def plot_weights(guessed_labels, pred_upper, pred_lower, sigs_names):
    num_classes = len(guessed_labels)
    fig, ax = plt.subplots()
    guessed_error_neg = guessed_labels - pred_lower
    guessed_error_pos = pred_upper - guessed_labels
    ax.bar(range(num_classes),guessed_labels, yerr=[abs(guessed_error_neg), abs(guessed_error_pos)], align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Weights')
    ax.set_xticks(range(num_classes))
    ax.set_xticklabels(sigs_names, rotation='vertical')
    ax.set_title('Signature decomposition')
    plt.tight_layout()
    plt.show()

def plot_weights_comparison(true_labels, guessed_labels, pred_upper, pred_lower, sigs_names):
    num_classes = len(guessed_labels)
    fig, ax = plt.subplots()
    guessed_error_neg = guessed_labels - pred_lower
    guessed_error_pos = pred_upper - guessed_labels
    ax.bar(range(num_classes),guessed_labels, yerr=[abs(guessed_error_neg), abs(guessed_error_pos)], align='center', width=0.2, alpha=0.5, ecolor='black', capsize=10)
    ax.bar(np.array(range(num_classes))+0.2, true_labels, width=0.2, align='center')
    ax.set_ylabel('Weights')
    ax.set_xticks(range(num_classes))
    ax.set_xticklabels(sigs_names, rotation='vertical')
    ax.set_title('Signature decomposition')
    plt.tight_layout()
    plt.show() 

# def plot_weights_comparison(true_labels, guessed_labels, guessed_error_pos, guessed_error_neg, sigs_names):
#     num_classes = len(guessed_labels)
#     fig, ax = plt.subplots()
#     ax.bar(range(num_classes),guessed_labels, yerr=[abs(guessed_error_neg), abs(guessed_error_pos)], align='center', width=0.2, alpha=0.5, ecolor='black', capsize=10)
#     ax.bar(np.array(range(num_classes))+0.2, true_labels, width=0.2, align='center')
#     ax.set_ylabel('Weights')
#     ax.set_xticks(range(num_classes))
#     ax.set_xticklabels(sigs_names, rotation='vertical')
#     ax.set_title('Signature decomposition')
#     plt.tight_layout()
#     plt.show()

def plot_weights_comparison_deconstructSigs(true_labels, deconstructSigs_labels, guessed_labels, pred_upper, pred_lower, sigs_names):
    num_classes = len(guessed_labels)
    fig, ax = plt.subplots()
    guessed_error_neg = guessed_labels - pred_lower
    guessed_error_pos = pred_upper - guessed_labels
    ax.bar(range(num_classes),guessed_labels, yerr=[abs(guessed_error_neg), abs(guessed_error_pos)], align='center', width=0.2, alpha=0.5, ecolor='black', capsize=10)
    ax.bar(np.array(range(num_classes))+0.2, true_labels, width=0.2, align='center')
    ax.bar(np.array(range(num_classes))-0.2,deconstructSigs_labels, width=0.2, align='center')
    ax.axhline(0.05, 0, num_classes, linestyle='--', c='red')
    ax.set_ylabel('Weights')
    ax.set_xticks(range(num_classes))
    ax.set_xticklabels(sigs_names, rotation='vertical')
    ax.set_title('Signature decomposition')
    plt.tight_layout()
    plt.show()
     
def plot_interval_performance(label_batch, pred_upper, pred_lower, sigs_names):
    lower = label_batch - pred_lower
    upper = pred_upper - label_batch
    num_error = torch.sum(lower<0, dim=0)
    num_error += torch.sum(upper<0, dim=0)
    num_error = num_error / label_batch.shape[0]
    num_classes = 72
    plt.bar(range(num_classes), 100*num_error, align='center', width=0.2, alpha=0.5, ecolor='black', capsize=10)
    plt.ylabel("Percentage of error (%)")
    plt.xticks(range(num_classes), sigs_names, rotation='vertical')
    plt.title('Confidence intervals performance')
    plt.show()

def plot_metric_vs_mutations(list_of_metrics, list_of_methods, list_of_guesses, label, plot_name):
    m = -1
    fig, axs = plt.subplots(len(list_of_metrics))
    fig.suptitle("Metrics vs Number of Mutations")
    
    for metric in list_of_metrics:
        m += 1
        num_muts = np.unique(label[:,-1].detach().numpy())
        values = np.zeros((len(list_of_methods), len(num_muts)))

        for k in range(len(list_of_methods)):
            for i in range(len(num_muts)):
                metrics = get_classification_metrics(label_batch=label[1000*i:1000*(i+1), :-1], prediction_batch=list_of_guesses[k][1000*i:1000*(i+1),:])
                values[k,i] = metrics[metric]
        
        handles = axs[m].plot(np.log10(num_muts), np.transpose(values))
        axs[m].set_ylabel(metric)
        if m == len(list_of_metrics)-1:
            axs[m].set_xlabel("log(N)")

        # Shrink current axis by 3%
        box = axs[m].get_position()
        axs[m].set_position([box.x0, box.y0, box.width * 0.97, box.height])
    fig.legend(handles = handles, labels=list_of_methods, bbox_to_anchor=(1, 0.5))
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()
    fig.savefig('../plots/exp_0/%s.png'%plot_name)


if __name__ == "__main__":
    deconstructSigs_labels = [0.1, 0.7, 0.2]
    real_labels = [0.2, 0.5, 0.3]
    guessed_labels = [0.25, 0.6, 0.2]
    guessed_error = [0.01, 0.04, 0.001]
    sigs_names = ["SBS1", "SBS2", "SBS3"]

    plot_weights_comparison_deconstructSigs(real_labels, deconstructSigs_labels, guessed_labels, guessed_error, sigs_names)