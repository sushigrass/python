#Peter Gillis - A00347016 - CSCI3430 Assignment 09 - Python 2.7.10

#Question 1
def fOnly(list):
    return [x for x in list if isinstance(x, float)]

#Question 2
def fNonPrimes(n):
    return list(filter(lambda x: not isPrimeNumber(x), range(2, n + 1)))

#Question 2 helper function
def isPrimeNumber(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

#Question 3
def speedLimit():
    while True:
        try:
            speedLimit = int(raw_input("Enter speed limit: "))
            speedGoing = int(raw_input("Enter speed you are going: "))
            if speedLimit < 0 or speedGoing < 0:
                print "Numbers entered cannot be less than 0. Try again"
            else:
                if speedGoing > 400 or speedGoing <= speedLimit:
                    fine = 0
                elif speedGoing > speedLimit + 20:
                    fine = 7700 + (1000 * (speedGoing - (speedLimit + 20)))
                elif speedGoing >= speedLimit + 5 and speedGoing <= speedLimit + 20:
                    fine = 200 + (500 * (speedGoing - (speedLimit + 5)))
                else:
                    fine = 200
                print("Your speeding fine is: {}".format(fine))
                break;
        except ValueError:
            print "Input is not an integer. Try again"

#Question 4 - Tkinter
import Tkinter
import tkMessageBox
root = Tkinter.Tk()
root.withdraw()
def question4():
    tkMessageBox.showwarning("Hi, this is my title", "Press ok plz")
    return

#Question 5
from threading import Thread, Lock
import datetime
import time
import sys

mutex = Lock()
theDate = datetime.datetime.now().strftime('%H:%M:%S')
quit = False

def findTime():
    global theDate
    while True:
        if (quit):
            break
        mutex.acquire()
        theDate = datetime.datetime.now().strftime('%H:%M:%S')
        mutex.release()
        time.sleep(0.01)

def displayTime():
    alreadyPrinted = 0
    while True:
        if (quit):
            break
        if alreadyPrinted != theDate:
            print(theDate)
        alreadyPrinted = theDate
        time.sleep(0.5)

def startTheProgram():
    global quit
    print "\nEnter q to quit.\n"
    Thread(target = findTime).start()
    Thread(target = displayTime).start()
    while True:
        quitSignal = raw_input()
        if (quitSignal=="q"):
            quit = True
            print "Closing the threads & ending the program, bye!"
            break
        else:
            print "\nEnter q to quit.\n"
