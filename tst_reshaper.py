from smuggler import pre_processor as proc
import json

with open('./json/main2.json', "r") as fp:
    json_data = json.loads(fp.read())

json_data = proc.canonicalize_json_data(json_data, True)
reshaped_data = proc.reshape_json_data(json_data, True)


#print("\n\n\n primary_data")
print(json.dumps(reshaped_data['primary_data'], indent=2))
exit(0)

print("\n\n\n municipality_data")
print(json.dumps(reshaped_data['primary_data']['municipality_data'], indent=2))

print("\n\n\n property_deeds")
print(json.dumps(reshaped_data['primary_data']['property_deeds'], indent=2))
# print(reshaped_data['primary_data']['municipality_data'])
# print(reshaped_data["primary_data"]["tax_rates"])
