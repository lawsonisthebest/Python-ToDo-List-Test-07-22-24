import tkinter as tk
import customtkinter as ctk
from tkinter import ttk


window = ctk.CTk()
window.geometry('300x500')
window.resizable('False', 'False')
window.title('Todo List')
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

def submit():
    data = todoEntry.get()
    table.insert(parent='', index=tk.END, values=data)

todoEntry = ctk.CTkEntry(window, placeholder_text='Type Something Here:', width=400)
todoEntry.pack(pady=(15,0), fill='both', padx=(15, 15))

submitButton = ctk.CTkButton(window, text='Submit', command=submit, width=150)
submitButton.pack(pady=(10,0))

table = ttk.Treeview(window, columns=('List'), show='headings')
table.heading('List', text='Todo List:')
table.pack(fill = 'both', expand = True, pady=(10,15), side='bottom', padx=15)

def deleteItems(_):
    for i in table.selection():
        table.delete(i)


table.bind('<Delete>', deleteItems)

window.mainloop()