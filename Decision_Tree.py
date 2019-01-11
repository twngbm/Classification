#using sklearn's DecisionTreeClassifier
from sklearn import tree
import numpy as np
X=np.load("data_train.npy")
Y=np.load("lable_train.npy")
print("dataset=\n",X,"\nlable=\n",Y)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
X_t=np.load("data_test.npy")
Y_t=np.load("lable_test.npy")
error=0
for index,x in enumerate(X_t):
    y=clf.predict([x])
    if y[0]!=Y_t[index]:
        error+1
print("rate of error=",error/len(Y_t))
