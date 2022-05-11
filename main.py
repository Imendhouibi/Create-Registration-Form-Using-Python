from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")


#heading
Label(root,text="Register Form", font="ar 30 bold").grid(row=0,column=3)

#Field Name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")

#Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)


#variable for storing Data
namevalue= StringVar
phonevalue= StringVar
gendervalue= StringVar


checkvalue=IntVar
#creating entry Field
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)

#packing entry fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)

#creating Checkbox
checkbtn = Checkbutton(text="remember me?",variable= checkvalue)
checkbtn.grid(row=4,column=3)

Button(text="Submit",command=getvals).grid(row=5,column=3)

root.mainloop()

