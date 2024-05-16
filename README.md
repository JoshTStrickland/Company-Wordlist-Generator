# Password Ban List Generator

## Overview
The Password Ban List Generator is a Python script designed to create a comprehensive list of potential weak passwords based on a company's name. The script generates passwords by applying common character substitutions and suffixes to the basic forms of the company name. This tool aims to assist system administrators and security professionals in pre-emptively banning commonly used weak passwords that could make systems vulnerable to attacks.

## Features
- **Basic Form Variations**: Generates passwords using the lowercase, uppercase, and capitalized versions of the company name.
- **Substitutions**: Applies common leetspeak substitutions (e.g., replacing 'a' with '@' or '4').
- **Suffixes**: Adds common numerical sequences and keywords like years, 'admin', and 'access'.
- **Flexibility**: Easy to customize with different substitutions or suffixes based on specific security requirements.

## Requirements
- Python 3.x
- OS Module (standard library)
- Access to a local or network file system for saving the output file.

## Installation
No additional installation is required apart from a standard Python setup. Ensure that Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/) if not already installed.

## Usage
To use the Password Ban List Generator, follow these steps:

1. **Clone or download this repository** to your local machine.
2. **Navigate to the script's directory** in your command line or terminal.
3. **Run the script** using Python:

   ```bash
   python company_passwords.py
