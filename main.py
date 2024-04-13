from tkinter import *
from backend.main import get_countries, add_country, update_country, delete_country, get_data_by_country

from tkinter import ttk


class Table:
    def __init__(self, root, lst):
        self.lst = lst
        total_rows = len(lst)
        total_columns = len(lst[0])

        # create a canvas on which to place the table
        self.canvas = Canvas(root)
        self.canvas.grid(row=0, column=0, sticky='nsew')  # place the canvas in the grid

        # create a scrollbar
        style = ttk.Style()
        style.configure("Vertical.TScrollbar", gripcount=0,
                        background='gray', darkcolor='gray', lightcolor='gray',
                        troughcolor='gray', bordercolor='gray', arrowcolor='gray')
        scrollbar = ttk.Scrollbar(root, command=self.canvas.yview, style="Vertical.TScrollbar")
        scrollbar.grid(row=0, column=1, sticky='ns')  # place the scrollbar in the grid

        # configure the canvas to scroll with the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # create a frame in the canvas to hold the table
        self.table_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.table_frame, anchor='nw')

        # data table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.table_frame, width=20, fg='white', font=('Arial', 12, 'normal'))

                self.e.grid(row=i, column=j)  # place the cells in a grid
                self.e.insert(END, lst[i][j])
                self.e.config(state='readonly')

        # update the scroll region after the canvas and table_frame have been modified
        self.table_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


def refresh_table():
    # get the data
    data = get_countries().data

    # convert the data into a list of tuples
    data_points = [(item['id'], item['name'], item['continent']) for item in data]

    # add table to table frame
    t = Table(table_frame, data_points)


# get the data
data = get_countries().data

# convert the data into a list of tuples
data_points = [(item['id'], item['name'], item['continent']) for item in data]

# create root window
tk = Tk()
tk.geometry("800x600")
tk.minsize(500, 400)
tk.maxsize(1024, 768)

top_frame = Frame(tk, bg='#494d52')
top_frame.pack(side=TOP, fill=BOTH, expand=True, padx=15, pady=20)

bottom_frame = Frame(tk)
bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=False, padx=15, pady=20)

bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)

# divide the bottom frame into two equal parts horizontally
bottom_frame1 = Frame(bottom_frame, )
bottom_frame1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

bottom_frame2 = Frame(bottom_frame)
bottom_frame2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

bottom_frame3 = Frame(bottom_frame)
bottom_frame3.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
# column

bottom_frame4 = Frame(bottom_frame)
bottom_frame4.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

# Create operation
label = Label(bottom_frame1, text="Create Country")
label.pack(fill=X, padx=5, pady=5)

country_entry = Entry(bottom_frame1)
country_entry.pack(fill=X, padx=5, pady=5)
country_entry.insert(0, "Enter country")

# Create a list of continents
continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'Oceania', 'North America', 'South America']
continent_var = StringVar(bottom_frame1)
continent_var.set(continents[0])  # set the default option

# Create the option menu
continent_option_menu = OptionMenu(bottom_frame1, continent_var, *continents)
continent_option_menu.pack(fill=X, padx=5, pady=5)

Button(bottom_frame1, text="Submit",
       command=lambda: [add_country(country_entry.get(), continent_var.get()), refresh_table()]).pack(fill=X)

# Update operation
label_update = Label(bottom_frame2, text="Update Country")
label_update.pack(fill=X, padx=5, pady=5)

country_entry_update = Entry(bottom_frame2)
country_entry_update.pack(fill=X, padx=5, pady=5)
country_entry_update.insert(0, "Enter country")

# Create a list of continents
continents_update = ['Africa', 'Antarctica', 'Asia', 'Europe', 'Oceania', 'North America', 'South America']
continent_var_update = StringVar(bottom_frame2)
continent_var_update.set(continents_update[0])  # set the default option

# Create the option menu
continent_optionmenu_update = OptionMenu(bottom_frame2, continent_var_update, *continents_update)
continent_optionmenu_update.pack(fill=X, padx=5, pady=5)

Button(bottom_frame2, text="Submit",
       command=lambda: [update_country(country_entry_update.get(), continent_var_update.get()), refresh_table()]).pack(
    fill=X)

# Delete operation
label_delete = Label(bottom_frame3, text="Delete Country")
label_delete.pack(fill=X, padx=5, pady=5)

country_entry_delete = Entry(bottom_frame3)
country_entry_delete.pack(fill=X, padx=5, pady=5)
country_entry_delete.insert(0, "Enter country")

Button(bottom_frame3, text="Submit",
       command=lambda: [delete_country(country_entry_delete.get()), refresh_table()]).pack(fill=X)

# Retrieve operation
label_retrieve = Label(bottom_frame4, text="Retrieve Country")
label_retrieve.pack(fill=X, padx=5, pady=5)

country_entry_retrieve = Entry(bottom_frame4)
country_entry_retrieve.pack(fill=X, padx=5, pady=5)
country_entry_retrieve.insert(0, "Enter country")

Button(bottom_frame4, text="Submit",
       command=lambda: [get_data_by_country(country_entry_retrieve.get()), refresh_table()]).pack(fill=X)

# create a new frame for the table
table_frame = Frame(top_frame)
table_frame.place(relx=0.5, rely=0.5, anchor='center')  # center the table frame

# add table to table frame
t = Table(table_frame, data_points)

tk.mainloop()
