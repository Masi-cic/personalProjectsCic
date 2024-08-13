import  bcrypt

password = "danielmasiorango"
password1 = "danielmasiorango1"

#generating a salt and hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(hashed_password)

if bcrypt.checkpw(password1.encode('utf-8'), hashed_password):
    print("password match")
else:
    print("password does not match")
