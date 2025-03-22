#check password
has_upper=False
has_lower=False
has_digit=False
has_special=False
special_char=["!","~","`","@","#","$","₹","%","^","&","*","(",")","_",".","/","?"]
def is_password_valid(p):
    if len(p)<6 or len(p)>14:
        print("Passowrd must have 6 to 14 characters")
    for char in p:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in special_char:
            has_special=True
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    elif not has_lower:
        return "Password must contain at least one lowercase letter."
    elif not has_digit:
        return "Password must contain at least one digit."
    elif not has_special:
        return "Password must contain at least one special character ($, @, #, %)."
    else:
        return "Password Valid"
def main():
    password=input("Enter a password: ")
    res=is_password_valid(password)
    print(res)
main()