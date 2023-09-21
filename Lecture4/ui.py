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

import tkinter as tk

def onClick():
    # Add your save logic here
    pass

window = tk.Tk()
window.title("Python App")
window.attributes('-fullscreen', True)

frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

labelA = tk.Label(frame, text="Student Name:")
labelA.grid(row=0, column=0, padx=10, pady=10)
txtA = tk.Text(frame, height=1, width=20)
txtA.grid(row=0, column=1, padx=10, pady=10)

labelB = tk.Label(frame, text="Student Age:")
labelB.grid(row=1, column=0, padx=10, pady=10)
txtB = tk.Text(frame, height=1, width=20)
txtB.grid(row=1, column=1, padx=10, pady=10)

button = tk.Button(frame, text="Save", command=onClick)
button.grid(row=2, column=0, columnspan=2, pady=20)

window.mainloop()


window.mainloop()