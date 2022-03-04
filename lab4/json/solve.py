import json

with open('sample-data.json','r') as file:
    data = json.load(file)
print("Interface Status")
print("================================================================================")
print("DN Description Speed MTU ")
print("-------------------------------------------------- -------------------- ------ ------")
for i in data["imdata"]: print(i["l1PhysIf"]["attributes"]["dn"]," "*28,i["l1PhysIf"]["attributes"]["fecMode"]," "*1,i["l1PhysIf"]["attributes"]["mtu"])