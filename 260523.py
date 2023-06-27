from schema import Schema
# from functions import get_function
import os
from faker import Faker
 
from faker import Faker
fake = Faker()

# print(fake.name())
# # 'Lucy Cechtelar'

# print(fake.address())
# # '426 Jordy Lodge
# #  Cartwrightshire, SC 88120-6700'

# print(fake.text() )


print(fake.first_name())

print(fake.last_name())
print(fake.email())
 
# schema = Schema({
#     'email': str,
#     'first_name': str,
#     'last_name': str
# })
 
# schema.is_valid({'email': 'Zion.Reichel12@yahoo.com',
#                  'first_name': 'Elizabeth',
#                  'last_name': 'Zulauf'}) # True
# schema.is_valid({'email': 'Zion.Reichel12@yahoo.com'}) # False



# faker = Faker()


# def get_default_data():
#     return {
#         "first_name": faker.first_name(),
#         "last_name": faker.last_name(),
#         "email": faker.email(),
#     }


# def _right(data={}):
#     default_data = get_default_data()
#     return {**default_data, **data}


# def _fail1(data={}):
#     data = data
#     return get_default_data()


# def _fail2(data={}):
#     default_data = get_default_data()
#     age_data = {"age": faker.random_int()}
#     return {**default_data, **data, **age_data}


# def _fail3(data={}):
#     faker.seed_instance(123)
#     default_data = get_default_data()
#     return {**default_data, **data}


# functions = {
#     "right": _right,
#     "fail1": _fail1,
#     "fail2": _fail2,
#     "fail3": _fail3,
# }


# def get_function():
#     name = os.environ['FUNCTION_VERSION']
#     return functions[name]



# build_user = get_function()
 
# print(build_user())
# # => {'email': 'Zion.Reichel12@yahoo.com', 'first_name': 'Elizabeth', 'last_name': 'Zulauf'}

# print(build_user({'first_name': 'Petya'}))
# # => {'email': 'Zion.Reichel12@yahoo.com', 'first_name': 'Petya', 'last_name': 'Zulauf'}