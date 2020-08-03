try:
  import threading
  import subprocess
  import keyboard
  import time
  from colorama import Fore, Style,init
except ModuleNotFoundError:
        subprocess.call("pip3 install keyboard", shell=True)
        subprocess.call("pip3 install colorama", shell=True)
        

banner = """


 #####  ######     #    #     # ######  ####### ####### 
 #     # #     #   # #   ##   ## #     # #     #    #    
 #       #     #  #   #  # # # # #     # #     #    #    
  #####  ######  #     # #  #  # ######  #     #    #    
       # #       ####### #     # #     # #     #    #    
 #     # #       #     # #     # #     # #     #    #    
  #####  #       #     # #     # ######  #######    #    
                                                     

 
                          AUTHOR       :   swagkarna

                          CONTACT ME   :   github.com/swagkarna

"""
print(Style.BRIGHT+Fore.RED+banner+Fore.RESET)

time.sleep(5)

      

      
def spam():
    while True:
       time.sleep(1)
       file=open("spam.txt", 'r')
       x=file.read()
       keyboard.write(x)
       time.sleep(2)
       keyboard.send("enter")
                     
spam()         






