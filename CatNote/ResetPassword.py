import os
def ResetPassword():
    os.remove("./MyPassword.txt")
    f = open("MyPassword.txt", "w");
    f.close()
def SetPassword(Password):
    f = open("./MyPassword.txt", "w");
    f.write(Password)
    f.close()
def ConfirmPassword(Password):
    f = open("./MyPassword.txt", "r");
    line = f.readline()
    if line == Password: return True
    else: return False
