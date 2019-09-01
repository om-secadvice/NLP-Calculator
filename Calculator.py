from tkinter import *
import tkinter.messagebox as msgBox
import BackendCode as backendCode

root = Tk()
root.title("NLP Calculator")
root.iconbitmap("calculator.ico")
root.configure(background="#cfcfcf")
root.resizable(0,0)

def showResult():
  userQuery = entryQuery.get()
  try:
    finalResult = backendCode.startTask(userQuery)
  except Exception as e:
    msgBox.showinfo("ERROR", "Incorrect input format. Resolve and try again.")
    resetCalculator()
  else:
    textResult.configure(state=NORMAL)
    textResult.delete("1.0", END)
    textResult.insert(INSERT,finalResult)
    textResult.configure(state=DISABLED)
  
def resetCalculator():
  entryQuery.delete(0,END)
  textResult.configure(state=NORMAL)
  textResult.delete("1.0", END)
  textResult.insert(INSERT,"Result is displayed here...")
  textResult.configure(state=DISABLED)
  
labelTitle = Label( root, bd=1, relief=SOLID, width=40, height=5, padx=10, pady=5, font=("", 24, "bold"), text="NLP Calculator", justify='center')
labelTitle.pack(padx=15, pady=15)

frame = Frame(root, bd=1, relief=SOLID, padx=10, pady=10)
frame.pack(padx=15, pady=15)

labelQuery = Label(frame, bd=10, font=20, text="Enter Query: ")
labelQuery.pack(padx=15, pady=15)

entryQuery = Entry(frame, bd=2, relief=RIDGE, width=70, font=12)
entryQuery.pack(padx=15, pady=15)

buttonOK = Button(frame, text="OK", font=10, width=20, height=2, command=showResult)
buttonOK.pack(padx=15, pady=15)

buttonReset = Button(frame, text="Reset", font=10, width=20, height=2, command=resetCalculator)
buttonReset.pack()

labelResult = Label(frame, bd=10, font=20, text="Result: ")
labelResult.pack(side=LEFT, padx=15, pady=15)

textResult = Text(frame, bd=2, relief=RIDGE, font=12, width=60, height=5)
textResult.insert(INSERT, "Result is displayed here...")
textResult.configure(state=DISABLED)
textResult.pack(padx=15, pady=15)

root.mainloop()