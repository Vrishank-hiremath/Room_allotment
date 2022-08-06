#
# Seat allotment during examination/meetings

# importing modules
from tkinter import *
import math

#creating empty lists and other variables that ll be used in the program later
li=[]
roomwise=[]
count=0
loc=0
seatcount=0
result=[]

def reading(f):          # reading the ID / Roll no. from the file
    global li
    for i in f.readlines():
        a=i.splitlines()
        li.append(a[0])
    li=tuple(li)         #Storing all values in a tuple
    f.close()

def allot(seats):        #Allocation depending on number of seats avalible in each room
    global loc
    global seatcount
    global result

    roomwise=[]
    if (seatcount+seats > count):
        seats=count-seatcount
    seatcount +=seats
    
    # Create list slice to hold 'roomwise' members
    roomwise = li[loc:seatcount]
    loc=seatcount
    result.append(roomwise)     # Add this slice to our result list.

def printing(mychart):        #Creating a function for showing the output, i.e the end result of the allocation
    global result
    global count

    color=["red", "blue", "purple", "green","black","orange",]    #assigning colors to each room
    Label(mychart, text="Room Allotment", fg="red").grid(row=2, column=0, columnspan=2)

    for i in range(rooms):
        mycolor=color[i%len(color)]
        msg="Room {} - ({} seats)".format(i+1, len(result[i]))
        Label(mychart, text=msg, fg=mycolor).grid(row=4, column=i*3, columnspan=2)

        
        if not result[i]:
            Label(mychart, text="This room is empty", fg=mycolor).grid(row=6, column=i*3)

        else:
            k = 0
            r = math.ceil(len(result[i])/3)  # Three columns per room, which r determines rows
            for row in range(r):
                for col in range(3):
                    if (k == len(result[i]) or count == 0):
                        break
                    else:
                        Label(mychart, text=result[i][k], fg=mycolor).grid(row=6+row, column=i*3+col)  #printing of each ID / roll no.
                        k +=1
                        count -=1
                
    

f=open(r"C:\\roll.txt","r")
reading(f)
count = len(li)     # Total number of students

rooms=int(input("Enter the number of rooms avalible for the examination/meeting: "))  #

for i in range(rooms):
    seats=int(input("Enter number of seats avalible in the room: "))
    allot(seats)

mychart = Tk()
mychart.title("Seat Allotment ")

Label(mychart, text="21BIT0637 - VRISHANK S HIREMATH", fg="red", bg="yellow").grid(row=0, column=0, columnspan=4)

printing(mychart)

Button(mychart,text=" QUIT ",command=mychart.destroy).grid(row=0, column=10)    #creating a quit button to close the window
mychart.mainloop()

