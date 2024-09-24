from tkinter import*
import tkinter.messagebox

class numbersOnly:

    def __init__(self, root):
        self.root = root
        self.root.title("Materials Calculator")
        self.root.configure(bg = "#15d47b")
        self.root.geometry("950x600")

#Frame
        mainFrame = Frame(self.root, bd = 10, relief=RIDGE)
        mainFrame.grid()

        Tops = Frame(mainFrame, bd = 10, width=860, height=450, relief=RIDGE)
        Tops.pack(side=TOP)

        self.lblTitle = Label(Tops, font = ('Helvetica', 61, 'bold'), text = "Materials Calculator",
                              justify = CENTER, bg = "#15d47b")
        self.lblTitle.grid()

        MemberName = LabelFrame(mainFrame, bd = 10, width = 840, height = 200, relief=RIDGE,
                                font = ('Helvetica', 20, 'bold'), text = "Enter wall dimensions:" )
        MemberName.pack(side=TOP)


        ButtonWidget = LabelFrame(mainFrame, bd = 10, width = 840, height = 200, relief=RIDGE,
                                font = ('Helvetica', 20, 'bold'), text = "Buttons" )
        ButtonWidget.pack(side=TOP)

#Variables

        NumOne = StringVar()
        NumTwo = StringVar()
        NumThree = StringVar()
        NumFour = StringVar()
        NumFive = StringVar()
        Answer = StringVar()


#Widget

        #Wall height
        self.lblNumOne = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Wall height(m)", bd = 7)
        self.lblNumOne.grid(row = 0, column = 0, sticky = W)
        self.entNumOne = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = NumOne,
                               width=42)
        self.entNumOne.grid(row = 0, column = 1)

        #Short wall length
        self.lblNumTwo = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Short wall length(m)", bd = 7)
        self.lblNumTwo.grid(row = 1, column = 0, sticky = W)
        self.entNumTwo = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = NumTwo,
                               width=42)
        self.entNumTwo.grid(row = 1, column = 1)

        #Long wall length
        self.lblNumThree = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Long wall length(m)", bd = 7)
        self.lblNumThree.grid(row = 2, column = 0, sticky = W)
        self.entNumThree = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = NumThree,
                               width=42)
        self.entNumThree.grid(row = 2, column = 1)

        #Paint cost
        self.lblNumFour = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Paint cost(£/m²)", bd = 7)
        self.lblNumFour.grid(row = 3, column = 0, sticky = W)
        self.entNumFour = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = NumFour,
                               width=42)
        self.entNumFour.grid(row = 3, column = 1)

        #Floor cost
        self.lblNumFive = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Floor cost(£)", bd = 7)
        self.lblNumFive.grid(row = 4, column = 0, sticky = W)
        self.entNumFive = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = NumFive,
                               width=42)
        self.entNumFive.grid(row = 4, column = 1)

        #Answer
        self.lblAnswer = Label(MemberName, font = ('Helvetica', 20, 'bold'), text = "Total cost(£)", bd = 7)
        self.lblAnswer.grid(row = 5, column = 0, sticky = W)
        self.entAnswer = Entry(MemberName, font = ('Helvetica', 20, 'bold'), bd = 7, textvariable = Answer,
                               width=42, state = DISABLED)
        self.entAnswer.grid(row = 5, column = 1)

        
#Functions
        def Reset():
            NumOne.set("")
            NumTwo.set("")
            NumThree.set("")
            NumFour.set("")
            NumFive.set("")
            Answer.set("")
            self.entNumOne.focus()
            return

        def Exit():
            Exit = tkinter.messagebox.askyesno("Materials Calculator", "Are you sure you want to exit?")
            if Exit > 0:
                root.destroy()
                return

        def Calculate():
            a = NumOne.get()
            b = NumTwo.get()
            c = NumThree.get()
            d = NumFour.get()
            e = NumFive.get()
            try:
                a == float(a) and b == float(b) and c == float(c) and d == float(d) and e == float(e)
            except ValueError:
                tkinter.messagebox.askyesno("Invalid Data", "Numbers only please!!")
                return False
            else:
                cost = (((2 * float(a) * float(b) + (2 * float(a) * float(c))))/float(d)) + float(e)
                Answer.set(cost)
                return True 


#Tutorials solution (modified):
            
            #if (a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit()):
                #cost = ((2 * float(a) * float(b) + (2 * float(a) * float(c))))/float(d)
                #Answer.set(cost)
                #return True
            #else:
                #tkinter.messagebox.askyesno("Invalid Data", "Numbers only please!!") 
                #NumOne.set("")
                #NumTwo.set("")
                #NumThree.set("")
                #NumFour.set("")
                #Answer.set("")
                #self.entNumOne.focus()
                #return False
            
#Buttons
        self.entNumOne.focus()

        #Calculate
        self.btnValidate = Button(ButtonWidget, font = ('Helvetica', 20, 'bold'), width=15,height = 2,
                text = "Calculate", bg="#15d47b", command=Calculate).grid(row = 0, column = 0, padx = 8)
        #Reset
        self.btnValidate = Button(ButtonWidget, font = ('Helvetica', 20, 'bold'), width=15,height = 2,
                text = "Reset", bg="#15d47b", command=Reset).grid(row = 0, column = 1, padx = 8)
        #Exit
        self.btnValidate = Button(ButtonWidget, font = ('Helvetica', 20, 'bold'), width=15, height = 2,
                text = "Exit", bg="#15d47b", command=Exit).grid(row = 0, column = 12, padx = 8)


        
if __name__=='__main__':
    root = Tk()
    application = numbersOnly(root)
    root.mainloop()
