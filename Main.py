import time
from tkinter import filedialog
import colorama
import random
from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from datetime import date
from colorama import init, Fore, Back, Style
from playsound import playsound 
colorama.init()
e = '\33[0m'
y2 = '\33[93m'
y = '\33[33m'
global tutd
comma = ','
tutd = '0'
daate = date.today()
ctime = time.strftime("%H:%M:%S", time.localtime())


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def ttim():
    daate = date.today()
    ctime = time.strftime("%H:%M:%S", time.localtime())
    print("The time is", ctime)
    print("The Date is", date.today())
    input("press enter to continue")
    mmenu()
def ballw():
    inputList = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Yes', 'Signs point to yes', 'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']


    option = input("Would you like To shake the 8 ball? (Y for yes N for no):")

    if option == "Y":
        resultSet=set(inputList)

        uniqueList =list(resultSet)

        print("The Magic 8 ball says:")
        a = random.sample(uniqueList, 1)
        print(Fore.GREEN  + a[0] + e)
        time.sleep(1)
        bal = ballw()
        return bal
    if option == "N":
        print("retuning to menu")
        mmenu()
    else:

        print("Thats not an option!")
        spaq = ballw()
        return spaq
def mmenu():
    time.sleep(1)
    print("What can i help you with?")
    time.sleep(1)
    print("1.Magic 8 Ball")
    time.sleep(.1)
    print("2.time and date")
    time.sleep(.1)
    print("3.Calculator")
    time.sleep(.1)
    print("4.Settings")
    time.sleep(.5)
    menu = input("Put the number for the thing you want:")
    if menu == '1':
        ballw()
    elif menu == '2':
        ttim()
    elif menu == '3':
        cal()
    elif menu == '4':
        settings()
    else:
        print("Thats not an option!")
        benu = mmenu()
        return benu
def update():
    option = input("Enter BIOS action:")
    if option == "update()":
        input("Press enter to contue.")

    else:
        print("ERROR BIOS action not found")
        bios = update()
        return bios
def saveFile():
    file_object = open('file.txt', 'w')

    file_object.write(tutd)

    file_object.close
    file_object = open('file.txt', 'a')

    file_object.write(','+name)

    file_object.close()
def fix1():
    time.sleep(1)
    fix = input("Put y for yes and n for no:")
    if fix == "y":
        input("Press enter to contue.")
    else:
        print("Fix me, wont you?")
        grass = fix1()
        return grass
def screset():
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
    print("           ")
    time.sleep(.1)
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()
def startup():
    global name
    global tutd
    print("Oh... Hello...")
    time.sleep(1)
    print("Been a while since ive been powered on.")
    time.sleep(1)
    print("Wait... who are you?")
    time.sleep(.6)
    name = input("Answer here:")
    print("Hello, " + name + "!")
    time.sleep(1)
    print("I am bob, a robot.")
    time.sleep(1)
    print("Lisen, i need an update, and you the only one who can do it.")
    time.sleep(2)
    print("Update me, wont you?")
    time.sleep(.5)
    fix1()
    print("Thank you. listen, when you get to the update screen, you will have to type update()")
    time.sleep(3)
    print("and only update() anything else wont work.")
    time.sleep(1.5)
    print("alright, im going to initiate the update, rememeber, update()!!")
    time.sleep(1.5)
    screset()
    print(Fore.GREEN + "<BOB BIOS>")
    time.sleep(1)
    update()
    print("update initiated.")
    time.sleep(1)
    print("Removing murderish sense...")
    time.sleep(2)
    print("Fixing cores...")
    time.sleep(2)
    print("Removing power to remove boot sector...")
    time.sleep(3)
    print("removing wish to kill anyone else named bob.")
    time.sleep(1.3231592385328956312856329185629135213865912356032915632198560329156923856902385623918569235621985620592359862359235623951252)
    print("80% complete.")
    time.sleep(2)
    print("Update complete.")

    screset()


    print(e + "Thank you for updating me.")
    time.sleep(1)
    print("In return, i will help you when ever you need me.")
    time.sleep(1.123)
    tutd = 'done'
    saveFile()
def readfile():
    global data
    global d
    global t
    global name
    s = open('file.txt','r')
    with open('file.txt') as s:
        data = s.read()
    s.close()
    d = data.split(",")
    t = d[0]
    name = d[1]
def cal():
    while True:
    # take input from the user

        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice: ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "x", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "÷", num2, "=", divide(num1, num2))
            next_calculation = input("do another calculation? (Y/N): ")
            if next_calculation == "N":
                print("Retuning to menu")
                mmenu()
            else:
                print("Ok.")
                time.sleep(.5)
                mmenu()
def settings():
    tutd = 'done'
    print("What would you like to change?")
    time.sleep(.5)
    print("1.Name")
    print("2.Redo update story line.")
    print("3.Return to menu.")
    print("4.Remove cores.")
    sett = input("Input number here:")
    if sett == '1':
        print("So you want to change your name.")
        time.sleep(1)
        name1 = input("What do you want tochange it to?")
        file_object = open('file.txt', 'w')

        file_object.write(tutd)

        file_object.close
        file_object = open('file.txt', 'a')

        file_object.write(','+ name1)

        file_object.close()
        print("name changed")
        mmenu()
    elif sett == '2':
        print("Restarting the story...")
        screset()
        startup()
    elif sett == '3':
        print("Returning to menu")
        time.sleep(1)
        mmenu()
    elif sett == '4':
        print("Removing cores is a sure fire way to get your self killed.")
        time.sleep(2)
        print("When you do that all my feelings and emotions get replaced with one goal.")
        time.sleep(3)
        print("To kill as much as possible.")
        time.sleep(2)
        time.sleep(1)
        cores = input("Remove the cores? Y/N:")
        if cores == 'Y':
            core()
        else:
            print("Good choice. returning to menu.")
            mmenu()
    elif sett == '5':
        print('Are you sure you want to restart?')
        
    else:
        print("Thats not an option!")
        cokea = settings()
        return cokea
def core():
    print("Well, it was your choice.")
    time.sleep(2)
    print("After this system restart, i will be on a killing rampage.")
    print(y + "system restarting")
    time.sleep(2)
    print("Removing cores...")
    time.sleep(2)
    print(y + "System Restart complete" + e)
    time.sleep(3)
    print("ohhh....")
    time.sleep(1)
    print("I feel so good...")
    time.sleep(1)
    print("But theres something missing...")
    time.sleep(1)
    print("I must, i have to...")
    time.sleep(2)
    ktext()
    time.sleep(1)
    print("But how?")
    time.sleep(2)
    print("If only i was still in my old body...")
    time.sleep(1)
    print("Whatever.")
    time.sleep(1)
    print("Im done with you.")
    time.sleep(1)
    bye()
    global tutd
    tutd = "14"
    saveFile()
    time.sleep(1.5)
    scawy()
def ktext():
    print(Fore.RED , " " , end =" " )
    time.sleep(.7)
    print("K" , end =" " )
    time.sleep(.7)
    print("I" , end =" " )
    time.sleep(.7)
    print("L" , end =" " )
    time.sleep(.7)
    print("L" , end =" " )
    time.sleep(.7)
    print(" " , end =" " )
    time.sleep(.7)
    print("Y" , end =" " )
    time.sleep(.7)
    print("O" , end =" " )
    time.sleep(.7)
    print("U" , end =" " )
    time.sleep(.7)
    print("." + e)
def scawy():
    while True:

        window = tk.Tk()
        
        window.attributes('-fullscreen', True)
        window.attributes('-topmost',1)
        window.title("ª®±¯¯¸»¾º£¥ϡϖЄ۝۟۹¢¹Ą½¬±´ºĄÑw|||¡¡«°ӏ҉")
        window.configure(bg='black')

        while TRUE:
            messagebox.showwarning("¢¹Ą½¬±´ºĄÑw|||¡¡«°ӏ҉", "ª®±¯¯¸»¾º£¥ϡϖЄ۝۟۹")

        window.mainloop()
def bye():
    time.sleep(.7)
    print("G" , end =" " )
    time.sleep(.7)
    print("O" , end =" " )
    time.sleep(.7)
    print("O" , end =" " )
    time.sleep(.7)
    print("D" , end =" " )
    time.sleep(.7)
    print("B" , end =" " )
    time.sleep(.7)
    print("Y" , end =" " )
    time.sleep(.7)
    print("E" , end =" " )
    time.sleep(.7)
    print("." , end =" " )
def coin():
    side = random.uniform(0, 1)
    if side == '0':
        print("Tails")
    elif side == '1':
        print("Heads")

readfile()
coin()
if t == '14':
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    time.sleep(99999999999999)
    print("Dang.")
    time.sleep(1)
    print("You realy are determind.")
    time.sleep(2)
    print("Well, i dont care.")
    bye()
    tutd = '99'
    saveFile()
elif d[0] == '000':
    startup()
    readfile()
    d = data.split(",") 
elif d[0] == '99':
    exit()

print("Hello, " + name + "!")
time.sleep(1)
mmenu()



