try:
  import os
  import threading
  import subprocess
  import keyboard
  import time
  from colorama import Fore, Style,init
  from pathlib import Path
  from os import path
except ModuleNotFoundError:
        subprocess.call("pip3 install keyboard", shell=True)
        subprocess.call("pip3 install colorama", shell=True)
        

banner = """



░█████╗░███╗░░██╗░█████╗░███╗░░██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗
██╔══██╗████╗░██║██╔══██╗████╗░██║  ██╔════╝██╔══██╗██╔══██╗████╗░████║
███████║██╔██╗██║██║░░██║██╔██╗██║  ╚█████╗░██████╔╝███████║██╔████╔██║
██╔══██║██║╚████║██║░░██║██║╚████║  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██║░░██║██║░╚███║╚█████╔╝██║░╚███║  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  
                                                     

 
                          AUTHOR       :   swagkarna

                          CONTACT ME   :   github.com/swagkarna

"""
print(Style.BRIGHT+Fore.RED+banner+Fore.RESET)




      
class spam :
    def checkfile(self) :
        if path.exists('spam.txt'):
           ask = input(str("File already Present\nDo you want to over write(yes or no) : "))
           if "yes" in ask :
                self.write()      
                self.spams()
           else :
             self.spams()
        else :
         self.write()
               
      
    def write(self) :
      f = open('spam.txt', 'w')
      s = int(input("Enter the number of line you want to write : "))
      for i in range(s) :
        n =input(str("Enter the characters you want to write : "))
         
        f.write(n)
        f.write("\n")
    
       

    def spams(self):
        print("Now Place the cursor where you want to spam")
        time.sleep(6)
        while True:
        
           file=open("spam.txt", 'r')
           x=file.read()
           keyboard.write(x)
           time.sleep(3)
           keyboard.send("enter")
    def main(self) :
           self.checkfile()
           self.spams()           
x = spam()  
x.main()       





















