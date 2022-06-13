import numpy as np
import matplotlib.pyplot as mtp  
import pandas as pd  
  
#importing datasets  
data_set= pd.read_csv('code-to-give.csv')  
#print(data_set.head())
  
#Extracting Independent and dependent Variable  
x= data_set.iloc[:, [5,6,7,11]].values  
y= data_set.iloc[:, 3].values  
  
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.01, random_state=100)  

#feature Scaling  
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)    

#Fitting Decision Tree classifier to the training set  
from sklearn.tree import DecisionTreeClassifier  
classifier= DecisionTreeClassifier(criterion='entropy', random_state=100)  
classifier.fit(x_train, y_train)  

#GET INPUT 
#***********************************************************************************************************
competitors = int(input("Do you have competitors (0 or 1): "))
space = int(input("Do you have space for your work (0 or 1) : "))
resource = int(input("Do you have resources available (0 or 1) : "))
skill = input("Enter your skill - tailoring (or) animal husbandry (or) farming : ")
#***********************************************************************************************************

skill = skill.strip().lower()
if(skill == 'tailoring'):
    skills_id = 1
elif(skill == 'animal husbandry'):
    skills_id = 2
elif(skill == 'farming'):
    skills_id = 3
else:
    skills_id = 4

classes = classifier.classes_
attributes = []
attributes.append([competitors, space, resource, skills_id])
user_attributes = st_x.transform(attributes)    
prediction = classifier.predict_proba(user_attributes)
threshold = 0.1 # change this accordingly
y_pred = []
for index, pred in enumerate(prediction[0]):
        if pred > threshold:
            y_pred.append(classes[index])

print("y_pred : ",y_pred)  
