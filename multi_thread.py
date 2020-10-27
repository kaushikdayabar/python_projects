import threading
import datetime
import time
from playsound import playsound

def check_alarm(t):
    n=len(t)
    if 0<=t[0]<=24  and 0<=t[1]<=59 and 0<=t[2]<=59:
        return True
    else:
        raise ValueError("inappropriate time")
   
        
def convert_into_seconds(t):
    return t[0]*3600+t[1]*60+t[2]

def buzz(t,q):
    time.sleep(t)

    print(q)

    playsound("dra.mp3")


l=[]


def alarm():
    s=input("enter the time in the format HH:MM:SS")
    q=input("label")
   
    s=s.split(":")

    s=[int(x) for x in s]  #list comprehension

    n=3-len(s)
    
    for i in range(n):
        s.append(0)

    check_alarm(s)



    s=convert_into_seconds(s)

    

    #to get current time

    t=str(datetime.datetime.now())[11:].split(":")

    print(t)
    t[2]=float(t[2])

    t=[int(x) for x in t]

    print(t)

    t=convert_into_seconds(t)

    
    #calculate difference

    c=s-t

    print(c)
    if c<0:
        c+=86400
        
    thread=threading.Thread(target=buzz,name=q,args=(c,q,))
    l.append(thread)
    thread.start()

def display():
    for i in range(len(l)):
        print(l[i].getName())
        
while(1):
    try:
        choice=int(input("enter the operation"))

        if choice==1:
            alarm()
        elif choice==2:
            display()
        else:
            exit()
                
        
    except ValueError as e:
            print(e)
