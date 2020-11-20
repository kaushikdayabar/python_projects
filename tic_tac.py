print("TIC TAC TOE")
no_of_moves=0
l=[0,1,2,3,4,5,6,7,8]  #board

winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))


def display():
    for i in range(3):
        end=" | "
        for j in range(3):
            if j%3==2:
                end="\n---------\n"
            if l[3*i+j] not in ["X","O"]:
                print(" ",end=end)
            else:    
                print(l[3*i+j],end=end)
        

        
def insertion(c):
    n=int(input("enter the position for {}".format(c)))

    if 0<n<10 and l[n-1]==n-1:
        l[n-1]=c
        global no_of_moves
        no_of_moves=no_of_moves+1
    else:
        print("invalid,try again")
        insertion(c)
        return
  


def get_pos(c):
    r=[] #to store player's position
    for i in range(9):
        if l[i]==c:
            r.append(i)
    return r            
    
def has_won(c):
    r=get_pos(c)
    
    for j in winners:
        if (j[0] in r) and (j[1] in r) and (j[2] in r):
            win=1
            break
    else:
        win=0
    return win    
            
            
def play():
    for i in range(5):
        for j in ["O","X"]:
            display()
            insertion(j)
            if has_won(j):
                display()
                print("Congratulations,you have won {}".format(j))
                return
            elif no_of_moves==9:
                print("tie game")
                return
            

play()

    
            
