import requests 
from pprint import pprint
from pydantic import BaseModel , confloat, field_validator, Field, model_validator
from datetime import date, datetime, timedelta
import uuid
from typing import Literal
from enums import DepartmentEnum
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()




class Module(BaseModel):
    id: int | uuid.UUID 
    name:str
    professor:str
    # FOr fixed number of values
    credits:Literal[10, 20]
    registration_code : str


# Modeling and defineing the data type for each fields
class Student(BaseModel):
    # can be done while converting to dict 
    id:uuid.UUID= Field(exclude=True)
    name:str
    # Custom Constrained type
    date_of_birth: date = Field(default_factory = lambda: datetime.today().date())
    #Constrained Type
    GPA: confloat(ge=0,le=4)
    course:str| None | int # Can be a union of any Union[str,None] also can be done using OPTIONAL
    # Enum small number of possible values  
    department:DepartmentEnum
    modules:list[Module] = Field(default=[], max_items=10) # default value = empty list

    class Config:
        # Output real value of enum rather than the object itself
        use_enum_values=True
        title = 'Student Model'
        extra = 'allow'

    @model_validator(mode='after')
    def validate_gpa_and_department(cls,values):
        dept = values.department
        gpa = values.GPA
        dept_scienc = dept == DepartmentEnum.SCIENCE_AND_ENGINEERING
        if dept_scienc and gpa <= 3.0:
                raise ValueError("GPA must be 3.0 or higher")
        return values


    @field_validator('GPA')
    def validate_gpa(cls,value,values):
        pass

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



for student in data:
    #Unpacking the json in our model
    try:
        model = Student(**student)
        print(f'GPA: {model.GPA},Department : {model.department}')
    except ValueError as e:
        print(e)
    # pprint(model)

### Root Validator run alidation on entire after the single validation of fileds is done 




