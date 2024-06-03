import numpy as np
from scipy.cluster.hierarchy import linkage,dendrogram
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris().data[:6]

def proximity_matrix(data):
    n = data.shape[0]
    proximity_matrix = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            proximity_matrix[i,j] = np.linalg.norm(data[i]-data[j])
            proximity_matrix[j,i] = proximity_matrix[i,j]

    return proximity_matrix

def display(proximity_matrix,linkage_type):
    Z = linkage(proximity_matrix,method=linkage_type)
    dendrogram(Z)
    plt.title(f"The {linkage_type} linkage")
    plt.xlabel("Data points")
    plt.ylabel("Distance")
    plt.show()

print("The proximity matrix",proximity_matrix(data))

display(data,linkage_type="single")
display(data,linkage_type="complete")