import functions
from data import cpus

#  if We don't want to use funts.name_def
    # We use from functs import *
# cpus = data.cpus

print("welcome to cumptech..")

goal = print("""
what do you want :
chose number :

1 : if you watn to cheack the configuration.     
2 : if you  want to search (want to buy a pc ).

""")
goal = input("enter your choice : ")
# this is for the x=checking 
if goal == "1":

    user_cpu = input("enter your cpu : ")
    user_ram = input("enter your RAM : ")
    
   
    # check if this cpu in the list or not 
    # for give the user all information about it
    cp = functions.check_cpu(user_cpu)
    
    print("this is the result of your CPU : ")
    if cp:
        print(f"Brand : {cp["brand"]}")
        print(f"Name : {cp['name']}")
        print(f"Gaming : {cp['gaming']}")
        print(f"Programming : {cp["programming"]}")
   
        print("but you must be check the other thing of your pc.")
        input("press enter to see what can do with your pc! ")
        # call the check storage , ask the user then  return 1 ,2 or 3
        result = functions.check_stockage()
        input ("press enter to se what your laptop can do...!")
        # this is for check 
        if int(user_ram) >= 16 and result == 1:
            functions.result_chek(cp,user_ram)

        elif int(user_ram) >= 16 and result == 2:
            functions.result_chek(cp,user_ram)

        elif int(user_ram) >= result == 3:
            print("whatever you have cpu,you have HHD storage and its to slow for prossesing and starting so you can do any best thing like programing and gaming.")

        elif int(user_ram) < 16 :
            print("you need to upgrade your RAM becaause it's nessesery to do anything greatful.")
    else: 
        print("this cpu is not in the list please check the name of your cpu and try again.")
# for the searching :
elif goal == "2":
    print("""enter what is the type of laptop you need (Gaming , Programming or both) : 
    1 - Programing
    2 - Gaming
    3 - Gaming and Programming
    """)
    laptop = input("enter your choice : ")
    if laptop == "1":
        functions.programing_pc()
    elif laptop == "2":
        functions.gaming_pc()
    elif laptop == "3":
        functions.both_gmaing_programing()

else : 
    print("your choice not in the list try agin..")
    