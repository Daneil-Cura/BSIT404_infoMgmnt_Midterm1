from tkinter import *
import pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=COMPLAB503_PC1;Database=DB_inventory;Trusted_Connection=yes;')
id
product=[]

class Product:
    def __init__(self, name, description, size, quantity, price, timestamp):
        self.name = name
        self.description = description
        self.size = size
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp

        def getName(self):
            return self.name

        def getDescription(self):
            return self.description
        def getSize(self):
            return self.size
        def getQuantity(self):
            return self.quantity
        def getPrice(self):
            return self.price
        def getTimeStamp(self):
            return timestamp

def ProductAdd():
    global product
    cursor = conn.cursor()
    date = datetime.datetime.now()
    sql = "INSERT INTO tbl_Products(name,description,size,price,timestamp)VALUES ('" + e1.get() + "', '" + e2.get() + "','" + e3.get() + "','" + e5.get()+"','" +date.strftime("%x")+"')"
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record inserted.")
    DisplayProduct()
    Clear()

def ProductDelete(getProduct):
    global product
    cursor = conn.cursor()
    sql = "DELETE FROM tbl_Products WHERE name='"+getProduct[1]+"' "
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record deleted.")
    DisplayProduct()
    Clear()

def ClickUpdate(getProduct):
    global id
    Clear()
    cursor = conn.cursor()
    sql = "SELECT * FROM tbl_Products WHERE name='"+getProduct[1]+"' "
    cursor.execute(sql)
    e1.insert(0, getProduct[1])
    e2.insert(0, getProduct[2])
    e3.insert(0, getProduct[3])
    e5.insert(0, getProduct[4])
    btnAdd['state'] = DISABLED
    btnUpdate['state'] = NORMAL
    id=getProduct[0]

def ProductUpdate():
    cursor = conn.cursor()
    sql = "UPDATE tbl_Products SET name='"+e1.get()+"', description='"+e2.get()+"', size='"+e3.get()+"', price='"+e5.get()+"' WHERE id='"+str(id)+"' "
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record updated.")
    DisplayProduct()
    Clear()
    btnAdd['state'] = NORMAL
    btnUpdate['state'] = DISABLED
def addHeaders():
    separator.grid(row=7, column=0, columnspan=5, pady=5, sticky=W+E+N+S)
    Label(separator, text="Name", background=color, width=10).grid(row=0, column=0, sticky=W, padx=10, pady=5)
    Label(separator, text="Description", background=color, width=10).grid(row=0, column=1, sticky=W, padx=10, pady=5)
    Label(separator, text="Size",background=color, width=10).grid(row=0, column=2, sticky=W, padx=10, pady=5)
    Label(separator, text="Price", background=color, width=10).grid(row=0, column=3, sticky=W, padx=10, pady=5)
    Label(separator, text="Action", background=color, width=10).grid(row=0, column=4, sticky=W, padx=10, pady=5, columnspan=2)

def DisplayProduct():
    global products
    row = 1
    list = separator.grid_slaves()
    cursor = conn.cursor()
    sql = "SELECT * FROM tbl_Products"
    cursor.execute(sql)
    records = cursor.fetchall()
    for l in list:
        l.destroy()
    addHeaders()
    for record in records:
        Label(separator, text=record[1], background=color, width=10).grid(row=row, column=0, sticky=W, padx=10, pady=5)
        Label(separator, text=record[2], background=color, width=10).grid(row=row, column=1, sticky=W, padx=10, pady=5)
        Label(separator, text=record[3], background=color, width=10).grid(row=row, column=2, sticky=W, padx=10, pady=5)
        Label(separator, text=record[4], background=color, width=10).grid(row=row, column=3, sticky=W, padx=10, pady=5)
      #  Label(separator, text=record[5], background=color, width=10).grid(row=row, column=4, sticky=W, padx=10, pady=5)

        btn_a1 = Button(separator, text="Update", width=7, command=lambda getRecord=record: ClickUpdate(getRecord))
        btn_a2 = Button(separator, text="Delete", width=7, command=lambda getRecord=record: ProductDelete(getRecord))

        btn_a1.grid(row=row, column=5, sticky=W, padx=5, pady=5)
        btn_a2.grid(row=row, column=6, sticky=E, padx=5, pady=5)

        row += 1

def Clear():
    e1.delete(0,'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e5.delete(0, 'end')

root = Tk()
root.title("Inventory System")
root.geometry("635x600")
root.resizable(0, 0)

#for label
Label(root, text="Products Information").grid(row=0, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Name: ").grid(row=1, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Description: ").grid(row=2, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Size: ").grid(row=3, column=0, sticky=W, padx=10, pady=5)
Label(root, text="Product Price: ").grid(row=4, column=0, sticky=W, padx=10, pady=5)

#for textbox
e1 = Entry(root, width=75)  #name
e2 = Entry(root, width=75)  #description
e3 = Entry(root, width=75)  #size
e5 = Entry(root, width=75)  #price
e1.grid(row=1, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e2.grid(row=2, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e3.grid(row=3, column=1, sticky=W, padx=10, pady=5, columnspan=2)
e5.grid(row=4, column=1, sticky=W, padx=10, pady=5, columnspan=2)

#for Button
btnAdd = Button(root, text="Add Product", width=15, state=NORMAL, command=ProductAdd)
btnUpdate = Button(root, text="Update Product", width=15, state=DISABLED, command=ProductUpdate)
btnDelete = Button(root, text="Delete Product", width=15, state=NORMAL, command=ProductDelete)
btnAdd.grid(row=6, column=1, sticky=E, padx=10, pady=5)
btnUpdate.grid(row=6, column=2, sticky=E, padx=10, pady=5)
#btnDelete.grid(row=6, column=2, sticky=E, padx=10, pady=5)

#for list
color = "#ba6b57"
separator = Canvas(root, height=100, width=520, background=color, relief=SUNKEN)
addHeaders()
DisplayProduct()

root.configure(background='#30475e')
root.mainloop()