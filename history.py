df1 = pd.DataFrame({'pid':col1,'pname':col2,'survived':col3})
df1.iloc[0:2,1]

df1.iloc[0:2,['pname']]
df1.iloc[0:2,['pname']]
print(type(df1.pid >20 ))
print(type(df1.pid >20 ))
df1[df1.pid ]
print(type(df1.pid >20 ))
df1[df1.pid > 20 ]
print(type(df1.pid >20 ))
df1[df1.pid  ]
print(df1.pid)
print(type(df1.pid >20 ))
print((df1.pid >20 ))
print(df1.pid >20 )
df1[df1.pid > 30]
df1.pid
df1[df1.pid > 30]
df1.pid
import pandas as pd
print(pd.__version__)
titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
print(type(titanic_train))
titanic_train.info()
titanic_train.describe()
titanic_train.shape
titanic_train.groupby(['Pclass'])
df1[df1.pid > 30]
df1.pid
dict1={a:10,b:20}
type(dict1)
print(dict1[a])
print(dict1.get(a))
print(dict1.keys())
print(dict1.items())
print(dict2.keys())
print(dict2.items())
dict2={'asdf':';lkj','10':'10'}
print(dict2.keys())
print(dict2.keys())
print(dict2.items())
print(dict2.keys())
print(dict2.items())
print(dict1.keys())
print(dict1.items())
titanic_train.groupby(['Pclass'])
titanic_train.groupby(['Pclass']).count()
titanic_train.head()
titanic_train._get_value()
titanic_train._get_value(0,1
titanic_train._get_value(0,1)
titanic_train._get_value(4,5)
titanic_train.groupby(['Embarked', 'Pclass']).mean()['Fare']
Embarked
titanic_train
titanic_train.head(
titanic_train.head()
h=titanic_train.head()
h
h['Fare']
h.Fare
from sklearn import tree
titanic_train.info()
titanic_train.describe()
titanic_train.shape
titanic_train.describe()
titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
titanic_train = t
t = titanic_train
from sklearn import tree
t.shape
x.t1 = t['Pclass','SibSp','Parch']
x.t1 = t[['Pclass','SibSp','Parch']]
x_t1 = t[['Pclass','SibSp','Parch']]
y_t1 = t['Survived']
dt = tree.DecisionTreeClassifier()
dt.fit(x_t1 , y_t1)
dt.fit(x_t1,y_t1)
from sklearn import tree # for decision tree
t.shape
x_t1 = t[['Pclass','SibSp','Parch']]
y_t1 = t['Survived']
dt = tree.DecisionTreeClassifier()
dt.fit(x_t1,y_t1)


t_test = pd.read_csv("C:\\Users\\Santosh\\Downloads\\titanic_test.csv")
X_test = t_test[['Pclass', 'SibSp', 'Parch']]
#Use .predict method on Test data using the model which we built

t_test['Survived'] = dt.predict(X_test)  
os.getcwd() #To get current working directory
t_test.to_csv("submission_Titanic.csv", columns=['PassengerId','Survived'], index=False)
os.getcwd()
t_test.to_csv("submission_Titanic.csv", columns=['PassengerId','Survived'])
t_test.to_csv("submission_Index_False.csv", columns=['PassengerId','Survived'] , index = False)
t_test.to_csv("submission_Index_True.csv", columns=['PassengerId','Survived'] , index = True)
import io
import os,io,pydot
t.shape

## ---(Sat Nov 17 06:47:13 2018)---
tree.export_graphviz(dt, out_file = objStringIO, feature_names = X_t1.columns)
titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
import pandas as pd
print(pd.__version__)
titanic_train = pd.read_csv("C:\\Users\\Santosh\\Downloads\\train.csv")
t = titanic_train
from sklearn import tree # for decision tree
import io

t.shape
x_t1 = t[['Pclass','SibSp','Parch']]
y_t1 = t['Survived']
dt = tree.DecisionTreeClassifier()
dt.fit(x_t1,y_t1)
import os,io,pydot
tree.export_graphviz(dt, out_file = objStringIO, feature_names = X_t1.columns)
import os,io,pydot
objStringIO = io.StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = X_t1.columns)
import os,io,pydot
objStringIO = io.StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
os.getcwd()
os.chdir("C:\Users\Santosh\Datascience")
os.chdir("C:\\Users\\Santosh\\Datascience")
file1.write_pdf("DecissionTree1.pdf")
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
file1[0].write_pdf("DecissionTree1.pdf")
import os,io,pydot
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
file1.write_pdf("DecissionTree1.pdf")
import os
import io
import pydot
objStringIO = StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
objStringIO = io.StringIO()
file1 = pydotplus.graph_from_dot_data(objStringIO.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
import pydotplus
file1.write_pdf("DecissionTree1.pdf")
file1[0] = pydot.graph_from_dot_data(objStringIO.getvalue())
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
import os
import io
import pydot
objStringIO = io.StringIO()
tree.export_graphviz(dt, out_file = objStringIO, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(objStringIO.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1[0].write_pdf("DecissionTree1.pdf")
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
file1.write_txt("DecissionTree1.txt")
import os
import io
import pydot
dot_data = io.StringIO()
tree.export_graphviz(dt, out_file = dot_data, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(dot_data.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
import os
import io
import pydot
data = io.StringIO()
tree.export_graphviz(dt, out_file = data, feature_names = x_t1.columns)
file1 = pydot.graph_from_dot_data(data.getvalue())
os.getcwd()
os.chdir("C:\\Users\\Santosh\\Datascience\\")
file1.write_pdf("DecissionTree1.pdf")
file1[0].write_pdf("DecissionTree1.pdf")
file1.write_pdf("DecissionTree1.pdf")