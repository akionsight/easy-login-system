import time


def create_account():
    user = str(input("enter username:- "))
    print(f"your username would be {user} enter 'ok' below to confirm")
    conf = str(input(">>> "))
    lol = open("kachua.txt", 'a')
    if conf.lower() == 'ok':             # account creation process
        try:
            lol.write(f'{user}\n')
        finally:
            lol.close()
    else:
        conf2 = input("do you want to create an account again(ok to confirm)")
        if conf2.lower() == 'ok':
            create_account()
        else:
            print("bye")
            pass


def login():
    with open("kachua.txt") as fobj:
        text = fobj.read().strip().split()
        try:
            while True:
                try:
                    s = input("Enter your username: ")
                    if s == "":
                        continue          # thanks stackoverflow
                    if s in text:
                        print("yay,logged in")
                        break
                    raise Exception("sorry,try again")
                except Exception as e:
                    print(e)
                except KeyboardInterrupt:
                    print("keyboard interruption")
        finally:
            fobj.close()


def to_do_function():
    to_do = str(input("what do you want to do:- "))
    if to_do == 'create account':
        print("creating account please wait")
        time.sleep(0.5)
        create_account()
    elif to_do == 'login':
        print("creating login system")
        time.sleep(0.5)
        login()  # give feeling
    elif to_do == 'help':
        print('''create account:- create an account
                    login:- to login''')


to_do_function()
