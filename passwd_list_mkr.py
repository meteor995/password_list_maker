def three_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a3 = ""
    a2 = ""
    a1 = ""
    for a3 in pl:
        for a2 in pl:
            for a1 in pl:
                passwd = a3 + a2 + a1 + "\n"
                print(passwd)
                file.write(passwd)

def four_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a4 = ""
    a3 = ""
    a2 = ""
    a1 = ""
    for a4 in pl:
        for a3 in pl:
            for a2 in pl:
                for a1 in pl:
                    passwd = a4 + a3 + a2 + a1 + "\n"
                    print(passwd)
                    file.write(passwd)

def five_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a5 = ""
    a4 = ""
    a3 = ""
    a2 = ""
    a1 = ""
    for a5 in pl:
        for a4 in pl:
            for a3 in pl:
                for a2 in pl:
                    for a1 in pl:
                        passwd = a5 + a4 + a3 + a2 + a1 + "\n"
                        print(passwd)
                        file.write(passwd)

def six_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a6 = ""
    a5 = ""
    a4 = ""
    a3 = ""
    a2 = ""
    a1 = ""
    for a6 in pl:
        for a5 in pl:
            for a4 in pl:
                for a3 in pl:
                    for a2 in pl:
                        for a1 in pl:
                            passwd = a6 + a5 + a4 + a3 + a2 + a1 + "\n"
                            print(passwd)
                            file.write(passwd)

def seven_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a7 = ""
    a6 = ""
    a5 = ""
    a4 = ""
    a3 = ""
    a2 = ""
    a1 = ""
    for a7 in pl:
        for a6 in pl:
            for a5 in pl:
                for a4 in pl:
                    for a3 in pl:
                        for a2 in pl:
                            for a1 in pl:
                                passwd = a7 + a6 + a5 + a4 + a3 + a2 + a1 + "\n"
                                print(passwd)
                                file.write(passwd)

def eight_digit():
    inp = input("enter all your character(ex: 0 to 9): ")
    inp_list = (inp)
    pl = list(inp_list)
    pl.sort()
    inp_file_addr = input("""\nyou should enter the file address with name and format
    for example in
    linux: /home/username/Documents/password_list.txt
    windows: C:\\User\\username\\Desktop\\password_list.txt
    enter the adderss: """)
    file_addr = inp_file_addr
    file = open(file_addr, "w")
    a8 = ""
    a7 = ""
    a6 = ""
    a5 = ""
    a4 = ""
    a3 = ""
    a2 = ""
    a1 = ""
    for a8 in pl:
        for a7 in pl:
            for a6 in pl:
                for a5 in pl:
                    for a4 in pl:
                        for a3 in pl:
                            for a2 in pl:
                                for a1 in pl:
                                    passwd = a8 + a7 + a6 + a5 + a4 + a3 + a2 + a1 + "\n"
                                    print(passwd)
                                    file.write(passwd)
print("""
PASSWORD LIST MAKER - CREATED BY shahab (meteor)

this is a simple project for my CV
but actually can be useful for old style password cracking""")
is_up = 1
while is_up == 1:
    print("""
    1) 3 digit
    2) 4 digit
    3) 5 digit
    4) 6 digit
    5) 7 digit
    6) 8 digit
    7) exit
    """)
    inp = input("enter your option (from 1 to 7): ")
    if inp == "1":
        three_digit()
    elif inp == "2":
        four_digit()
    elif inp == "3":
        five_digit()
    elif inp == "4":
        six_digit()
    elif inp == "5":
        seven_digit()
    elif inp == "6":
        eight_digit()
    elif inp == "7":
        is_up = 0
    else:
        print("\ncommand not found! try from 1 to 7")
