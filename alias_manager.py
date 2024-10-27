import os
import json
from consts import *
from models.alias import Alias
from models.alias_data import AliasData
from models.action import Action

def generate_aliases_file():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as json_file:
            json.dump({"aliases": []}, json_file, indent=4)
        print(f"✅Default aliases.json created at {CONFIG_FILE}")

def create_new_alias(args: list):
    if len(args) < 5:
        print("Error: Not enough arguments to create an alias. Provide ALIAS, DESCRIPTION, ACTION, and PATH.")
        return

    alias_name = args[0]
    description = args[1]
    action_str = args[2]
    path = args[3]

    # Create the Action object
    action = Action(action=action_str, args=args[4:])

    # Create the AliasData object
    alias_data = AliasData(path=path, action=action)

    # Create the Alias object
    new_alias = Alias(alias=alias_name, description=description, data=alias_data)

    # Load existing aliases
    with open(CONFIG_FILE, 'r') as json_file:
        data = json.load(json_file)

    # Append new alias to the existing list
    data['aliases'].append(new_alias.to_dict())

    # Write updated aliases back to the file
    with open(CONFIG_FILE, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"✅ Alias '{new_alias.alias}' added successfully.")
