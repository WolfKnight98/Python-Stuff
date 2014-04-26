# TKinter Clock Example

from tkinter import * 
import time 

base_panel = Tk() 
clock = Label( base_panel, font = ( 'Arial', 48, 'bold' ), bg = 'red' ) 
clock.pack( fill = BOTH, expand = 1 ) 

def tick(): 
    global time1 
    time1 = ""

    # get the current local time from the PC 
    time2 = time.strftime( '%H:%M:%S' ) 

    # if time string has changed, update it 
    if time2 != time1: 
        time1 = time2 
        clock.config( text = time2 ) 
        
    clock.after( 200, tick ) 

tick() 
base_panel.mainloop() 