import json

person = '{ "name":"john", "email":"john@gmail.com","age":35}'

i = json.loads(person)

print(i["name"] + " " + i["email"] + " ", i["age"])