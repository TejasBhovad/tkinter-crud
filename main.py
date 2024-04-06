from tkinter import *
from backend.main import get_countries


class Table:
    def __init__(self, root, lst):
        self.lst = lst
        total_rows = len(lst)
        total_columns = len(lst[0])
        # data table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='white', font=('Arial', 12, 'normal'))

                self.e.grid(row=i, column=j)  # place the cells in a grid
                self.e.insert(END, lst[i][j])
                self.e.config(state='readonly')


# get the data
data = get_countries().data

# convert the data into a list of tuples
data_points = [(item['id'], item['name'], item['continent']) for item in data]

# create root window
tk = Tk()

# create frames
top_frame = Frame(tk, bg='blue')
top_frame.pack(side=TOP, fill=BOTH, expand=True)

bottom_frame = Frame(tk, bg='red')
bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=True)

# create a new frame for the table
table_frame = Frame(top_frame)
table_frame.place(relx=0.5, rely=0.5, anchor='center')  # center the table frame

# add table to table frame
t = Table(table_frame, data_points)

# add label to bottom frame
label = Label(bottom_frame, text="Other stuff goes here", bg='red', fg='white')
label.pack()

tk.mainloop()