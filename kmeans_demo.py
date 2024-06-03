import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def kmeans( X, k, max_iters=100):
    centroids = X[:k]
    for _ in range(max_iters):
        expanded_x = X[:,np.newaxis]
        euclid = np.linalg.norm(expanded_x - centroids,axis=2)
        labels = np.argmin(euclid,axis=1)
        new_centroids = np.array(X[labels == k].means(aixs=0) for k in range(k))

        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids
    return labels, centroids         


X = load_iris().data
k=3
labels,centroids = kmeans(X,k)        
print("labels are :",labels)
print("centroids are :",centroids)

plt.x_label("sepal length")
plt.y_label("sepal width")
plt.scatter(X[:,0],X[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],color="red",marker='x',s=200)
plt.title("The k means clustering plot")
plt.show()