import sqlite3
import tkinter as tk

def add_data():
    name = name_entry.get()
    age = age_entry.get()
    
    cursor.execute('''
        INSERT INTO my_table (name, age)
        VALUES (?, ?)
    ''', (name, age))
    
    conn.commit()
    display_data()

def display_data():
    cursor.execute('SELECT * FROM my_table')
    rows = cursor.fetchall()

    output.delete(1.0, tk.END)
    for row in rows:
        output.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}\n")

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

root = tk.Tk()
root.title("Database Frontend")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# Button
add_button = tk.Button(root, text="Add Data", command=add_data)
add_button.grid(row=2, column=0, columnspan=2)


output = tk.Text(root, height=10, width=30)
output.grid(row=3, column=0, columnspan=2)

display_data()

root.mainloop()
