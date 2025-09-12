import string
import random
import getpass
def password_checker(password):
    issues=[]
    if len(password)<8:
        issues.append("too short password")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing puncuation ")
    return issues
def generate_strong_password(length=12):
    chars= string.ascii_letters+string.digits+string.punctuation
    return "".join(random.choice(chars) for _ in range(length))
password= getpass.getpass("Enter a password : ")
issues = password_checker(password)
if not issues:
    print("Strong password")
else:
    print("Weak password")
    print(issues)
suggestion= generate_strong_password()

print("\n Suggesting you a strong password")
print(suggestion)
        