from time import sleep
import os
import sys                                                                      # 376 Lines
from os import system


def cls():
    if sys.platform.startswith('win32' or 'win64' or 'win86'):
        os.system('cls')
    else:
        os.system('clear')
try:
	try:
		os.system('pip3 install -r requirements.txt || pip install -r requirements.txt')
	except Exception:
		pass
	cls()

	def banner():
		    try:
		        from pyfiglet import Figlet
		        f = Figlet(font='big')
		        print(f.renderText("""Merryweather\nATM services"""))
		    except ImportError or ModuleNotFoundError:
		        pass

	try:
		import re
		import colorama
		class IO(object):
		    _ANSI_CSI_RE = re.compile('\001?\033\\[((?:\\d|;)*)([a-zA-Z])\002?') 

		    Back = colorama.Back
		    Fore = colorama.Fore
		    Style = colorama.Style
		def c_banner():
		    MAIN_BANNER = r"""{}

	██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
	██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
	██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
	██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
	╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
	 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
		                                                                                                                                                                
		{}         
		                                                                                                   
		""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)
		    print(MAIN_BANNER)
		

		c_banner()
	except ImportError or ModuleNotFoundError:
		if sys.platform.startswith("win32" or "win64" or "win86"):
		    banner()
		else:
		    print('Consider installing Colorama in your distro (sudo apt-get install python3-colorama)')
		    banner()


		








	try:
		from asset.asset0 import a0
	except ModuleNotFoundError or ImportError:      #balance
		pass    


	try:
		from asset.asset1 import a1
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset2 import a2
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset3 import a3
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset4 import a4
	except ModuleNotFoundError or ImportError:              #balance
		pass



	try:
		from asset.asset5 import a5
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset6 import a6
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset7 import a7
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset8 import a8
	except ModuleNotFoundError or ImportError:
		pass



	try:
		from asset.asset9 import a9
	except ModuleNotFoundError or ImportError:      #balance
		pass







	try:
		from asset.pin0 import pin0                 # pin
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin1 import pin1
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin2 import pin2
	except ModuleNotFoundError or ImportError:
		pass              
	try:
		from asset.pin3 import pin3
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin4 import pin4
	except ModuleNotFoundError or ImportError:              #pin
		pass
	try:
		from asset.pin5 import pin5
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin6 import pin6
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin7 import pin7
	except ModuleNotFoundError or ImportError:
		pass              
	try:
		from asset.pin8 import pin8
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.pin9 import pin9
	except ModuleNotFoundError or ImportError:     #pin
		pass







	try:    
		from asset.name0 import name0               #name
	except ModuleNotFoundError or ImportError:
		pass

	try:
		from asset.name1 import name1
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.name2 import name2
	except ModuleNotFoundError or ImportError:
		pass              
	try:
		from asset.name3 import name3
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.name4 import name4
	except ModuleNotFoundError or ImportError:                  #name
		pass
	try:
		from asset.name5 import name5
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.name6 import name6
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.name7 import name7
	except ModuleNotFoundError or ImportError:
		pass              
	try:
		from asset.name8 import name8
	except ModuleNotFoundError or ImportError:
		pass
	try:
		from asset.name9 import name9
	except ModuleNotFoundError or ImportError:
		pass                                        #name




	def users():
		cls()
		try:
		    val = int(input('How many users do you want to add in this facility?\n\n> '))
		    val1 = str(val).startswith('0')
		    if val <= 10 and val != 0:
		        global f
		        f = int(val)
		        cls()
		        name()
		    elif val > 10:
		        cls()
		        print('You can only add a maximum of ten users.')
		        sleep(3)
		        users()
		    elif val1 == True:
		        cls()
		        print('Are you kidding me? Why the hell are you using this script then???')
		        sleep(5)
		        print('')
		        print('Don\'t be a jerk this time.')
		        sleep(5)
		        users()
		    
		except ValueError:
		    cls()
		    print('Please enter only integers')
		    sleep(3)
		    users()
		    
		
	def welcome():
		print('Welcome to the Merryweather ATM setup wizard.\n\nPlease enter the following questions carefully for any wrong information may create further problems.')

		sleep(5)
		print('')

		print('Gathering information', end = '')
		
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.')

		sleep(2)
		print('')

		print('Compiling data', end = '')
		
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.')

		print('')
		sleep(2)
		print('Processing', end = '')
		
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.', end = '')
		sleep(0.5)
		print('.')
		
		sleep(2)
		cls()
		users()

	names = []

	def name():
		inx = 0
		usr = 1
		
		for i in range(f):
		    o_name = input('Enter the name of user {}.\n> '.format(usr))
		    print('')
		    t_name = o_name.title()
		    names.append(t_name)
		    with open('asset/name{}.py'.format(str(inx)), 'w') as nn:
		        nn.write('name{} = \'{}\''.format(inx, t_name))
		        nn.close()
		        inx += 1
		        usr += 1
		        cls()
		print('Saving Names in Database...')
		sleep(3)
		cls()
		pin()



	def pin():
		inx2 = 0
		for i in range(f):
		    try:
		        o_pin = int(input('Enter the preferred PIN for {}.\n> '.format(names[inx2])))
		        print('')
		        o_pin1 = str(o_pin).startswith('0')
		        if o_pin1 == True:
		            cls()
		            print("Please avoid using \'0\' as the first digit.")
		            sleep(3)
		            cls()
		            pin()
		        else:
		            cls()
		            with open('asset/pin{}.py'.format(str(inx2)), 'w') as pn:
		                pn.write('pin{} = {}'.format(inx2, o_pin))
		                pn.close()
		                inx2 += 1
		    except ValueError:
		        cls()
		        print('Please enter only numbers.')
		        sleep(3)
		        pin()
		print('Saving PINs in Database...')
		sleep(3)
		cls()
		bal()
		     






	def bal():
		inx3 = 0
		for i in range(f):
		    try:
		        o_bal = int(input('Enter the Balance for {}.\n> $ '.format(names[inx3])))
		        print('')
		        with open('asset/asset{}.py'.format(str(inx3)), 'w') as bl:
		            bl.write('a{} = {}'.format(inx3, o_bal))
		            bl.close()
		            inx3 += 1
		            cls()
		        
		    except ValueError:
		        cls()
		        print('Please enter only numbers.')
		        sleep(3)
		        bal()
		done()



	def done():
		print('Configuration successful!')
		print('')
		print('You can now run the ATM.py script and login with the credentials you entered.')
		sleep(8)
		run()

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
except PermissionError:
	cls()
	print('It has been detected that you dont have the permission to write files in this directory.\nIf you\'re using this script on a Linux distribution, root the script as root.\nIf you\'re on Windows, check that the files are not set to \"read only\".\nIf it still doesn\'t work then you doesn\'t have the right privileges to execute this script and make changes. Most probably your administration has blocked this feature.')
welcome()
