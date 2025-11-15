import json
import os

base_dir = os.path.dirname(__file__)
vars_path = os.path.join(base_dir, "variables.json")

with open(vars_path, "r") as f:
    data = json.load(f)

data["Log"]["FileDestination"] = os.environ.get(
    "FILE_DESTINATION", data["Log"].get("FileDestination")
)
data["Bdd"]["Host"] = os.environ.get("BDD_HOST", data["Bdd"].get("Host"))
data["Bdd"]["Database"] = os.environ.get("BDD_DATABASE", data["Bdd"].get("Database"))
data["Bdd"]["User"] = os.environ.get("BDD_USER", data["Bdd"].get("User"))
data["Bdd"]["Password"] = os.environ.get("BDD_PASSWORD", data["Bdd"].get("Password"))
data["Bdd"]["Port"] = os.environ.get("BDD_PORT", data["Bdd"].get("Port"))

with open(vars_path, "w") as f:
    json.dump(data, f, indent=4)
