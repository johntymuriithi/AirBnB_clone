#!/usr/bin/python3

# Write tests for the Base Model that all other classes inherits from

from models.base_model import BaseModel

my_model = BaseModel()
print(my_model)
print("==================================================================================================")
print(my_model.__dict__)

#my_model.name = "My First Model"
#my_model.my_number = 89
#print(my_model)
#my_model.save()
#print(my_model)
#my_model_json = my_model.to_dict()
#print(my_model_json)
#print("JSON of my_model:")
#for key in my_model_json.keys():
 #   print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
