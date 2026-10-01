import data

# this funct too check the if this cpu in the list 
cpus = data.cpus

def display():
    for cpu in cpus :
        print(f"Brand : { cpu["brand"]}")
        print(f"Name : {cpu['name']}")
        print(f"Gaming : {cpu['gaming']}")
        print(f"Programming : {cpu["programming"]}")

def check_cpu(name):

    name = name.strip().lower()
    for cpu in cpus:
        if cpu["name"].lower()==name:
            return cpu
    
    return None

def check_stockage():
    # 1/ ssd
    # 2/ hdd
    print("""enter the type of your disk

    1 - SSD
    2 - HDD
        
    """)
    types = input ("enter your choice : ")
    storage =  int(input("enter the storage : "))
    if types == "1" and storage >= 512:
        result = 1
    elif types == "1" and storage < 512 :
        result = 2
    elif types == "2":
        result = 3
    return result

def result_chek(cp,user_ram):
    if cp["gaming"] == "Great" and cp["programming"] == "Great":
        print("this  pc for gaming and programming")
    elif cp["programming"] == "Great":
        print("this pc for programming ")
    elif cp["gaming"]== "Great" and int(user_ram) == 16 :
        print("this pc for gaming but you need to upgrade your RAM. ")   
    elif cp["gaming"]== "Great":    
        print("your pc for gaming.")

def gaming_pc():
    print("the CPU : ")

    for cpu in cpus:
        if cpu["gaming"] == "Great":
            print("*"*100)
            print(f"Brand : { cpu["brand"]}")
            print(f"Name : {cpu['name']}")
            print(f"Gaming : {cpu['gaming']}")
            # print(f"Programming : {cpu["programming"]}")
    print("\n NOTE : ")
    print(" - the RAM is more then 16 GB")
    print(" - the storage you need [ SSD ] type and equal or more then [ 512 GB ] ")

def programing_pc():
    print("the CPU : ")

    for cpu in cpus:
        if cpu["programming"] == "Great":
            print("*"*100)
            print(f"Brand : { cpu["brand"]}")
            print(f"Name : {cpu['name']}")
            # print(f"Gaming : {cpu['gaming']}")
            print(f"Programming : {cpu["programming"]}") 
    print("\n NOTE : ")
    print(" - the RAM is equal or  more then 16 GB")
    print(" - the storage you need [ SSD ] type and equal or more then [ 256 GB ] ")

def both_gmaing_programing(): 
    print("the CPU : ")
    for cpu in cpus:
        if cpu["gaming"] == "Great" and cpu["programming"] == "Great":
            print("*"*100)
            print(f"Brand : { cpu["brand"]}")
            print(f"Name : {cpu['name']}")
            print(f"Gaming : {cpu['gaming']}")
            print(f"Programming : {cpu["programming"]}")
    print("\n NOTE : ")

    print(" - the RAM is more then 16 GB")
    print(" - the storage you need [ SSD ] type and equal or more then [ 512 GB ] ")

