import random
import re

while(1):
    print("Rock,Paper and Scissor")
    user=input("choose your weapon R->Rock,P->Paper and S->Scissor\n")
    d={"r":"Rock","p":"Paper","s":"Scissor"}
    if not re.match("[SRPsrp]",user):
        print("Invalid Input,try again")
        continue
    opponent=random.choice(["r","p","s"])

    print("You chose "+d[user.lower()]+"\nI chose "+d[opponent]+"\n")
    
    if user.lower()==opponent:
        print("It's a tie")
    elif (user.lower()=="r" and opponent=="p") or (user.lower()=="p" and opponent=="s"):
        print(d[opponent]+" beats "+d[user.lower()]+" hence I win.")
    else:
        print(d[user.lower()]+" beats "+d[opponent]+" hence you win.")         

    c=input("Do you want to play again?(y/n)")

    if c=="n":
        break    
        
    
    
