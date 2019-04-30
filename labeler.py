#usr/bin/python3
# SUPERHUB Reverse Logistics Printer, written by Rob Morrow 4/2019
 
import tkinter as tk
import os
import subprocess as sub
import datetime 
from tkinter import *
 
master = Tk()
master.attributes("-fullscreen", True)
master.title("SUPERHUB Reverse Logistics Label Printer")
master.option_add('*font', ('verdana', 12, 'bold'))

def prnt_label(store_Number, delivery_Route):
     datetime_now = datetime.datetime.now()
     #delivery_Route = routNum
     fh = open("rendered.epl","w")
     lines_of_text= """
N
q457
Q228,32,-16
A50,5,0,2,1,1,N,"TRAN#             ORDER #"
A90,45,0,2,2,2,N,"STORE #0{0}"
A50,100,0,3,1,1,N,"{1}"
A150,150,0,2,1,1,N,"Route:{2}"
A150,200,0,2,1,1,N,"From: Janitrol Rd (7996)"
P1

""".format(store_Number, datetime_now, delivery_Route)
     fh.writelines(lines_of_text)                          
     fh.close()
     sub.run("lp rendered.epl", shell=True)
 
def close(event):
     master.withdraw()
     sys.exit()
 
# Key bindings
master.bind('<Escape>', close)
 
 
# Various program parameters

master.geometry("800x480".format(master.winfo_screenwidth(), master.winfo_screenheight()))
master.focus_set()
 
class App:
     
     def __init__(self, master):

         master.option_add('*font', ('verdana', 12, 'bold'))
     master.configure(background="#CC0033")
     master.grid_columnconfigure((0,12), weight=1)
     master.grid_rowconfigure((0,10), weight=1)

          
     
     button1 = Button(master, text="1008", command=lambda : prnt_label("1008", "None specified"))
     button1.grid(row=1, column=1, padx=30, pady=30)
     button2 = Button(master, text="1009", command=lambda : prnt_label("1009", "Columbus 16VSH2"))
     button2.grid(row=3, column=1, padx=30, pady=30)
     button3 = Button(master, text="1043", command=lambda : prnt_label("1043", "None specified"))
     button3.grid(row=5, column=1, padx=30, pady=30)
     button4 = Button(master, text="1051", command=lambda : prnt_label("1051", "None specified"))
     button4.grid(row=7, column=1, padx=30, pady=30)
     button5 = Button(master, text="1061", command=lambda : prnt_label("1061", "Columbus 16VSH2"))
     button5.grid(row=9, column=1, padx=30, pady=30)

     button6 = Button(master, text="1063", command=lambda : prnt_label("1063", "Columbus 13"))
     button6.grid(row=1, column=3, padx=30, pady=30)
     button7 = Button(master, text="1064", command=lambda : prnt_label("1064", "None specified"))
     button7.grid(row=3, column=3, padx=30, pady=30)
     button8 = Button(master, text="1083", command=lambda : prnt_label("1083", "None specified"))
     button8.grid(row=5, column=3, padx=30, pady=30)
     button9 = Button(master, text="1086", command=lambda : prnt_label("1086", "Columbus 14",))
     button9.grid(row=7, column=3, padx=30, pady=30)
     button10 = Button(master, text="2042", command=lambda : prnt_label("2042", "Columbus 17VSH3"))
     button10.grid(row=9, column=3, padx=30, pady=30)
     
     button11 = Button(master, text="6485", command=lambda : prnt_label("6485", "None specified"))
     button11.grid(row=1, column=5, padx=30, pady=30)
     button12 = Button(master, text="7524", command=lambda : prnt_label("7524", "Columbus 15",))
     button12.grid(row=3, column=5, padx=30, pady=30)
     button13 = Button(master, text="7541", command=lambda : prnt_label("7541", "None specified"))
     button13.grid(row=5, column=5, padx=30, pady=30)
     button14 = Button(master, text="7545", command=lambda : prnt_label("7545", "PDQ Shuttle"))
     button14.grid(row=7, column=5, padx=30, pady=30)
     button15 = Button(master, text="7570", command=lambda : prnt_label("7570", "None specified"))
     button15.grid(row=9, column=5, padx=30, pady=30)
     
     button16 = Button(master, text="7595", command=lambda : prnt_label("7595", "Columbus 12"))
     button16.grid(row=1, column=7, padx=30, pady=30)
     button17 = Button(master, text="7596", command=lambda : prnt_label("7596", "Columbus 11"))
     button17.grid(row=3, column=7, padx=30, pady=30)
     button18 = Button(master, text="7663", command=lambda : prnt_label("7663", "Columbus 15"))
     button18.grid(row=5, column=7, padx=30, pady=30)
     button19 = Button(master, text="7665", command=lambda : prnt_label("7665", "Columbus 12"))
     button19.grid(row=7, column=7, padx=30, pady=30)
     button20 = Button(master, text="7674", command=lambda : prnt_label("7674", "PDQ Shuttle"))
     button20.grid(row=9, column=7, padx=30, pady=30)
     
     button21 = Button(master, text="7752", command=lambda : prnt_label("7752", "Columbus 10"))
     button21.grid(row=1, column=9, padx=30, pady=30)
     button22 = Button(master, text="7754", command=lambda : prnt_label("7754", "None specified"))
     button22.grid(row=3, column=9, padx=30, pady=30)
     button23 = Button(master, text="7875", command=lambda : prnt_label("7875", "None specified"))
     button23.grid(row=5, column=9, padx=30, pady=30)
     button24 = Button(master, text="7876", command=lambda : prnt_label("7876", "None specified"))
     button24.grid(row=7, column=9, padx=30, pady=30)
     button25 = Button(master, text="8103", command=lambda : prnt_label("8103", "Columbus 14"))
     button25.grid(row=9, column=9, padx=30, pady=30)
     
     button26 = Button(master, text="8468", command=lambda : prnt_label("8468", "None specified"))
     button26.grid(row=1, column=11, padx=30, pady=30)
     button27 = Button(master, text="8476", command=lambda : prnt_label("8476", "Columbus 15"))
     button27.grid(row=3, column=11, padx=30, pady=30)
     button28 = Button(master, text="8956", command=lambda : prnt_label("8956", "Columbus 10"))
     button28.grid(row=5, column=11, padx=30, pady=30)     

     master.store_entry = StringVar()
     entry1 = Entry(master, textvariable=master.store_entry, width=4)
     entry1.grid(row=9, column=11, padx=30, pady=30)
     
     def prnt_store(self):
         #store_Number = self.Entry.get()
         prnt_label(master.store_entry.get(), "None specified")
     
     master.bind('<Return>', prnt_store)
     master.bind('<KP_Enter>', prnt_store)
             
display = App(master)
master.mainloop()
