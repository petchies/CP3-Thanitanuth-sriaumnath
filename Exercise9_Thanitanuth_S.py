usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "petch88":
    print("Wrong username or password, Please try to login again")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Login success")