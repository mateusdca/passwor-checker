while True:
    password = input("Enter a password: ")
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["uppercase"] = uppercase

    print(result)
    if all(result.values()):
        print("Strong password.")
        break
    else:
        print("Weak password.")