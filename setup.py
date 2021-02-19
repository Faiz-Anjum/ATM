from time import sleep
import os
import sys
from os import system


def cls():
    if sys.platform.startswith('win32' or 'win64' or 'win86'):
        os.system('cls')
    else:
        os.system('clear')

try:
    os.system('pip3 install -r requirements.txt || pip install -r requirements.txt')
except RuntimeError:
    pass
cls()

try:
    from pyfiglet import Figlet
    f = Figlet(font='big')
    print(f.renderText('Welcome'))
except ImportError or ModuleNotFoundError:
    pass




from asset.asset0 import a0
from asset.asset1 import a1
from asset.asset2 import a2             # This is for balance
from asset.asset3 import a3
from asset.asset4 import a4

from asset.pin0 import pin0
from asset.pin1 import pin1
from asset.pin2 import pin2              # This is for pins
from asset.pin3 import pin3
from asset.pin4 import pin4



from asset.name0 import name0
from asset.name1 import name1
from asset.name2 import name2              # This is for names
from asset.name3 import name3
from asset.name4 import name4



print('Welcome to the Merryweather ATM setup wizard.\n\nPlease enter the following questions carefully for any wrong information may create further problems.')

sleep(5)
print('')

print('Gathering information')

sleep(3)
print('')

print('Compiling data')

print('')
sleep(3)
print('Processing')
sleep(3)
cls()

inx = 0
usr = 1
names = []
for i in range(5):
    o_name = input('Enter the name of user {}.\n> '.format(usr))
    print('')
    t_name = o_name.title()
    names.append(t_name)
    with open('asset/name{}.py'.format(str(inx)), 'w') as nn:
        nn.write('name{} = \'{}\''.format(inx, t_name))
        nn.close()
        inx += 1
        usr += 1
print('')
print('Saving Names in Database')
sleep(3)
cls()


inx2 = 0



for i in range(5):
    try:
        o_pin = int(input('Enter the preferred PIN for {}.\n> '.format(names[inx2])))
        print('')
        with open('asset/pin{}.py'.format(str(inx2)), 'w') as pn:
            pn.write('pin{} = {}'.format(inx2, o_pin))
            pn.close()
            inx2 += 1
            
    except ValueError:
        cls()
        print('You corrupted the data files by not being careful while entering data. Run this script again but if it doesn\'t run, reinstall the whole script')
        sleep(10)
        exit()

print('')
print('Saving PINs in Database')
sleep(3)
cls()


inx3 = 0


for i in range(5):
    try:
        o_bal = int(input('Enter the Balance for {}.\n> $ '.format(names[inx3])))
        print('')
        with open('asset/asset{}.py'.format(str(inx3)), 'w') as bl:
            bl.write('a{} = {}'.format(inx3, o_bal))
            bl.close()
            inx3 += 1
            
    except ValueError:
        cls()
        print('You corrupted the data files by not being careful while entering data. Run this script again but if it doesn\'t run, reinstall the whole script')
        sleep(10)
        exit()



cls()

print('Configuration successful')
print('')
print('You can now run the ATM.py script and login with the credentials you entered.')
sleep(8)
def run():
    cls()
    atm = input('Would you like to run the ATM script now?\n> ')
    
    if atm == 'y' or atm == 'Y' or atm == 'YES' or atm == 'Yes' or atm == 'yes':
        os.system('python3 ATM.py || python ATM.py')
        cls()
        exit()
        
    elif atm == 'n' or atm == 'N' or atm == 'NO' or atm == 'No' or atm == 'no':
        cls()
        a = input("Press Enter to close this script.\n")

    elif len(atm) <= 0 or atm != atm.isalpha() or atm != 'yes' or atm != 'YES' or atm != 'Yes' or atm != 'y' or atm != 'Y' or atm != 'no' or atm != 'NO' or atm != 'No' or atm != 'n' or atm != 'N':
        cls()
        print('Please enter either \'Yes\' or \'No\'.')
        sleep(3)
        run()
    
run()









