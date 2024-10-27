# QuickLaunch

QuickLaunch is a simple Python-based tool to quickly open your favorite projects using predefined aliases. Instead of navigating through directories or remembering long paths, you can use easy-to-remember aliases to launch projects and files effortlessly.

## Features

Quickly open projects with a predefined alias.
Easily list all available aliases.
Add new aliases with a simple command.

## Requirements

Python 3.x
macOS (for the open command)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/BennoCrafter/QuickLaunch
cd QuickLaunch
```

### Step 2: Set Up Your Virtual Environment (optional)
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows use `venv\Scripts\activate`

### Step 4: Install quicklaunch
Just run
```bash
sh add_quicklaunch.sh
```

### Step 4: Create and Configure Aliases
You will need to define the aliases in a JSON file (default: ~/.config/quicklaunch/aliases.json). You can create your own aliases using the --add flag or manually edit this JSON file.

##### JSON Structure Example
```json
{
  "aliases": [
    {
      "alias": "t",
      "description": "Opens the TimetableApp",
      "data": {
        "path": "/Users/username/projects/TimetableApp",
        "action": {
          "action": "open",
          "args": ["Visual Studio Code"]
        }
      }
    }
  ]
}

```

### Usage

##### Basic Command
```bash
ql <alias name>
```

#### Listing All Available Aliases
```bash
ql -l
```
This command will show a list of all aliases available.

#### Adding a New Alias
```bash
ql --add <ALIAS> <DESCRIPTION> <ACTION> <PATH> <ARG>
```

```yaml
ALIAS: Short name for the alias (e.g., "t" for TimetableApp).
DESCRIPTION: A short description of the alias.
ACTION: The action to perform, e.g., "open".
PATH: The full path of the project or file.
ARG: The application to use (e.g., "Visual Studio Code").
```

For example:

```bash
ql --add "p" "Opens My cool Project" "open" "/Users/username/projects/MyCoolProject" "Visual Studio Code"
```
