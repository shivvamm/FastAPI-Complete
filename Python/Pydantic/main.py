import requests 
from pydantic import BaseModel , confloat, field_validator
from datetime import date, datetime, timedelta
import uuid
from typing import Literal
from enums import DepartmentEnum
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
# data[-1]["modules"].append(
#     {
#         "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
#         "name": "Eric Travis",
#         "professor": "John Doe",
#         "credits": 20,
#         "registration_code": "ABC123"
#     }
# )


# data.append({
#         "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
#         "name": "Eric Travis",
#         "date_of_birth": "2010-05-25",
#         "GPA": "5.0",
#         "course": "Computer Science",
#         "department": "Science and Engineering",
#         "fees_paid": False,
#         "modules": []
#     })


class Module(BaseModel):
    id: int | uuid.UUID 
    name:str
    professor:str
    # FOr fixed number of values
    credits:Literal[10, 20]
    registration_code : str


# Modeling and defineing the data type for each fields
class Student(BaseModel):
    id:uuid.UUID
    name:str
    # Custom Constrained type
    date_of_birth: date 
    #Constrained Type
    GPA: confloat(ge=0,le=4)
    course:str| None | int # Can be a union of any Union[str,None] also can be done using OPTIONAL
    # Enum small number of possible values  
    department:DepartmentEnum
    fees_paid:bool
    modules:list[Module] = [] # default value = empty list


    @field_validator('modules')
    def validate_module_length(cls,value):
        if len(value) and len(value) != 3:
            raise ValueError("Modules must be 3")
        return value
     

    @field_validator('date_of_birth')
    def ensure_16_or_over(cls,value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        if value > sixteen_years_ago.date():
            raise ValueError("Student must be 16 or older")
        return value



# for student in data:
#     #Unpacking the json in our model
#     model = Student(**student)
#     # for module in model.modules:
#     #     print(module.id)
#     # Convert into Dictionary for Further use with all the complex data types maintaintng the data objects 
#     print(model.model_dump())

# print("### Json")
# for student in data:
#     model = Student(**student)
#     # Converting everyhtign to string for serialize (convert from objects to simple strings)
#     print(model.model_dump_json())



# Jshom Schema to share with other devs for validation in other languages
print(Module.model_json_schema())
 
