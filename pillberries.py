from gpiozero import Buzzer,LED,Button
import time
from time import sleep
from datetime import datetime
buzz = Buzzer(6)
button = Button(17)
OM = LED(13)#Omeperazole
BU = LED(19)#Buscopan
AZ = LED(16)#Azathioprine
SA = LED(5)#Salofalk
# this is an array which stores all the days and times the buzzer should go off
# eg 5(Sat) 18,32 (6.32pm)
# There are 4 times in here
#ISSUE:when trying to do 08 as the minute it will say the 0 is an invalid token

schedule = [
    [4,13,12],
    [0,19,30],
    [1,8,30],
    [1,19,30],
    [2,8,30],
    [2,19,30],
    [3,8,30],
    [3,19,30],
    [4,8,30],
    [4,19,30],
    [5,8,30],
    [5,19,30],
    [6,8,30],
    [6,19,30],
]
# TODO - read these in from somewhere else...
#for each of the 4 times I've got another array to
# store whether they have been snoozed by the button
alarmSnoozed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False]
ledSchedule=[SA,AZ,SA,OM,SA,AZ,BU,OM,BU,OM,SA,AZ,BU,OM]
pillnumbers=[2,2,3,1,1,2,3,1,1,3,2,1,1,2]

# this is a subroutine called alarm
# it takes in two numbers in brackets as variables
# the first (num) tells the subroutine how many times to beep
# the second (alarmnum) tells the subroutine which of the times its the alarm for
def alarm(num, alarmnum):
    global alarmSnoozed
    #run the block of code num times
    for i in range(num):
        if button.is_pressed:
            time.sleep(1)
            alarmSnoozed[alarmnum] = True
            print("Count the beeps for how many pills to take and look at light for which one")
            flash(ledSchedule[alarmnum],pillnumbers[alarmnum])
            break
        buzz.on()
        time.sleep(0.1)
        buzz.off()
        time.sleep(0.3)
# anoth subroutine called flash which takes a number in brackets
# this is how many times it flashes / beeps
def flash(whichled,flashtimes):
    #repeats the number of times given
    for i in range(flashtimes):
        buzz.on()
        whichled.on()
        time.sleep(0.3)
        buzz.off()
        whichled.off()
        time.sleep(0.2)

#main program loop - runs forever
while True:
    now = datetime.now() #get the current day/time
    mynow = [now.weekday(),now.hour,now.minute] # make an array of weekday,hour,minute
    
    print(mynow,now.second)#for debugging
    print(alarmSnoozed, button.is_pressed)#for debugging
    #loop through all the dates / times in the schedule
    for i in range(len(schedule)):
        #check if the mynow variable matches a date in the schedule
        #and they haven't yet snoozed it
        if mynow==schedule[i] and alarmSnoozed[i]==False:
            print("Time to take a pill! Press button to stop alarm!")
            #then ring the alarm ten times
            # it also passes in i which is the number of the day in the schedule that matches
            alarm(10,i)
# TODO need to set the alarmSnoozed array back to all False on midnight Monday!





    
