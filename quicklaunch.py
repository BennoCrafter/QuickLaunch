#!/usr/bin/python3

import os
import argparse
import subprocess
import json
from typing import List, Optional
from alias_manager import generate_aliases_file, create_new_alias
from models.action import Action
from models.alias_data import AliasData
from models.alias import Alias
from consts import *

os.makedirs(CONFIG_DIR, exist_ok=True)

if not os.path.exists(CONFIG_FILE):
    generate_aliases_file()


class ProjectConfig:
    def __init__(self, aliases: List[Alias]) -> None:
        self.aliases: List[Alias] = aliases

    def get_alias(self, alias_name: str) -> Optional[Alias]:
        for a in self.aliases:
            if a.alias == alias_name:
                return a
        return None

    def get_all_aliases(self) -> str:
        s = ""
        for a in self.aliases:
            s += f"  {a.alias}: {a.description}\n"
        return s

def load_aliases_from_json(file_path: str) -> ProjectConfig:
    with open(file_path, 'r') as file:
        data = json.load(file)

    aliases = []
    for alias in data["aliases"]:
        action = Action(**alias["data"]["action"])
        alias_data = AliasData(path=alias["data"]["path"], action=action)
        aliases.append(Alias(alias=alias["alias"], description=alias["description"], data=alias_data))

    return ProjectConfig(aliases)

def execute_alias(alias: Alias):
    if alias.data.action.action == "open":  # Compare the 'action' attribute of the Action object
        subprocess.run(["open", "-a", alias.data.action.args[0], alias.data.path])
        print(f"✅ Opened {alias.data.get_last_path_component()}")

def main(config: ProjectConfig):
    parser = argparse.ArgumentParser(
        description=(
            "\n"
            "  🚀  Open your favorite projects instantly!  🚀\n"
            "\n"
            "Quickly open projects using an alias you've defined.\n\n"
            "📌 **Available Aliases:**\n" +
            config.get_all_aliases() +
            "\n"
            "🛠️ **Usage:**\n"
            "  Setup in your .zshrc file an alias for this project.\n\n"
            "❓ **Example:**\n"
            "  ql t  # Opens 'TimetableApp'\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter  # Preserve formatting
    )

    parser.add_argument(
        "alias",
        type=str,
        nargs='?',
        help="The alias of your project (e.g., 't' for TimetableApp)."
    )

    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="Show all available aliases."
    )

    parser.add_argument('--add', "-a", nargs=5, metavar=('ALIAS', 'DESCRIPTION', 'ACTION', 'PATH', 'ARG'),
                            help='Add a name and a description')

    args = parser.parse_args()

    if args.add:
        create_new_alias(args.add)
        return

    if args.list or not args.alias:
        print("\n📋 **Available Aliases:**\n")
        print(config.get_all_aliases())
        return

    alias = config.get_alias(args.alias)

    if not alias:
        print(f"❌ Alias '{args.alias}' not found. Please check your configuration or try a different alias.")
        return

    execute_alias(alias=alias)


if __name__ == "__main__":
    # Load aliases from the JSON file
    project_config = load_aliases_from_json(CONFIG_FILE)
    main(config=project_config)
