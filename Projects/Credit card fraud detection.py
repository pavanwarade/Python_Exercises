import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('Python: {}'.format(sys.version))
print('Numpy: {}'.format(numpy.__version__))
print('Pandas: {}'.format(pandas.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importing the datasets from CSV files using pandas
data=pd.read_csv('creditcard.csv')


# explore the datasets
print(data.columns)

print(data.shape)

# for each column info
print(data.describe())


# taking 10% of datasets
data=data.sample(frac=0.1,random_state=1)
print(data.shape)


# plot histogram for each parameter
data.hist(figsize = (20,20))
plt.show()


# determine no of fraud cases in datasets
Fraud= data[data['Class']==1]
Valid=data[data['Class']==0]

outlier_fraction=len(Fraud)/float(len(Valid))
print(outlier_fraction)
print('Fraud cases: {}'.format(len(Fraud)))
print('Valid cases: {}'.format(len(Valid)))


# co-relation Matrix
cormat=data.corr()
fig=plt.figure(figsize=(12,9))

sns.heatmap(cormat, vmax=.8, square=True)
plt.show()


# Get all data columns from the dataframes
columns=data.columns.tolist()


# filter the column to remove data we do not want
columns=[c for c in columns if c not in ['Class']]

# store the variable we will precdicting on
target='Class'

X=data[columns]
Y=data[target]   #-----------------1)

print(X.shape)
print(Y.shape)

# Now use the algorithms 1- Isolation Forest, 2- Localoutlier factor
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# define Random state
state=1

# define the outlier detection methods
Classifiers={"Isoation Forest":IsolationForest(max_samples=len(X), contamination=outlier_fraction, random_state=state),
             "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, contamination=outlier_fraction)
            }


# fit the model
n_outliers=len(Fraud)
for i, (clf_name, clf) in enumerate(Classifiers.items()):
    
    
    # fit the data and outliers
    if clf_name=="Local Outlier Factor":
        y_pred=clf.fit_predict(X)
        scores_pred=clf.negative_outlier_factor_
        
    else:
        clf.fit(X)
        scores_pred=clf.decision_function(X)
        y_pred=clf.predict(X)
        
    
    # reshape the prediction values to 0 for valid and 1 for Fraud.
    y_pred[y_pred==1]=0
    y_pred[y_pred==-1]=1
    
    # from 1)
    n_errors=(y_pred !=Y).sum()
    
    # run the classification matrixs
    
    print('{}:{}'.format(clf_name, n_errors))
    print(accuracy_score(Y, y_pred))
    print(classification_report(Y, y_pred))
    




