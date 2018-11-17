# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 10.5
print(type(a))
print(a)

b=False
print(b)

list1=[10,'@',10.5,'testabcd']
print(list1)
print(type(list1))

print(list1[0])
print(list1[0:4])
list1.append('asdasd')
list1[2]=2000

list1.extend((10,20))
list2=[30]
list1.extend(list2)
print(list1)

print(list1[1])
print(list1[1:3])
print(list1[3:3])

# =============================================================================
# 
# //tuple reffers to [] and list mean () dictinary mean {} key value pair
# tuple mean read only 
#where as list can be edittable
#list and tuple are heterogenoud data types
# =============================================================================
tuple1 = (1,2,3,4)
print(type(tuple1))

tuple2 = (1,2,'test')
print(type(tuple2))

len(tuple2)


#access elements by key 
test = {'length':10,'breadth':20}
print(type(test))
print(test['breadth'])

#alternate way to access elements by key
print(test.get('length'))

#acess both key value pair
print(test.items())

#access keys
print(test.keys())

#data freames is used for list of list or for rows and columns


import pandas as pd
pd.__version__

pd.show_versions()

import pandas as pd
print(pd.__version__)

titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
print(type(titanic_train))
titanic_train.info()
titanic_train.describe()
titanic_train.shape
titanic_train['sex']
titanic_train['Fare']
titanic_train.Sex
titanic_train.Fare
titanic_train.groupby('Pclass').size() # no extra brackets are required for single values
titanic_train.groupby(('Pclass','Sex')).size()

col1 = [10,20,30,40]
col2 =['abc','def','asdf','dgsfg']




list3=[1,2,3,]
print(list3)
list4=(10.20,30.50)
a=list3.append(list4)
print (a)



import os
os.getcwd()
os.chdir('C:\\Users\\Santosh\\Downloads')
os.getcwd()
temp_var=open("train.csv")
temp_var.shape()



import pandas as pd
col1 = [10,20,30,40]
col2 = ['abc','def','xyz','pqr']
col3 = [0,1,0,1]
df1 = pd.DataFrame({'pid':col1,'pname':col2,'survived':col3})
df1.iloc[0:2,1] # i loc and loca diff
df1.loc[0:2,['pname']] #i location and location diff


print(df1.pid >20 )
df1[df1.pid > 30]
df1.pid


import pandas as pd
print(pd.__version__)
titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
t = titanic_train
print(type(titanic_train))
titanic_train.info()
titanic_train.describe()
titanic_train.shape
h=titanic_train.head()
h
titanic_train.groupby(['Embarked', 'Pclass']).mean()['Fare']
titanic_train.groupby(['Pclass']).count()
titanic_train.head()
h['Fare']
h.Fare



dict1={a:10,b:20}
dict2={'asdf':';lkj','10':'10'}
type(dict1)
print(dict1[a])
print(dict1.get(a))
print(dict2.keys())
print(dict2.items())
print(dict1.keys())
print(dict1.items())

from sklearn import tree # for decision tree
#import io

t.shape
x_t1 = t[['Pclass','SibSp','Parch']]
y_t1 = t['Survived']
dt = tree.DecisionTreeClassifier()
dt.fit(x_t1,y_t1)


#t_test = pd.read_csv("C:\\Users\\Santosh\\Downloads\\titanic_test.csv")
#X_test = t_test[['Pclass', 'SibSp', 'Parch']]
#Use .predict method on Test data using the model which we built

#t_test['Survived'] = dt.predict(X_test)  
#os.getcwd() #To get current working directory
#t_test.to_csv("submission_Index_True.csv", columns=['PassengerId','Survived'] , index = True)

import os
import io
import pydot
objStringIO = io.StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")






