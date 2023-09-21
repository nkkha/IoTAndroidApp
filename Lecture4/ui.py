import tkinter as tk

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentController:
    def __init__(self):
        self.students = []

    def insertStudent(self, student):
        self.students.append(student)
        
def onClick():
    #TODO
    name = txtA.get("1.0","end")
    age =txtB.get("1.0","end")
    aStudent = Student(name,age)
    StudentController().insertStudent(aStudent)
    return

window = tk.Tk()
window.title("Python App")
window.geometry("600x400")

labelA=tk.Label(text="Student Name:")
labelA.place(x=5,y=5,width=80,height=30)

txtA=tk.Text()
txtA.place(x=85,y=5,width=100,height=30)

labelB=tk.Label(text="Student Age:")
labelB.place(x=5,y=35,width=80,height=30)

txtB=tk.Text()
txtB.place(x=85,y=35,width=100,height=30)

button = tk.Button(text="Save",command=onClick)
button.place(x=85,y=70,width=100,height=30)

# window.mainloop()