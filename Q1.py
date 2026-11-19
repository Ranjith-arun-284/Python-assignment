username = input("Enter a username: ")
cleaned_username = username.strip()
lowercase_username = username.lower()

if cleaned_username == "":
    print("Invalid username: it must not contain only spaces.")
elif len(username) < 5:
    print("Invalid username: it must contain at least 5 characters.")
elif lowercase_username == "admin":
    print("Invalid username: 'admin' is not allowed (in any uppercase/lowercase form).")
else:
    print("Valid username!")
