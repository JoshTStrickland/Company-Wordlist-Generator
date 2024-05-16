import os

def generate_passwords(company_name, output_dir):
    # Basic variations of the company name
    base_forms = [
        company_name.lower(),
        company_name.upper(),
        company_name.capitalize()
    ]

    # Common substitutions that users might realistically use
    substitutions = {'a': ['@', '4'], 'i': ['1', '!'], 'e': ['3'], 'o': ['0'], 's': ['5', '$']}
    # Common additions
    suffixes = ['123', '!', '2023', '2022', '2021', '2020', '2024', '1', '111', 'summer', 'fall', 'spring', 'winter']

    passwords = set()

    # Generate passwords based on basic forms
    for form in base_forms:
        passwords.add(form)  # Add the basic form itself
        # Apply common substitutions recursively
        for subbed in apply_substitutions(form, substitutions):
            passwords.add(subbed)
            # Add numbers and special characters
            for suffix in suffixes:
                passwords.add(subbed + suffix)

    # Write to file
    output_file = os.path.join(output_dir, f"{company_name}_ban_list.txt")
    with open(output_file, "w") as file:
        for password in sorted(passwords):
            file.write(password + "\n")

def apply_substitutions(text, subs, current=""):
    if not text:
        yield current
    else:
        first, rest = text[0], text[1:]
        if first.lower() in subs:
            for replacement in subs[first.lower()]:
                # Continue substituting the rest of the string after replacing the current character
                yield from apply_substitutions(rest, subs, current + replacement)
        # Always yield the version with the current character unchanged
        yield from apply_substitutions(rest, subs, current + first)

def get_desktop_path():
    return os.path.join(os.path.expanduser('~'), 'Desktop')

# Prompt the user for the company name
company_name = input("Enter the company name to generate the ban list: ")
output_dir = get_desktop_path()

# Generate the passwords
generate_passwords(company_name, output_dir)
print(f"Password ban list generated and saved to {output_dir}/{company_name}_ban_list.txt")
