# auto-proyect-python
 This Python script automates the creation and management of development projects. It handles tasks like setting up virtual environments, organizing project directories, and opening files in NeoVim, all via the command line. It's perfect for developers looking to streamline their workflow when starting or resuming projects.
# 💻 Project Management Script

## Overview

This script is designed to streamline your Python project management process by automating tasks such as creating project directories, setting up virtual environments, and opening projects in NeoVim. It's especially useful for developers who frequently start new projects or revisit existing ones.

## Features

- **Project Setup Automation**: Easily create new project directories with pre-defined structures.
- **Virtual Environment Creation**: Automatically set up a Python virtual environment for your projects.
- **Project Management**: List and open existing projects in NeoVim with a single command.
- **Customizable**: The script uses color customization via `colorama` for a more visually appealing CLI experience.

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/project-management-script.git
    cd project-management-script
    ```

2. **Run the Script:**
    ```bash
    python3 script_name.py
    ```

3. **Select an Option:**
    - **1**: Start a new project.
    - **2**: Resume a previous project.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **NeoVim**: The script uses NeoVim (`nvim`) for opening and editing project files.
- **Colorama**: The script uses the `colorama` library for colored output. Install it using:
    ```bash
    pip install colorama
    ```

## Customization

- **System Paths**: Update the `HOME` and `RUTE` variables in the `mode` class to match your directory structure.
- **Color Scheme**: Modify the color variables in the `mode` class to customize the CLI's appearance.

## Example

When running the script, you will be greeted with the following options:

```plaintext
Hello SKULL, are we going to program a new script or resume a previous project?

[1] Nuevo poyecto
[2] Retoma de proyecto anterior
