import time
from tkinter import filedialog
import colorama
import random
colorama.init()
from colorama import init, Fore, Back, Style
from playsound import playsound 
e = '\33[0m'
y2 = '\33[93m'
y = '\33[33m'
global tutd
comma = ','
tutd = '0'

def ballw():
    inputList = ['spageti', 'pepr', 'coke', 'pepsi', 'sprite', 'dr pep', 'slime', 'glue']


    option = input("Would you like To shake the 8 ball? (Y for yes N for no)")

    if option == "Y":
        resultSet=set(inputList)

        uniqueList =list(resultSet)

        print("The Magic 8 ball says:")
        a = random.sample(uniqueList, 1)
        print(a[0])
        time.sleep(1)
        bal = ballw()
        return bal
    if option == "N":
        print("retuning to menu")
    else:

        print("Thats not an option!")
        bal = ballw()
        return bal


def update():
    time.sleep(1)
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
    fix = input("Put 1 for yes and 0 for no:")
    if fix == "1":
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
    time.sleep(1)
    print("Update me, wont you?")
    time.sleep(.5)
    fix1()
    print("Thank you. listen, when you get to the update screen, you will have to type update()")
    time.sleep(1)
    print("and only update() anything else wont work.")
    time.sleep(1.2)
    print("alright, im going to initiate the update, rememeber, update()!!")
    time.sleep(1)
    screset()
    print(Fore.GREEN + "<BOB BIOS>")
    time.sleep(1)
    update()
    print("update initiated.")
    playsound('beep2.wav')
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
    s = open('file.txt','r')
    with open('file.txt') as s:
        data = s.read()
    print("Save Loaded")
    s.close()

readfile()
d = data.split(",")


if not d[0] == 'done':
    startup()
    readfile()
    d = data.split(",") 

name = d[1]
print("Hello, " + name + "!")
time.sleep(1)
print("What can i help you with?")
print("1.Magic 8 Ball")
menu = input("Put the number for the thing you want!")
if menu == '1':
    ballw()
