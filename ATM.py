import os
import sys
from os import system                                                                   # 412 Lines
from time import sleep

def run():
    atm = input("Would you like to run the setup script now?\n> ")
        
    if atm == "y" or atm == "Y" or atm == "YES" or atm == "Yes" or atm == "yes":
        os.system("python3 setup.py || python setup.py")
        cls()
        exit()
            
    elif atm == "n" or atm == "N" or atm == "NO" or atm == "No" or atm == "no":
            cls()
            a = input("Press Enter to close this script.\n")

    elif len(atm) <= 0 or atm != atm.isalpha() or atm != "yes" or atm != "YES" or atm != "Yes" or atm != "y" or atm != "Y" or atm != "no" or atm != "NO" or atm != "No" or atm != "n" or atm != "N":
        cls()
        print("Please enter either 'Yes' or 'No'.")
        sleep(3)
        run()
        
def cls():
        if sys.platform.startswith("win32" or "win64" or "win86"):
            os.system("cls")
        else:
            os.system("clear")

try:
    
    
    from asset.database import id_list, id_name, id_balance
    
    if sys.platform.startswith("win32" or "win64" or "win86"):
        os.system("cls")
    else:
        os.system("clear")

    try:
        from pyfiglet import Figlet
        f = Figlet(font="big")
        print(f.renderText("Merryweather ATM"))
    except ImportError or ModuleNotFoundError:
        pass


    ast = []

    withdraw_count = []

    username = []

    def empty_response():
        cls()
        print("Please answer the respective question.")
        sleep(3)


    misc_index = []


    


    # Function for homescreen.
    def home():
        print("\nWelcome to Merryweather Automated Machine Services.")
        print("")
        try:
            idd = int(input("Please enter your personal identification number.\n> "))
        except ValueError:
            cls()
            print("Please enter only numbers.")
            sleep(3)
            cls()
            home()
        
        from asset.database import id_list, id_name, id_balance
        if idd in id_list:
            indexx = id_list.index(idd)
            misc_index.append(indexx)
            ast.append(indexx)
            cls()
            print("Hello {}," .format(id_name[indexx]))
            username.append(id_name[indexx])
            service()
        elif not idd in id_list:
            cls()
            print("You entered an incorrect PIN. Please try again.")
            sleep(3)
            cls()
            home()


            
    def service():
        print("What service would you like to use today?\n")
        print("1. Withdrawl\n2. Deposit\n3. Balance enquiry\n4. Money Transfer\n5. Change PIN")
        print("")
        try:
            serv = int(input("Enter either '1', '2', '3', '4', '5' or Enter '0' to exit.\n> "))
        except ValueError:
            cls()
            print("Please enter only numbers.")
            sleep(3)
            cls()
            service()
            
        if serv == 1:
            withdraw()
            
        elif serv == 2:
            deposit()
            
        elif serv == 3:
            balance()

        elif serv == 4:
            money_transfer()

        elif serv == 5:
            id_change()

        elif serv == 0:
            ex()


    def ex():
        cls()
        ab = input("Thank you for using Merryweather ATM services. Press Enter to exit this script.\n")
        if len(ab) >= 0:
            exit()
        
    def emp():
        print("Please enter the respective question.")


    def other():
        cls()
        ott = input("Do you want to use any other service?\n\nEnter either 'Yes' or 'No.'\n> ")
        if ott == "Yes" or ott == "yes" or ott == "YES" or ott == "Y" or ott == "y":
            cls()
            service()
        elif ott == "No" or ott == "no" or ott == "NO" or ott == "N" or ott == "n":
            ex()
        elif ott != ott.isalpha():
            cls()
            print("Please enter only alphabets.")
            sleep(3)
            other()
        elif ott != "Yes" or ott != "YES" or ott != "yes" or ott != "no" or ott != "No" or ott != "NO":
            cls()
            print("Please enter either 'Yes' or 'No'.")
            sleep(3)
            other()
        elif len(ott) == 0:
            cls()
            emp()
            other()
            


    ac_bal = []

            
    def balance():
        if len(money_transfer_count) > 0:
            cls()
            print("Session Timed out, Please login again.")
            sleep(3)
            os.system("python3 ATM.py || python ATM.py")
            cls()
            exit()
        else:
            from asset.database import id_balance
            bal = id_balance[misc_index[0]]
            cls()
            print("Your available balance is ${}." .format(bal))
            sleep(3)
            cls()
            other()
        
    def withdraw():
        cls()
        bal = id_balance[misc_index[0]]
        ac_bal.append(bal)
        try:
            if len(withdraw_count) > 0:
                cls()
                print("Session Timed out, Please login again.")
                sleep(3)
                os.system("python3 ATM.py || python ATM.py")
                cls()
                exit()
            elif len(withdraw_count) <= 0:
                amount = int(input("How much money do you want to withdraw?\n> $ "))
                if int(amount) > ac_bal[0]:
                    cls()
                    print("Transaction Failed")
                    print("")
                    print("You do not have sufficient balance in your account.")
                    sleep(3)
                    cls()
                    other()
                elif int(amount) > 0 and int(amount) <= ac_bal[0] and len(withdraw_count) <= 0:
                    up_bal = int(ac_bal[0]) - int(amount)
                    a = misc_index[0]
                    id_balance[a] = up_bal
                    print("")
                    print("Your remaining balance is ${}." .format(id_balance[misc_index[0]]))
                    abc = "asset" + str(ast[0])
                    with open("asset/{}.py".format(abc),"w") as a:
                        a.write("a{} = {}".format(ast[0], id_balance[misc_index[0]]))
                        a.close()
                        withdraw_count.append(1)
                        sleep(3)
                        other()
                elif len(amount) == 0:
                    cls()
                    emp()
                    withdraw()
                
        except ValueError:
            cls()
            print("Please enter only numbers.")
            sleep(3)
            cls()
            withdraw()
        
        
    def deposit():
        cls()
        bal = id_balance[misc_index[0]]
        ac_bal.append(bal)
        try:
            if len(withdraw_count) > 0:
                cls()
                print("Session Timed out, Please login again.")
                sleep(3)
                os.system("python3 ATM.py || python ATM.py")
                cls()
                exit()
            check = int(input("How much money do you want to deposit?\n\n> $ "))
            if check <= 10000:
                up_bal = int(ac_bal[0]) + int(check)
                a = misc_index[0]
                id_balance[a] = up_bal
                print("")
                print("Your updated balance is ${}." .format(id_balance[misc_index[0]]))
                abc = "asset" + str(ast[0])
                with open("asset/{}.py".format(abc),"w") as b:
                    
                    b.write("a{} = {}".format(ast[0], id_balance[misc_index[0]]))
                    b.close()
                    withdraw_count.append(1)
                    sleep(3)
                    other()
                    sleep(3)
                    cls()
                    other()
            elif check > 10000:
                cls()
                print("You can only deposit $10,000 at a time")
                sleep(3)
                deposit()
            elif len(check) == 0:
                cls()
                emp()
                deposit()
                
                
        except ValueError:
            cls()
            print("Please enter only numbers.")
            sleep(3)
            cls()
            deposit()

    misc_id = []

    def id_change():
        cls()
        inx = misc_index[0]
        try:
            check = int(input("Enter a four digit password.\n> "))
            print("")
            dcheck = int(input("Enter your password again.\n> "))
            check1 = str(check).startswith("0")
            
            if check1 == True:
                cls()
                print("Please avoid using '0' as the first digit.")
                sleep(3)
                cls()
                id_change()
            elif check == dcheck and len(str(check)) == 4 and len(str(dcheck)) ==4:
                cls()
                with open("asset/pin{}.py".format(inx),"w") as f:
                    f.write("pin{} = {}".format(inx, check))
                    misc_id.append(1)
                    print("Password successfully changed!")
                    f.close()
                    sleep(3)
                    other()
            elif check != dcheck:
                cls()
                print("Your Password doesn"t match, please try again.")
                sleep(3)
                cls()
                id_change()
            elif len(str(check)) > 4 or len(str(check)) < 4:
                cls()
                print("Please enter exactly four digits.")
                sleep(3)
                cls()
                id_change()
            else:
                cls()
                print("Please answer the respective question.")
                sleep(3)
                cls()
                id_change()
                
                
        except ValueError:
            cls()
            print("Please enter only numbers.")
            sleep(3)
            cls()
            id_change()
            

    recipient_index = []


    money_transfer_count = []



    def money_transfer():
        cls()
        inx = misc_index[0]
        cc = input("Enter the name of the recipient\n> ")
        cb = cc.title()
        if cb == str(*username):
            cls()
            print("You cannot send money to yourself.")
            sleep(3)
            other()
            
        elif cb in id_name:
            
            inx2 =  id_name.index(cb)
            try:
                print("")
                mn = int(input("How much money do you want to send to {}?\n> $ ".format(cb)))
                bal = id_balance[misc_index[0]]
                r_bal = id_balance[inx2]
                if mn <= bal and mn <= 10000 and mn != 0 and mn > 0:
                    new_bal = bal - mn
                    new_r_bal = r_bal + mn
                    with open("asset/asset{}.py".format(inx2),"w") as f:
                        f.write("a{} = {}".format(inx2, new_r_bal))
                        print("Transaction Successful.")
                        f.close()


                    with open("asset/asset{}.py".format(misc_index[0]),"w") as g:
                        g.write("a{} = {}".format(misc_index[0], new_bal))
                        print("Your available balance is ${}.".format(new_bal))
                        money_transfer_count.append(1)
                        g.close()
                        sleep(3)
                        other()
                elif mn < 0:
                    cls()
                    print("Transaction Failed!")
                    print("")
                    print("Please enter a valid amount.")
                    sleep(3)
                    other()
                elif mn == 0:
                    cls()
                    emp()
                    sleep(3)
                    cls()
                    other()
                elif mn > bal:
                    cls()
                    print("Transaction Failed!")
                    print("")
                    print("You don't have sufficient balance in your account.")
                    sleep(3)
                    other()
            except ValueError:
                cls()
                print("Please enter only numbers.")
                sleep(3)
                cls()
                money_transfer()
        elif not cb in id_name:
            cls()
            print("Transaction Failed.\n\nThe recepient name you entered doesn't match our records.")
            sleep(3)
            other()




    home()

            
except ImportError:
    print("Please run the setup file before running this script.")
    sleep(6)
    print("")
    run()
