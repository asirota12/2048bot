# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:12:07 2016

@author: Alexander Sirota
"""
import os
import numpy as np

class Board:
    
    # Constructor
    def __init__(self):
        self.state =np.zeros((4,4))
        self.numZero=16
        self.changed=1
        self.stuck=np.zeros(4)
        
    # next turn!
    def addTwo(self):
    
        x=np.random.randint(0,4)
        y=np.random.randint(0,4)
        
        while self.state[x,y]:
            x=np.random.randint(0,4)
            y=np.random.randint(0,4)
        self.changed=1
        self.state[x,y]=2
    
    
    #some tranformation helpers
        
    def flipy(self):
        x=np.zeros((4,4))
        for i in range(0,4):
            for j in range(0,4):
                x[i,j]=self.state[i,3-j]
        self.state=x
        
    def rot(self):
        x=np.zeros((4,4))
        for i in range(0,4):
            for j in range(0,4):
                x[i,j]=self.state[j,3-i]
        self.state=x
        
    def unrot(self):
        x=np.zeros((4,4))
        for i in range(0,4):
            for j in range(0,4):
                x[i,j]=self.state[3-j,i]
        self.state=x

    # the main directions
        
    def left(self):
        self.flipy()
        self.right()
        self.flipy()
    
    def down(self):
        self.rot()
        self.right()
        self.unrot()
        
    def up(self):
        self.unrot()
        self.right()
        self.rot()

    # main swipe functionality
    def right(self):
        self.changed=0
        for row in self.state:
          #  print(row)
            
            while row[3]==0:
                if row[0]==row[1]==row[2]==row[3]==0:
                    break
                row[3]=row[2]
                row[2]=row[1]
                row[1]=row[0]
                row[0]=0  
                self.changed=1 
            while row[2]==0:
                if row[0]==row[1]==row[2]==0:
                    break
                row[2]=row[1]
                row[1]=row[0]
                row[0]=0  
                self.changed=1
            while row[1]==0:
                if row[0]==row[1]==0:
                    break
                row[1]=row[0]
                row[0]=0  
                self.changed=1 
            if row[3]==row[2]!=0:
                row[3]=2*row[2]
                row[2]=row[1]
                row[1]=row[0]
                row[0]=0 
                self.changed=1 
            elif row[2]==row[1]!=0:
                row[2]=2*row[1]
                row[1]=row[0]
                row[0]=0 
                self.changed=1 
            elif row[1]==row[0]!=0:
                row[1]=2*row[0]
                row[0]=0 
                self.changed=1 
        if(self.changed==0):
            print("can't move!")
        else:
            b.stuck=np.zeros(4)

#start the board
b = Board()

# start the game   
b.addTwo()
print(b.state)



while True:
    x = raw_input("Enter an adsw key")
    if x=="a":
        b.left()
        if b.changed==0:
            b.stuck[0]=1
    elif x=="s":
        b.down()
        if b.changed==0:
            b.stuck[1]=1
    elif x=="w":
        b.up()
        if b.changed==0:
            b.stuck[2]=1
    elif x=="d":
        b.right()
        if b.changed==0:
            b.stuck[3]=1
    else:
        print("one of the keys!!!!!!")
    if b.changed==1:
        b.addTwo()
        os.system('cls')  # for Windows
        print(b.state)
    if (np.array_equal(b.stuck,np.ones(4))):
        print("score of!")
        os.system('cls')  # for Windows
        print(np.amax(b.state))
        break


