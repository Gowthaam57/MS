from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from sqlalchemy import Float
import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient
import urllib


password=urllib.parse.quote_plus('Lakshana@57')
client = pymongo.MongoClient("mongodb+srv://Gowthaam:%s@buzz.qjh5k.mongodb.net/?retryWrites=true&w=majority"%(password))
db = client.get_database('BuzzWomen')
records=db.Records

print(records.count_documents({}))



ch={'Name' : 'Gowthaam','Age' : '','Education':'','Experience' : '','Equipment' : '','Competitors' : '','Investment' : '','Location' : '','Business Chosen' : ''}

class ValidateSimpleTailoringForm(FormValidationAction):
    fl=0
    
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


        if(y>=5000):
            ValidateSimpleTailoringForm.fl=ValidateSimpleTailoringForm.fl+20
            print("f")

        print("g")
        dispatcher.utter_message(text=f"Okay")
        print(ValidateSimpleTailoringForm.fl)
        if(ValidateSimpleTailoringForm.fl>75) :
            dispatcher.utter_message(text=f"The tailoring field is an amazing avenue for you to start a business!..All the best")
        else :
            dispatcher.utter_message(text=f"Try considering other areas of business")
        
        ValidateSimpleTailoringForm.fl=0
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


    

class ValidateSimpleEmbroideryForm(FormValidationAction):
    fl=0
    
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
        ch["Business Chosen"]="Tailoring"


        if(y>=5000):
            ValidateSimpleEmbroideryForm.fl=ValidateSimpleEmbroideryForm.fl+20
            print("f")

        print("g")
        dispatcher.utter_message(text=f"Okay")
        print(ValidateSimpleEmbroideryForm.fl)
        if(ValidateSimpleEmbroideryForm.fl>75) :
            dispatcher.utter_message(text=f"The embroidery field is an amazing avenue for you to start a business!..All the best")
        else :
            dispatcher.utter_message(text=f"Try considering other areas of business")
        
        ValidateSimpleEmbroideryForm.fl=0
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


    