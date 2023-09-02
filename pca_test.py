from tkinter import *
from tkinter import ttk, font

serialNumberString = "12345"
startUpDelay = 1
duration = 10
shutdownTime = 1
numberOfTrials = 5

def runFunction ():
    try:
        serialNumberString = SerialNumber_Box.get()
        startUpDelay = int(StartUp_Box.get())
        duration = int(Duration_Box.get())
        shutdownTime = int(Shutdown_Box.get())
        numberOfTrials = int(Trial_Box.get())
    except Exception:
        print("ERROR: Invalid inputs. Values must be greater than zero and not empty.")
        return

    print("                      ")
    print("======================")
    print(" TEST CONFIGURATION   ")
    print("======================")
    print("                      ")
    print("Serial Number: " + str(serialNumberString))
    print("Startup Delay: " + str(startUpDelay))
    print("Test Duration: " + str(duration))
    print("Shutdown Time: " + str(shutdownTime))
    print("Trials       : " + str(numberOfTrials))
    print("                      ")

def callback (input) :
    if input.isdigit() and int(input)<=100 and int(input)>0:
        return True
    
    elif input == "":
        return True
    else:
        return False


window = Tk()
window.geometry("400x250")
window.title("Data Acquisition")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

reg = window.register(callback)
mainframe = ttk.Frame(window, padding="12 12 12 12")
mainframe.grid(column=0, row=0)

ttk.Label(mainframe,text="Serial Number",font=("Arial",16),width=15,justify=LEFT).grid(row=1,column=1)
ttk.Label(mainframe,text="Start Up",font=("Arial",16),width=15,justify=LEFT).grid(row=2,column=1)
ttk.Label(mainframe,text="Duration",font=("Arial",16),width=15,justify=LEFT).grid(row=3,column=1)
ttk.Label(mainframe,text="Shutdown",font=("Arial",16),width=15,justify=LEFT).grid(row=4,column=1)
ttk.Label(mainframe,text="Trials",font=("Arial",16),width=15,justify=LEFT).grid(row=5,column=1)

SerialNumber_Box = Entry(mainframe, width=10, font=("Arial", 16))
SerialNumber_Box.grid(row=1, column=2)
SerialNumber_Box.insert(0,serialNumberString)

StartUp_Box = Entry(mainframe, width=10, font=("Arial", 16))
StartUp_Box.grid(row=2, column=2)
StartUp_Box.insert(0,startUpDelay)
StartUp_Box.config(validate="key", validatecommand=(reg, '%P'))

Duration_Box = Entry(mainframe, width=10, font=("Arial", 16))
Duration_Box.grid(row=3, column=2)
Duration_Box.insert(0,duration)
Duration_Box.config(validate="key", validatecommand=(reg, '%P'))

Shutdown_Box = Entry(mainframe, width=10, font=("Arial", 16))
Shutdown_Box.grid(row=4, column=2)
Shutdown_Box.insert(0,shutdownTime)
Shutdown_Box.config(validate="key", validatecommand=(reg, '%P'))

Trial_Box = Entry(mainframe, width=10, font=("Arial", 16))
Trial_Box.grid(row=5, column=2)
Trial_Box.insert(0,numberOfTrials)
Trial_Box.config(validate="key", validatecommand=(reg, '%P'))

ttk.Label(mainframe,text="",font=("Arial",15),width=20,justify=LEFT).grid(row=6,column=1,columnspan=2)

f = font.Font(weight="bold",size=18,family="Arial")
btn = Button(mainframe, text="RUN", command=runFunction,width=20,bg="green",fg="white",activebackground="white",activeforeground="green")
btn['font'] = f
btn.grid(row=7,column=1,columnspan=2)

ttk.Label(mainframe,text="",font=("Arial",16),width=15,justify=LEFT).grid(row=8,column=1,columnspan=2)

window.mainloop()