#Definition
#Wheither bank will give you creditcard or not?
# k=6 features
#1. Income(>90 or not?)
#2. Stable Work State(yes or not)
#3. Famous Company(yes or not)
#4. Age(>30 or not)
#5. Credit State(yes or not)
#6. Real estate(yes or not)
#A more clearly picture will be shown in README.md.
import random
import numpy as np
#Generate data
data=[]
for i in range(50000):
    x=[]
    x.append(random.randint(30,150))
    x.append(random.randint(0,10))
    x.append(random.randint(0,1))
    x.append(random.randint(0,1))
    x.append(random.randint(20,40))
    x.append(random.randint(0,1))
    data.append(x)
lable=[]
for d in data:
    if d[0]>=90:
        if d[2]==1:
            lable.append(1)
        else:
            if d[5]==1:
                lable.append(1)
            else:
                lable.append(-1)
    else:
        if d[1]>=5:
            if d[4]>=30:
                lable.append(1)
            else:
                lable.append(-1)
        else:
            if d[3]==1:
                lable.append(1)
            else:
                lable.append(-1)
data_train=data[0:40000]
data_test=data[40001:]
lable_train=lable[0:40000]
lable_test=lable[40001:]
data_train=np.asarray(data_train)
data_test=np.asarray(data_test)
lable_train=np.asarray(lable_train)
lable_test=np.asarray(lable_test)
np.save("data_train",data_train)
np.save("data_test",data_test)
np.save("lable_train",lable_train)
np.save("lable_test",lable_test)