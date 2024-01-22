import tkinter as tk
from tkinter import ttk #importing ttk module from the tkinter library
from tkinter import messagebox
import sqlite3 as sql # importing sqlite3 module

#defining an empty list
tasks = []

#defining a function to add tasks into list
def add_task():
    task_string = task_field.get()
    if len(task_string)==0:
        messagebox.warning("Error", "Task box is Empty")
    else:
        tasks.append(task_string) #adding tasks to task list
        #using execute() statement to execute a sql statement
        the_cursor.execute('insert into tasks values(?)',(task_string))
        list_update()
        task_field.delete(0,"end")


#defining function to update new tasks in the list
def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert("end",task) #using insert method to insert task into the list

#defining a function to delete tasks form the list
def delete_task():
    #suing try-except method
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            #using execute() method to execute a sql statement
            the_cursor.execute("delete form tasks where title = ?", (the_value))

    except:
        messagebox.warning("Error" , "Please select a task to delete")

#defining a function to delete all tasks form the list

def delete_all_tasks():
    message_box = messagebox.askyesorno("Delete All", "Are you Sure?" )

    if message_box==True:
        while(len(tasks)!=0):
            tasks.pop()
        the_cursor.execute("delete form tasks")

        list_update()

#defining a function to clear the list

def clear_list():
    task_listbox.delete(0,"end")

#defining a function to close the application

def close():
    print(tasks)

    guiWindow.destroy()

#defining a function to restore data from the database

def restore_database():
    #iterating elements in the list
    while(len(tasks)!=0):
        #pop method to pop elements form the list
        tasks.pop()
        #iterrating through the rows in the database table
    for row in the_cursor.execute("select title from tasks"):
        tasks.append(row[0])


#---------->MAIN FUNCTION<-----------

if __name__ == "__main__":
    guiWindow = tk.Tk()
    #title for the window
    guiWindow.title("To-DO list -- Codesoft")
    guiWindow.geometry("500x500")
    guiWindow.resizable(False,False)
    guiWindow.configure(bg = "#E6E6FA")


    #using connect method too connect to the database
    the_connection = sql.connect('listOfTasks.db')  
# creating an object of the cursor class  
    the_cursor = the_connection.cursor()  
# using the execute() method to execute a SQL statement  
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    #defining frames 

    header_frame = tk.Frame(guiWindow, bg = "#2F4F4F")
    header_frame.pack(fill = "both")
    function_frame = tk.Frame(guiWindow, bg = "#BC8F8F" )
    function_frame.pack(side = "left", expand = True, fill = "both")
    listbox_frame = tk.Frame(guiWindow, bg = "#00FFFF")
    listbox_frame.pack(side = "right", expand = True, fill = "both")

    #defining label using ttk.label() widget
    header_label = ttk.Label(
        header_frame, text = "To-Do List",
        font=("Lucida calligraphy", 40),
        background = "#FAEBD7",
        foreground = "#8B4513"
    )
    header_label.pack(padx = 20, pady = 20)

    task_label = ttk.Label(
        function_frame,
        text = "Enter the Task:",
        font = ("Ariel","11","bold"),
        background = "#FAEBD7",  
        foreground = "#000000"  
    )






    guiWindow.mainloop()
        