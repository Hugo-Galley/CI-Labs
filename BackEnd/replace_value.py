import json
import os

with open("variables.json") as f:
    data = json.load(f)

data["Log"]["FileDestination"] = os.environ["FILE_DESTINATION"]
data["Bdd"]["Host"] = os.environ["BDD_HOST"]
data["Bdd"]["Database"] = os.environ["BDD_DATABASE"]
data["Bdd"]["User"] = os.environ["BDD_USER"]
data["Bdd"]["Password"] = os.environ["BDD_PASSWORD"]
data["Bdd"]["Port"] = os.environ["BDD_PORT"]

with open("variables.json", "w") as f:
    json.dump(data, indent=4)
