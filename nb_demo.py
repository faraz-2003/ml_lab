import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

class nb() :
    def __init__(self) :
        self.prior = {}
        self.conditional = {}

    def fit(self, X, y) :
        self.classes = np.unique(y)
        for c in self.classes :
            self.prior[c] = np.mean(y == c)

        for feature in X.columns:
            self.conditional[feature] = {}
            for c in self.classes:
                feature_value = X[feature][c==y]
                self.conditional[feature][c] = { 'mean' : np.mean(feature_value), 'std' : np.std(feature_value) }

    def predict(self, X) :
        y_pred = []
        for _,sample in X.iterrows() :
            probabilities = {}
            for c in self.classes:
                probabilities[c] = self.prior[c]
                for feature in X.columns :
                    m = self.conditional[feature][c]['mean']
                    std = self.conditional[feature][c]['std']
                    x  = sample[feature]
                    probabilities[c] *= self.gaussian(m,std,x)
            y_pred.append(max(probabilities,key=probabilities.get))
        return y_pred
    
    def gaussian(self,mean,std,x):
        e = np.exp(-((x-mean)**2)/(2 * (std**2)))
        return (1/(np.sqrt(2*np.pi))*std)* e
    
df = pd.read_csv('Titanic-Dataset.csv')
df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
df['Age'].fillna(df['Age'].median(),inplace=True)
df['Fare'].fillna(df['Fare'].median(),inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0],inplace=True)
df['Embarked'] =df['Embarked'].map({'C':0,'Q':1,'S':2})

train,test = train_test_split(df,test_size=0.3)
y_train = train['Survived']
x_train = train.drop('Survived',axis=1)
y_test = test['Survived']
x_test = test.drop('Survived',axis=1)

bn = nb()
bn.fit(x_train,y_train)
y_pred = bn.predict(x_test)    
cm = confusion_matrix(y_pred,y_test)
print("The confusion matrix is : \n",cm)
accuracy = np.mean(y_test == y_pred)
print("The accuracy is : ",accuracy)

