from BankAccount import *

oAccount01 = BankAccount(630910359, 10, 5000, "Woraphob Sinbunyama", "qwerty")
oAccount02 = BankAccount(630910000, 10, 1000, "Zack Fair", "final")

oAccount01._acc_info("we")          #test conditions
oAccount01._acc_info("qwerty")      #test conditions
oAccount01.calInterest()            
oAccount01.deposit(500,"as")        #test conditions
oAccount01.deposit(-500,"qwerty")   #test conditions
oAccount01.deposit(500,"qwerty")    #test conditions
oAccount01.withdraw(5000,"as")      #test conditions
oAccount01.withdraw(-1000,"qwerty") #test conditions
oAccount01.withdraw(6000,"qwerty")  #test conditions
oAccount01.withdraw(1500,"qwerty")  #test conditions
oAccount01._acc_info("qwerty")
oAccount01.transfer(oAccount02, 5000, "qwe")    #test conditions
oAccount01.transfer(oAccount02, 5000, "qwerty") #test conditions
oAccount01.transfer(oAccount02, 4000, "qwerty") #test conditions
oAccount02._acc_info("final")
oAccount01._acc_info("qwerty")
oAccount02.transfer(oAccount01, -3500, "final") #test conditions
oAccount02.transfer(oAccount01, 252.54, "final") #test conditions
oAccount02._acc_info("final")
oAccount01._acc_info("qwerty")


