
import tkinter as tk
import pandas as pd
from tkinter import *
from tkinter import ttk

# from statistics import pvariance
# import pandas as pd
# import scipy as sp
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from matplotlib.figure import Figure 
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 


# import sklearn as skl 
# import numpy as np
# from scipy import fftpack
# from scipy import signal
# import pylab
# from datetime import datetime
# import yfinance as yf
# ### STATS PACKAGES
# import statsmodels.api as sm
# import statsmodels.formula.api as smf
# import statsmodels.graphics.api as smg
# import patsy
# from scipy import stats


### setup Window
mainWIN = Tk()
mainWIN.geometry("1000x900")
mainWIN.configure(bg='darkgrey')


#Entry, ticker start, stop and interval inputs
Ticker_lab = Label(mainWIN,text = "Ticker")
Ticker_txt = ttk.Entry(mainWIN, width = 20)
START_lab = Label(mainWIN,text = "Start DateTime(yyyy-mm-dd)")
START_txt = ttk.Entry(mainWIN, width = 20)
STOP_lab =  Label(mainWIN, text = "STOP DateTime(yyyy-mm-dd)" )
STOP_txt = ttk.Entry(mainWIN, width = 20) 
Interval_lab = Label(mainWIN, text = "Interval (Sample TimeStep)")
Intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
### Draws Above Entries and Label
Interval_txt = ttk.Combobox(master = mainWIN ,values = Intervals )


#plt.style.use('seaborn-v0_8-darkgrid') # Using a specific seaborn style

##########################
#### IMPORT DATA FUNCTION
def IMPORT_DATA(ticker, start0, end0 , intvl):

        if not ticker or not start0 or not end0 or not intvl: print("Nothin'")
        elif ticker:
            #Import Yahoo Data and store in CSV then edit text to collumns
            DF = yf.Ticker(ticker)
            print(ticker)
            DF_data = pd.DataFrame(DF.history(start = start0, end = end0, interval = intvl))
            ## place insert 'Index' code here...
            print(DF_data)
            print("df type is -> ",type(DF_data))
            DF_data.to_csv('{file_path}'+ticker+'.csv', index=True)
            return pd.read_csv('{file_path}'+ticker+'.csv')

                

##############################
### FUNCTION for IMPORT BUTTON
def runIMPORTbutton(): 
    IMPORT_DATA(ticker = Ticker_txt.get(), start0 = START_txt.get(), end0 = STOP_txt.get(), intvl = Interval_txt.get())  
### DRAW IMPORT BUTTON
IMPORT_button = Button(master = mainWIN, text = "IMPORT DATA",command = runIMPORTbutton  )
### DRAW SET DROPDOWN BUTTON


### loops that places above widgets in order
winLIST1 =[ Ticker_lab,Ticker_txt ,START_lab ,START_txt ,STOP_lab ,STOP_txt,Interval_lab, Interval_txt, IMPORT_button]
### Draws Above Entries and Label
for i in range(0,len(winLIST1)): winLIST1[i].place(x=25,y=25*(i+1))



###########################################################################################################
###########################################################################################################
###########################################################################################################
### setup canvas for scollable content
canvas1 = tk.Canvas(mainWIN, bg="black", width=1000, height=1000) #canvas1 is parent to frame1
canvas1.place( x= 250,y=0) # Place the canvas into the frame, plced slightly to the right, using coordinates. subsequnet frames will be in a grid.


# frame dims
frame1x = 200
frame1y = 100

### create scrollbar set in mainWIN1
scrollbar_y = tk.Scrollbar(mainWIN, orient=tk.VERTICAL, command=canvas1.yview)
scrollbar_y.place(x = 1050+frame1x, y = 0,relheight=1)
canvas1.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(mainWIN, orient=tk.HORIZONTAL, command=canvas1.xview)
scrollbar_x.place(x = frame1x, y= 1000,relwidth=0.547)
canvas1.config(xscrollcommand=scrollbar_x.set)


# create FRAME(or canvas) set in Canvas1, parent to sub-canvases and PLOTS on grid()
frame1 = tk.Canvas(canvas1, width=100, height=1200, bg="darkred")
frame1.place(x=0, y=0) # Places the top-left corner of the canvas at ()
frame1.bind("<Configure>", lambda e: canvas1.configure(scrollregion=canvas1.bbox("all")))# binds events for frame and canvas1
# initialize 'window frame'
canvas1.create_window((10, 00), window=frame1, anchor = 'nw')# place at coords within frame1





########################################################################################################################
#######################  sub-canvas1 onto frame1  [0,0] and [0,1]
########################################################################################################################

### sub canvas1
sub_canvas1 = tk.Canvas(frame1, bg="blue", width=300, height=700) # Canvas parent is 'frame'
sub_canvas1.grid( row= 0,column=0) # Pack the canvas into the frame
sc1_lab = Label(sub_canvas1,text = "SubCanvas1")
sc1_lab.place(x = 10, y = 10)


### DV DropwDOwn
SetDT_lab = Label(master = sub_canvas1, text = "Set Dependent Variable")
Datelist = ['Datetime', 'Date', 'Time', 'Index', 'Volume']
### Draws Above Entries and Label
SetDT_entry = ttk.Combobox(master =sub_canvas1,text = Datelist ,values = Datelist)
SetDT_entry.place(x = 50, y = 50)


##############################################################################################

   ### sub canvas1a
sub_canvas1a = tk.Canvas(frame1, bg="darkblue", width=300, height=700) # Canvas parent is 'frame'
sub_canvas1a.grid( row= 0,column=1) # Pack the canvas into the frame
sc1_laba = Label(sub_canvas1a,text = "SubCanvas1a")
sc1_laba.place(x = 10, y = 10)


### DV DropwDOwn
SetDT_laba = Label(master = sub_canvas1a, text = "Set Dependent Variable")
Datelista = ['Datetime', 'Date', 'Time', 'Index', 'Volume']
### Draws Above Entries and Label
SetDT_entrya = ttk.Combobox(master =sub_canvas1,text = Datelist ,values = Datelist)
SetDT_entrya.place(x = 50, y = 50)



######################################################################################################
######################################################################################################
############### sub canvas2 onto frame1
######################################################################################################


### sub canvas2
sub_canvas2 = tk.Canvas(frame1, bg="blue", width=300, height=700) # Canvas parent is 'frame'
sub_canvas2.grid( row= 1,column=0) # Pack the canvas into the frame

sc2_lab = Label(sub_canvas2,text = "SubCanvas2")
sc2_lab.place(x = 10, y = 10)

### sub canvas2a
sub_canvas2a = tk.Canvas(frame1, bg="darkred", width=300, height=700) # Canvas parent is 'frame'
sub_canvas2a.grid( row= 1,column=1) # Pack the canvas into the frame

sc2_laba = Label(sub_canvas2a,text = "SubCanvas2a")
sc2_laba.place(x = 10, y = 10)

###sub-sub canvas onto canvas2a

miniSUB_2a_0 = tk.Canvas(sub_canvas2a, bg="yellow", width=100, height=700/2) # Canvas parent is 'frame'
miniSUB_2a_0.grid( row= 0,column=0) # Pack the canvas into the frame

miniSUB_2a_1 = tk.Canvas(sub_canvas2a, bg="grey", width=100, height=700/2) # Canvas parent is 'frame'
miniSUB_2a_1.grid( row= 0,column=1) # Pack the canvas into the frame

miniSUB_2a_2 = tk.Canvas(sub_canvas2a, bg="black", width=100, height=700/2) # Canvas parent is 'frame'
miniSUB_2a_2.grid( row= 1,column=0) # Pack the canvas into the frame

miniSUB_2a_3 = tk.Canvas(sub_canvas2a, bg="yellow", width=100, height=700/2) # Canvas parent is 'frame'
miniSUB_2a_3.grid( row= 1,column=1) # Pack the canvas into the frame


######################################################################################################################
######################################################################################################################
############ subcanvas3 onto frame1
######################################################################################################################

sub_canvas3 = tk.Canvas(frame1, bg="blue", width=300, height=700) # Canvas parent is 'frame'
sub_canvas3.grid( row= 2,column=0) # Pack the canvas into the frame

sc3_lab = Label(sub_canvas3,text = "SubCanvas3")
sc3_lab.place(x = 10, y = 10)


sub_canvas3a = tk.Canvas(frame1, bg="darkblue", width=300, height=700) # Canvas parent is 'frame'
sub_canvas3a.grid( row= 2,column=1) # Pack the canvas into the frame

sc3_laba = Label(sub_canvas3a,text = "SubCanvas3a")
sc3_laba.place(x = 10, y = 10)



################################################################################################
################################################################################################


mainWIN.resizable(True, True) 

### MAIN LOOP
mainWIN.mainloop()








