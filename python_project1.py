c=int(input("enter the operation:"
            "\n1.block website"
            "\n2.display blocked websites"
            "\n3.unblock website\n"))




if  c==1:
    with open("/etc/hosts","a") as f:
        s=input("enter the website to be blocked")
        f.seek(0,2)
        f.write("\n127.0.0.1 "+s)

elif c==2:
    with open("/etc/hosts","r") as f:
        f.seek(0)
        s=f.read()[240:]
        if s.strip()=="":
            print("none")
        else:
            print(s.strip())
elif c==3:
    s="127.0.0.1 "+input("enter the website to unblock")
    output=""
    with open("/etc/hosts","r") as f:
        for line in f:
            if line.strip()!=s.strip():
                output+=line
                
    with open("/etc/hosts","w") as f:
        f.writelines(output)     
         
         
    
        
        
    


