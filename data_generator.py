import argparse
from faker import Faker
import json
# import pprint

parser = argparse.ArgumentParser(description="Process data set generator parameters")

# Options for data_set_size are "test" or "demo"
parser.add_argument('data_set_option')
parser.add_argument('data_set_size', type=int)
args = parser.parse_args()

fake = Faker()
data_set = []

for x in range(1, args.data_set_size + 1):
    if args.data_set_option == "test":
        item = {
            "countTest": x,
            "color": fake.color_name()
        }
    else:
        item = {
            "countDemo": x,
            "person": fake.name()
        }
    data_set.append(item)

# Leaving this code in case of debugging needs
# pp = pprint.PrettyPrinter()
# pp.pprint(data_set)

with open(F"{args.data_set_option}_data.json", "w") as outfile:
    json.dump(data_set, outfile)
