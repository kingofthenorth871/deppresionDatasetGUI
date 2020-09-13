from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from tkinter import *

# Packages for analysis
import pandas as pd
import numpy as np

# Packages for visuals

#if __name__ == "__main__":

# Pickle package
import pickle

class deppresionDataset:

    df = pd.read_csv('scores.csv')


    def load(self):
        return self.df


df2 = pd.read_csv('scores.csv')


controlSubjects = ['condition_1','condition_2','condition_3','condition_4','condition_5','condition_5','condition_5','condition_5','condition_5','condition_6'
                ,'condition_7','condition_8','condition_9','condition_10','condition_11','condition_12','condition_13','condition_14','condition_15','condition_16'
                ,'condition_17','condition_18','condition_19','condition_20','condition_21','condition_22','condition_23']

filtered_df = df2[df2['number'].isin(controlSubjects)]

condition_control = pd.read_csv('condition_control.csv')

#hele datasettet hvor klassene deprimert / ikke deprimert er delt i 0 og 1 under 'control'

condition_new = pd.read_csv('condition_new.csv')

controlAndCondition = condition_new.append(condition_control)

controlAndCondition.to_csv("controlAndCondition.csv")

print("printer control and condition")
print(controlAndCondition)


feature_df = controlAndCondition[['average', 'median', 'averageAll']]

#independent variable
X = np.asarray(feature_df)


## error error error!!!!!!
#dependent variable
y = np.asarray(controlAndCondition['control'])

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=4)

#print(X_test['averageAll'])

classifier = svm.SVC(kernel='linear', gamma='auto', C=2, probability=True)
classifier.fit(X_train, y_train)
y_predict = classifier.predict(X_test)


y_pred = classifier.predict_proba(X_test)[:, 1]
y_pred = pd.Series(y_pred, name='averageAll')



import ethik

explainer = ethik.ClassificationExplainer()

print(y_pred)

#print(X_test['averageAll'])


#explainer.plot_influence(X_test=X_test, y_pred=y_predict).show()

#classifier.predict_proba

#evaluation
from sklearn.metrics import classification_report



#print(condition_new)

axes = condition_new.plot(kind = 'scatter', x='median', y='averageAll', color='red', label='depressed')
condition_control.plot(kind = 'scatter', x='median', y='averageAll', color='blue', label='nonDepressed', ax=axes)

print("print X-test:",X_test)
print("")
print("")
print("")

print("printer y_pred:",y_pred)
print("")
print("")
print("")

print(classification_report(y_test, y_predict))


X = controlAndCondition

import re
X = X.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

del X['date']
del X['timestamp']
y = controlAndCondition['control']

from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, shuffle=True, random_state=42)

import lightgbm as lgb

model = lgb.LGBMClassifier(random_state=42).fit(X_train, y_train)

y_pred = model.predict_proba(X_test)[:, 1]

# We use a named pandas series to make plot labels more explicit
y_pred = pd.Series(y_pred, name='>$50k')

import ethik




X = controlAndCondition

import re
X = X.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

del X['date']
del X['timestamp']
y = controlAndCondition['control']

from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, shuffle=True, random_state=42)


classifier = svm.SVC(kernel='linear', gamma='auto', C=2, probability=True).fit(X_train, y_train)


y_pred = classifier.predict_proba(X_test)[:, 1]

# We use a named pandas series to make plot labels more explicit
y_pred = pd.Series(y_pred, name='chance of being depressed')

import ethik

explainer3 = ethik.ClassificationExplainer()



def averageAll():
    return  explainer3.plot_influence(
    X_test=X_test['averageAll'],
    y_pred=y_pred
)

def median():
    return  explainer3.plot_influence(
    X_test=X_test['median'],
    y_pred=y_pred
)

def average():
    return  explainer3.plot_influence(
    X_test=X_test['average'],
    y_pred=y_pred
)