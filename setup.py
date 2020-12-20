from time import sleep
import os
from os import system





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

def cls():
    os.system('cls')




print('Welcome to the Merryweather ATM setup wizard.\nPlease enter the following questions carefully for any wrong information may create further problems.')

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

for i in range(5):
    o_name = input('Enter the name of user {}.\n> '.format(usr))
    t_name = o_name.title()
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
usr2 = 1


for i in range(5):
    try:
        o_pin = int(input('Enter the preferred PIN for user {}.\n> '.format(usr2)))
        with open('asset/pin{}.py'.format(str(inx2)), 'w') as pn:
            pn.write('pin{} = {}'.format(inx2, o_pin))
            pn.close()
            inx2 += 1
            usr2 += 1
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
usr3 = 1

for i in range(5):
    try:
        o_bal = int(input('Enter the Balance for user {}.\n> $ '.format(usr3)))
        with open('asset/asset{}.py'.format(str(inx3)), 'w') as bl:
            bl.write('a{} = {}'.format(inx3, o_bal))
            bl.close()
            inx3 += 1
            usr3 += 1
    except ValueError:
        cls()
        print('You corrupted the data files by not being careful while entering data. Run this script again but if it doesn\'t run, reinstall the whole script')
        sleep(10)
        exit()



cls()

print('Configuration successful')
print('You can now run the ATM.py script and login with the credentials you entered.')
print('')
a = input("Press any key and hit enter to close this script.\n")








