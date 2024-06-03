import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split

def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

def manhattan_distance(x1,x2):
    return np.sum(np.abs(x1-x2))
class knn():
    def __init__(self,k,dist_func):
        self.k = k
        self.dist_func = dist_func

    def fit(self,X,y):
        self.x_train = X
        self.y_train = y

    def predict(self,X):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self,x):
        distances = [euclidean_distance(x,x_train) for x_train in self.x_train]
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        most_comm = Counter(k_labels).most_common()
        return most_comm[0][0]
    
dp = pd.read_csv('glass.csv')    
y = dp['Type'].values
x = dp.drop('Type',axis=1).values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

kn = knn(3,dist_func=euclidean_distance)
kn.fit(x_train,y_train)
predictions = kn.predict(x_test)
euc_val = np.sum(predictions==y_test)/len(y_test)
print("The accuracy by euclidiean distance is ",euc_val)

knm = knn(3,dist_func=manhattan_distance)
knm.fit(x_train,y_train)
predictions = knm.predict(x_test)
man_val = np.sum(predictions==y_test)/len(y_test)
print("The accuracy by manhattan distance is ",man_val)