import getpass

database = {"satyajit.senapati": "qazwsx", "shashi.behera": "123456789"}

username = input("Enter your user name: ")
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break
    
print("verified")