import os
import maskpass
def signin():
    user_mail = input("Enter your E-mail : ")
    try:
        with open ("user-detail.txt", "r") as read:
            print("file is open")
    except :
        open("user-detail.txt", "x")
        print("file is creted")
    with open("user-detail.txt", "r") as file_read:
        user_detail = file_read.read()
        singal_user = user_detail.split("\n")
        users = False
        for user in singal_user:
            if user == user_mail :
                print("Welcome Back Sir")
                users = True
        if users == False :
            print("Welcome in our family as member sir")
            with open ("user-detail.txt", "a") as file_write:
                file_write.write(f"\n{user_mail}")
 
 
def user_order():
    print("Meanu List")
    meanu_list = {"Espresso: 300","Latte: 500","Caffè mocha: 600","Cortado: 450",
                  "Flat white: 300","Cappuccino: 900"}
    def meau():
        for item in meanu_list:
            print(item)
    lop = True
    prevoius_bill = 0
    while lop :
        meau()
        order_item = input("Enter what want to  order : ")
        amount = input("enter the number of cups :")
        for item in meanu_list:
            item_detail = item.split(":")
            if item_detail[0] == order_item:
                new_bill = int(amount)*int(item_detail[1]) + int(prevoius_bill )
                print(f"Your bill is {new_bill}rs")
                prevoius_bill = new_bill
        condition = input("you want to order more items: ")
        if condition.lower() == 'yes' or condition.lower() == 'y':
            lop =   True
        else:
            lop = False
        

signin()
user_order()

