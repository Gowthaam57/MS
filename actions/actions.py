from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted
from rasa_sdk.types import DomainDict
from sqlalchemy import Float
import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient
import urllib
from csv import writer



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


password=urllib.parse.quote_plus('Lakshana@57')
client = pymongo.MongoClient("mongodb+srv://Gowthaam:%s@buzz.qjh5k.mongodb.net/?retryWrites=true&w=majority"%(password))
db = client.get_database('BuzzWomen')
records=db.Records

print(records.count_documents({}))



ch={'Name' : 'Gowthaam','Age' : '','Education':'','Experience' : '','Equipment' : '','Competitors' : '','Investment' : '','Location' : '','Business Chosen' : ''}

class ValidateSimpleTailoringForm(FormValidationAction):
    fl=0
    competitors=0
    space=0
    resource=0
    skill=0

    
    def name(self) -> Text:
        return "validate_simple_tailoring_form"

    



    def validate_experience(

        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `experience` value."""
        print("c")
        
        ValidateSimpleTailoringForm.fl=ValidateSimpleTailoringForm.fl+40
        print(ValidateSimpleTailoringForm.fl)
        a=list(slot_value)
        ch["Experience"]=int(a[0])

        dispatcher.utter_message(text=f"OK!")

        return {"experience": slot_value}

    def validate_machine(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `machine` value."""
        

        if slot_value.lower()=="yes":
            print("d")
            ValidateSimpleTailoringForm.resource=1
            ValidateSimpleTailoringForm.fl=ValidateSimpleTailoringForm.fl+10
            print(ValidateSimpleTailoringForm.fl)
            dispatcher.utter_message(text=f"Great")
            return {"machine": slot_value}
        ch["Equipment"]=slot_value
        dispatcher.utter_message(text=f"Okay")
        return {"machine": slot_value}
    
    def validate_garmentkind(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `garmentkind` value."""

        print("e")
        print(ValidateSimpleTailoringForm.fl)
        dispatcher.utter_message(text=f"That's amazing")
        return {"garmentkind": slot_value}


    def validate_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `location` value."""

        print("f")
        ch["Location"]=slot_value
        print(ValidateSimpleTailoringForm.fl)
        dispatcher.utter_message(text=f"That's a beautiful place!")
        return {"location": slot_value}


    def validate_raw(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `raw` value."""

        print("g")
        print(ValidateSimpleTailoringForm.fl)
        dispatcher.utter_message(text=f"That's great to hear")
        return {"raw": slot_value}

    



    def validate_comp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `comp` value."""

        print("h")
        
        a=list(slot_value)

        x=float(a[0])
        ch["Competitors"]=int(x)

        if(x>0): 
            ValidateSimpleTailoringForm.competitors=1

        if(x<=3) :
            dispatcher.utter_message(text=f"You have a high chance of establishing your business here since there are less number of competiors")
            ValidateSimpleTailoringForm.fl=ValidateSimpleTailoringForm.fl+10
            print(ValidateSimpleTailoringForm.fl)

        else :
            dispatcher.utter_message(text=f"Seems like a lot of competitors are there in your locality. It might be a little difficult to carry out tailoring there. However answer the following questions so that we can give a comphrensive review")
            print(ValidateSimpleTailoringForm.fl)



        return {"comp": x}

    

    def validate_investment(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `investment` value."""
        y=float(slot_value)

        ch["Investment"]=y
        ch["Business Chosen"]="Tailoring"

        ValidateSimpleTailoringForm.skill=1
        if(y>=5000):
            ValidateSimpleTailoringForm.fl=ValidateSimpleTailoringForm.fl+20
            print("f")

        print("g")
        dispatcher.utter_message(text=f"Okay")
        print(ValidateSimpleTailoringForm.fl)
        if(ValidateSimpleTailoringForm.fl>75) :
            dispatcher.utter_message(text=f"The tailoring field is an amazing avenue for you to start a business!..All the best")
        else :
            classes = classifier.classes_
            attributes = []
            attributes.append([ValidateSimpleTailoringForm.competitors, ValidateSimpleTailoringForm.space, ValidateSimpleTailoringForm.resource, ValidateSimpleTailoringForm.skill])
            user_attributes = st_x.transform(attributes)    
            prediction = classifier.predict_proba(user_attributes)
            threshold = 0.1 # change this accordingly
            y_pred = []
            for index, pred in enumerate(prediction[0]):

                if pred > threshold:

                   y_pred.append(classes[index])

              
            dispatcher.utter_message(text=f"Try considering other areas of business :")

            for i in y_pred:
                if(i!="tailoring") :

                    dispatcher.utter_message(i)
        
        ValidateSimpleTailoringForm.fl=0
        #del records["_id"]
        records.insert_one(ch)


        temp=[ch["Name"],ch["Age"],10,"tailoring",4,ValidateSimpleTailoringForm.competitors,ValidateSimpleTailoringForm.space,ValidateSimpleTailoringForm.resource,ch["Investment"],ch["Experience"],"tailoring",ValidateSimpleTailoringForm.skill]
        with open('code-to-give.csv', 'a') as f_object:

  
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
  
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(temp)
    
            #Close the file object
            f_object.close()


        ch["Name"]=''
        ch["Age"]=''
        ch["Experience"]=''
        ch["Equipment"]=''
        ch["Competitors"]=''
        ch["Investment"]=''
        ch["Location"]=''
        ch["Business Chosen"]=''
        
        ValidateSimpleTailoringForm.competitors=0
        ValidateSimpleTailoringForm.space=0
        ValidateSimpleTailoringForm.resource=0
        ValidateSimpleTailoringForm.skill=0


        return {"investment": slot_value}


    

class ValidateSimpleEmbroideryForm(FormValidationAction):
    fl=0
    competitors=0
    space=0
    resource=1
    skill=4
    
    def name(self) -> Text:
        return "validate_simple_embroidery_form"

    



    def validate_experience(

        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `experience` value."""
        print("c")
        
        ValidateSimpleEmbroideryForm.fl=ValidateSimpleEmbroideryForm.fl+65
        print(ValidateSimpleEmbroideryForm.fl)
        a=list(slot_value)
        ch["Experience"]=int(a[0])

        dispatcher.utter_message(text=f"OK!")

        return {"experience": slot_value}

    
    
    


    def validate_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `location` value."""

        print("f")
        ch["Location"]=slot_value
        print(ValidateSimpleEmbroideryForm.fl)
        dispatcher.utter_message(text=f"That's a beautiful place!")
        return {"location": slot_value}


    def validate_raw(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `raw` value."""

        print("g")
        print(ValidateSimpleEmbroideryForm.fl)
        dispatcher.utter_message(text=f"That's great to hear")
        return {"raw": slot_value}

    



    def validate_comp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `comp` value."""

        print("h")
        
        a=list(slot_value)

        x=float(a[0])
        ch["Competitors"]=int(x)

        if(x>0) :
            ValidateSimpleEmbroideryForm.competitors=1

        if(x<=3) :

            dispatcher.utter_message(text=f"You have a high chance of establishing your business here since there are less number of competiors")
            ValidateSimpleEmbroideryForm.fl=ValidateSimpleEmbroideryForm.fl+10
            print(ValidateSimpleEmbroideryForm.fl)

        else :
            dispatcher.utter_message(text=f"Seems like a lot of competitors are there in your locality. It might be a little difficult to carry out embroidery there. However answer the following questions so that we can give a comphrensive review")
            print(ValidateSimpleEmbroideryForm.fl)



        return {"comp": x}

    

    def validate_investment(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `investment` value."""
        y=float(slot_value)

        ch["Investment"]=y
        ch["Business Chosen"]="Embroidery"


        if(y>=5000):
            ValidateSimpleEmbroideryForm.fl=ValidateSimpleEmbroideryForm.fl+20
            print("f")

        print("g")
        dispatcher.utter_message(text=f"Okay")
        print(ValidateSimpleEmbroideryForm.fl)
        if(ValidateSimpleEmbroideryForm.fl>75) :
            dispatcher.utter_message(text=f"The embroidery field is an amazing avenue for you to start a business!..All the best")
        else :
            classes = classifier.classes_
            attributes = []
            attributes.append([ValidateSimpleEmbroideryForm.competitors, ValidateSimpleEmbroideryForm.space, ValidateSimpleEmbroideryForm.resource,ValidateSimpleEmbroideryForm.skill])
            user_attributes = st_x.transform(attributes)    
            prediction = classifier.predict_proba(user_attributes)
            threshold = 0.1 # change this accordingly
            y_pred = []
            for index, pred in enumerate(prediction[0]):

                if pred > threshold:

                   y_pred.append(classes[index])

              
            dispatcher.utter_message(text=f"Try considering other areas of business :")

            for i in y_pred:
                if(i!="embroidery") :

                    dispatcher.utter_message(i)
            
        
        ValidateSimpleEmbroideryForm.fl=0
        
        records.insert_one(ch)
        

        temp=[ch["Name"],ch["Age"],10,"embroidery",4,ValidateSimpleEmbroideryForm.competitors,ValidateSimpleEmbroideryForm.space,ValidateSimpleEmbroideryForm.resource,ch["Investment"],ch["Experience"],"embroidery",ValidateSimpleEmbroideryForm.skill]
        with open('code-to-give.csv', 'a') as f_object:

  
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
  
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(temp)
    
            #Close the file object
            f_object.close()

        ch["Name"]=''
        ch["Age"]=''
        ch["Experience"]=''
        ch["Equipment"]=''
        ch["Competitors"]=''
        ch["Investment"]=''
        ch["Location"]=''
        ch["Business Chosen"]=''


        ValidateSimpleEmbroideryForm.competitors=0
        ValidateSimpleEmbroideryForm.space=0
        ValidateSimpleEmbroideryForm.resource=0
        ValidateSimpleEmbroideryForm.skill=0




        return {"investment": slot_value}





























class ValidateSimpleDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_details_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        print("a")
        ch["Name"]=slot_value

        dispatcher.utter_message(text=f"Hello!! {slot_value} ")
        return {"name": slot_value}

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `age` value."""

        x=int(slot_value)
        print("b")

        if x<=1 or x>100:
            dispatcher.utter_message(text=f"Please enter a valid age")
            return {"age": None}
        ch["Age"]=x
        dispatcher.utter_message(text=f"Thank you")
        return {"age": slot_value}

class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]






class ValidateSimpleFarmingForm(FormValidationAction):
    fl=0
    
    def name(self) -> Text:
        return "validate_simple_farming_form"

    



    def validate_experience(

        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `experience` value."""
        print("c")
        
        ValidateSimpleFarmingForm.fl=ValidateSimpleFarmingForm.fl+65
        print(ValidateSimpleFarmingForm.fl)
        a=list(slot_value)
        ch["Experience"]=int(a[0])

        dispatcher.utter_message(text=f"OK!")

        return {"experience": slot_value}

    
    
    


    def validate_location(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `location` value."""

        print("f")
        ch["Location"]=slot_value
        print(ValidateSimpleFarmingForm.fl)
        dispatcher.utter_message(text=f"That's a beautiful place!")
        return {"location": slot_value}


    def validate_land(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `raw` value."""

        print("g")
        print(ValidateSimpleFarmingForm.fl)
        l=str(slot_value)
        print(l)
        if(l.lower()=="yes") :
            print(l[0])
            ValidateSimpleFarmingForm.fl=ValidateSimpleFarmingForm.fl+50
            dispatcher.utter_message(text=f"That's great to hear")
            return {"raw": slot_value}

        dispatcher.utter_message(text=f"Difficult to earn profits without owning a land")
        return {"raw": slot_value}

    



    def validate_comp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `comp` value."""

        print("h")
        
        a=list(slot_value)

        x=float(a[0])
        ch["Competitors"]=int(x)

        if(x<=3) :
            dispatcher.utter_message(text=f"You have a high chance of establishing your business here since there are less number of competiors")
            ValidateSimpleFarmingForm.fl=ValidateSimpleFarmingForm.fl+10
            print(ValidateSimpleFarmingForm.fl)

        else :
            dispatcher.utter_message(text=f"Seems like a lot of competitors are there in your locality. It might be a little difficult to carry out embroidery there. However answer the following questions so that we can give a comphrensive review")
            print(ValidateSimpleFarmingForm.fl)



        return {"comp": x}

    

    def validate_investment(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `investment` value."""
        y=float(slot_value)

        ch["Investment"]=y
        ch["Business Chosen"]="Farming"


        if(y>=5000):
            ValidateSimpleFarmingForm.fl=ValidateSimpleFarmingForm.fl+20
            print("f")

        print("g")
        dispatcher.utter_message(text=f"Okay")
        print(ValidateSimpleFarmingForm.fl)
        if(ValidateSimpleFarmingForm.fl>60) :
            dispatcher.utter_message(text=f"Farming is an amazing avenue for you to start a business!..All the best")
        else :
            dispatcher.utter_message(text=f"Try considering other areas of business")
        
        ValidateSimpleFarmingForm.fl=0
        #del records['_id']
        records.insert_one(ch)

        ch["Name"]=''
        ch["Age"]=''
        ch["Experience"]=''
        ch["Equipment"]=''
        ch["Competitors"]=''
        ch["Investment"]=''
        ch["Location"]=''
        ch["Business Chosen"]=''

        return {"investment": slot_value}


