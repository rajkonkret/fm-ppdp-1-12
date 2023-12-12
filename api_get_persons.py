from pydantic import BaseModel
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)
print(response)
data = response.json()
print(data)


# 'name': {
#     'title': 'Mr',
#     'first': 'Humberto',
#     'last': 'Haro'
# }
class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture


# {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Trifun', 'last': 'Borojević'},
#               'location': {'street': {'number': 1137, 'name': 'Veštih Pletilja'}, 'city': 'Žitorađa', 'state': 'Rasina',
#                            'country': 'Serbia', 'postcode': 16964,
#                            'coordinates': {'latitude': '60.7172', 'longitude': '-50.7248'},
#                            'timezone': {'offset': '+11:00', 'description': 'Magadan, Solomon Islands, New Caledonia'}},
#               'email': 'trifun.borojevic@example.com',
#               'login': {'uuid': 'd1f1efb1-10c6-44e2-87d7-c9d56c6823ff', 'username': 'smallladybug794',
#                         'password': 'hotass', 'salt': 'haVyq4ka', 'md5': 'd5a30ed3e43e6ccf215b4451bea77039',
#                         'sha1': '15f26c9f2b26779e78ac34a6ce091fad729d9836',
#                         'sha256': 'f7eb7ee969a1cb002019b7557928af93b4f304b7b1de737174aeee0211a8e9c2'},
#               'dob': {'date': '1980-01-18T10:32:45.584Z', 'age': 43},
#               'registered': {'date': '2018-09-16T04:24:56.480Z', 'age': 5}, 'phone': '027-4511-997',
#               'cell': '069-2582-408', 'id': {'name': 'SID', 'value': '536733870'},
#               'picture': {'large': 'https://randomuser.me/api/portraits/men/31.jpg',
#                           'medium': 'https://randomuser.me/api/portraits/med/men/31.jpg',
#                           'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/31.jpg'}, 'nat': 'RS'}],
#  'info': {'seed': '860b1b2a6b88b029', 'results': 1, 'page': 1, 'version': '1.4'}}
print(data['results'][0]['email'])  # stella.dutko@example.com
print(data['results'][0]['picture'])  # stella.dutko@example.com
photo_url = data['results'][0]['picture']['large']
response_photo = requests.get(photo_url)
with open("user_photo.jpg", 'wb') as f:
    f.write(response_photo.content)

user = data['results'][0]
user_info = UserInfo(**user)
print(user_info)
print(type(user_info))  # <class '__main__.UserInfo'>
response_photo_pydantic = requests.get(user_info.picture.large)
with open('user_phto_pydantic.jpg', 'wb') as f:
    f.write(response_photo_pydantic.content)
