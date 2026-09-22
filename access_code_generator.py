def generate_code(name, key):
    if key % 2 == 0:
        return f"The member: {name} access is granted."
    return f"The member: {name} is denied."


first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
numeric_key = int(input("What's your numeric key?: "))

formatted_name = f"{first_name.title()} {last_name.title()}"

result = generate_code(formatted_name, numeric_key)
print(result)
