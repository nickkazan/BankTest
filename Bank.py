#Fake Bank Account Program
#Name: Nicholas Kazan
#Date: September 18, 2017
import os

def createAccount(money):
    user = input("We need a new username for you: ")
    print("Welcome " + user + " !")
    password = input("Now we will need a password for your account: ")
    print("From now on you will need to use this log in! We will credit you $100 to get your account started!")
    money += 100.0
    path = ("/Users/nickkazan/Desktop/" + user)
    if not os.path.isdir(path):
        os.mkdir(path)
    with open(os.path.join(path, 'balance.txt'), 'w+') as temp_file:
        temp_file.write(str(money))
    with open(os.path.join(path, 'login.txt'), 'w+') as temp_file2:
        temp_file2.write('user:' + user + '\n' + 'pass:' + password)
    loopStats(money, user, password)
    return;

def loopStats(money, user, password):
    length = len(password)
    print(" **YOUR ACCOUNT STATS** \n")
    print(" USER: " + user + "    PASS: ", end='')
    for x in range(0, length):
        print('*', end='')
    print("\n")
    print(" MONEY: $ " + '${:,.2f}'.format(money))
    return;

def loggedAccount():
    counter = 0
    while counter < 3:
        userC = input("What is your username: ")
        path = ("/Users/nickkazan/Desktop/" + userC)
        if os.path.isdir(path):
            passwordC = input("What is the password associated with that account: ")
            with open(path + '/login.txt', 'r') as f:
                for i, x in enumerate(f):
                    if 1 <= i < 2:
                        matcher = x
                        compare = matcher.split(":", 1)[0]
                        if (compare != passwordC){
                            counter++
                            "That was an incorrect login \n"
                        }
                        else{
                            
                        }
print("\n \n \n")
print("Welcome to World Bank\n")
flag = True
money = 0.0
while flag == True:
    option = input("What brings you here today? (1 = New Account, 2 = Logging In, 3 = Quit)\n")
    if (option > "3" or option < "1"):
        print("That's not an option\n")
    if (option == "1"):
        createAccount(money)
    if (option == "2"):
        loggedAccount()
    if (option == "3"):
        exit()
