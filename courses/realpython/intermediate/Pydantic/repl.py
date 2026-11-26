from uuid import uuid4
from pydantic_models import Employee

print(uuid4())

# Valid Employee
employee = Employee(
   employee_id = uuid4(),
   name="Luis Lazu",
   email="lazu@gmail.com",
   date_of_birth="1984-06-11",
   salary= 123_000,
   department="IT",
   elected_benefits=True
)

"""
# In-valid Employee
Employee(
   employee_id = "abc",
   name="123",
   email="your-name",
   date_of_birth="xyz",
   salary= 123_000,
   department="1.0",
   elected_benefits=1000
)
"""

new_employee_dict= {
   "employee_id": uuid4(),
   "name":"Luis Lazu",
   "email": "lazu@gmaul.com",
   "date_of_birth": "1984-06-11",
   "salary": 123_000,
   "department": "IT",
   "elected_benefits": True
}

new_employee_json = f"""
{{   
    "employee_id": "{uuid4()}",
    "name": "Brian Lewis",
    "email": "brian@gmail.com",
    "date_of_birth": "1990-11-13",
    "salary": 200000.00,
    "department": "HR",
    "elected_benefits": false
}}  
"""



val = Employee.model_validate(new_employee_dict)
print(val)

new_employee = Employee.model_validate_json(new_employee_json)
print(new_employee)