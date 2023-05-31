

import random
import os



def Init():
    B=[]
    dim=int(input("\nEnter Dimension : "))
    nop=int(input("\nEnter number of players : "))
    for r in range(0,dim):
        row=[]
        for c in range(0,dim):
            row.append('-')
        B.append(row)
    winC=int(input("Enter Winning Condition : "))
    sym=[]
    pName=[]
    for i in range(0,nop):
        pName.append(input(f"Enter player{i+1}'s name : "))
        sym.append(input(f"Enter player{i+1}'s symbol : "))
    turn=random.randint(0,nop-1)
    return B,dim,nop,winC,sym,pName,turn

def printBoard(B,dim):
    os.system("cls")
    for r in range(0,dim):
        for c in range(0,dim):
            print(B[r][c],end="")
        print()

def turnMsg(name):
    print(f"{name}'s turn")

def selectPos(dim):
    pr=int(input(f"Select Row (1...{dim})"))
    pc=int(input(f"Select Column (1...{dim})"))
    pr-=1
    pc-=1
    return pr,pc

def placeMove(B,pr,pc,sym):
    B[pr][pc]=sym

def turnChange(turn,nop):
    turn=(turn+1)%nop
    return turn

def isValid(B,pr,pc):
    if(B[pr][pc]=='-'):
        return True
    else:
        return False

def horizentalChk(B,dim,r,c,winC,sym):
    if(c+winC>dim):
        return False
    count=0
    for i in range(0,winC):
        if(B[r][c+i]==sym):
            count+=1

    if(count==winC):
        return True
    else:
        return False

def verticalChk(B,dim,r,c,winC,sym):
    if(r+winC>dim):
        return False
    count=0
    for i in range(0,winC):
        if(B[r+i][c]==sym):
            count+=1

    if(count==winC):
        return True
    else:
        return False

def dignolChkL2R(B,dim,r,c,winC,sym):
    if(r+winC>dim or c+winC>dim):
        return False
    count=0
    for i in range(0,winC):
        if(B[r+i][c+i]==sym):
            count+=1

    if(count==winC):
        return True
    else:
        return False

def dignolChkR2L(B,dim,r,c,winC,sym):
    if(r+winC>dim or c-winC<0):
        return False
    count=0
    for i in range(0,winC):
        if(B[r+i][c-i]==sym):
            count+=1

    if(count==winC):
        return True
    else:
        return False

def doIWinHere(B,dim,r,c,winC,sym):
    if(horizentalChk(B,dim,r,c,winC,sym) or verticalChk(B,dim,r,c,winC,sym) or dignolChkL2R(B,dim,r,c,winC,sym) or dignolChkR2L(B,dim,r,c,winC,sym)):
        return True
    else:
        return False

def isWin(B,dim,winC,sym):
    for r in range(0,dim):
        for c in range(0,dim):
            if(doIWinHere(B,dim,r,c,winC,sym)):
                return True

    return False

def isDraw(B,dim):
    for r in range(0,dim):
        for c in range(0,dim):
            if(B[r][c]=='-'):
                return False

    return True

comp=1
hum=0

def Init2():
    B=[]
    dim=int(input("\nEnter Dimension : "))
    nop=2
    for r in range(0,dim):
        row=[]
        for c in range(0,dim):
            row.append('-')
        B.append(row)
    winC=int(input("Enter Winning Condition : "))
    pName=[]
    sym=[]
    for i in range(0,nop):
        pName.append(input(f"Enter player{i+1}'s name : "))
        sym.append(input(f"Enter player{i+1}'s symbol : "))
    turn=random.randint(0,nop-1)
    return B,dim,nop,winC,sym,pName,turn

def computerPositioning(B,dim,winC,sym):
    for wc in range(winC,2,-1):
        for r in range(0,dim):
            for c in range(0,dim):
                if(isValid(B,r,c)):
                    B[r][c]=sym[comp]
                    if(isWin(B,dim,winC,sym[comp])):
                        return r,c
                    B[r][c]='-'

    for wc in range(winC,2,-1):
        for r in range(0,dim):
            for c in range(0,dim):
                if(isValid(B,r,c)):
                    B[r][c]=sym[hum]
                    if(isWin(B,dim,winC,sym[0])):
                        placeMove(B,r,c,sym[comp])
                        return r,c
                    B[r][c]='-'


    r=random.randint(0,dim)%dim
    c=random.randint(0,dim)%dim

    while True:
        if(isValid(B,r,c)):
            placeMove(B,r,c,sym[comp])
            return r,c
        else:
            r=random.randit(0,dim)%dim
            c=random.randit(0,dim)%dim







print("\nHow you want to play")
choice=int(input("1- Human vs Human\n2- Human vs Computer\n "))

if(choice==1):
    GameOver=False
    B,dim,nop,winC,sym,pName,turn=Init()
    printBoard(B,dim)
    while(GameOver==False):
        turnMsg(pName[turn])
        pr,pc=selectPos(dim)
        while True:
            if(isValid(B,pr,pc)):
                placeMove(B,pr,pc,sym[turn])
                break
            else:
                print("\nInvalid Cordinates\nEnter Again\n")
                pr,pc=selectPos(dim)
        printBoard(B,dim)
        if(isWin(B,dim,winC,sym[turn])):
            GameOver=True
            print(f"{pName[turn]} has won the game")
            break

        if(isDraw(B,dim)):
            GameOver=True
            print("Game is a tie")
            break

        turn=turnChange(turn,nop)

else:
    GameOver=False
    B,dim,nop,winC,sym,pName,turn=Init2()
    printBoard(B,dim)
    while(True):
        turnMsg(pName[turn])
        if(turn==0):
            pr,pc=selectPos(dim)
            while True:
                if(isValid(B,pr,pc)):
                    placeMove(B,pr,pc,sym[turn])
                    break
                else:
                    print("\nInvalid Cordinates\nEnter Again\n")
                    pr,pc=selectPos(dim)
        else:
            pr,pc=computerPositioning(B,dim,winC,sym)
        printBoard(B,dim)
        if(isWin(B,dim,winC,sym[turn])):
            GameOver=True
            print(f"{pName[turn]} has won the game")
            break

        if(isDraw(B,dim)):
            GameOver=True
            print("Game is a tie")
            break

        turn=turnChange(turn,nop)







