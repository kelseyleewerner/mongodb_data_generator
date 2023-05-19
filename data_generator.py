from faker import Faker
import json
# import pprint
import sys

# Options for data_set_size are "test" or "demo"
data_set_option = sys.argv[1]
data_set_size = int(sys.argv[2]) + 1

fake = Faker()
data_set = []

for x in range(1, data_set_size):
    if data_set_option == "test":
        item = {
            "count_test": x,
            "color": fake.color_name()
        }
    else:
        item = {
            "count_demo": x,
            "person": fake.name()
        }
    data_set.append(item)

# pp = pprint.PrettyPrinter()
# pp.pprint(data_set)

with open(F"{data_set_option}_data.json", "w") as outfile:
    json.dump(data_set, outfile)
