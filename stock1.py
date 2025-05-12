import tkinter as tk
from tkinter import messagebox, Label
from PIL import Image, ImageTk  # Importing for image handling
import pandas as pd

# Define window dimensions
window_width = 500
window_height = 500

# Main window
root = tk.Tk()
root.title("Stock Management System")
root.geometry(f"{window_width}x{window_height}")

# Load and resize the background image
image_path = "stock.jpg"
image = Image.open(image_path)
image_resized = image.resize((1600, 800))  # Resize to fit the window
image_tk = ImageTk.PhotoImage(image_resized)

# Create a label to display the background image
background_label = tk.Label(root, image=image_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place the label to cover the full window

# Heading with a white background for contrast and padding
heading = Label(root, text="GUI-Based Stock Market and Control System", font=("Helvetica", 24, "bold"),
                bg="orange", fg="black", padx=10, pady=10)
heading.pack(pady=20)  # Add some padding around the heading

# In-memory stock data
stock_data = {}

# Add stock functionality
def add_stock():
    def save_item():
        name = entry_name.get()
        quantity = entry_quantity.get()
        price = entry_price.get()
        supplier = entry_supplier.get()

        if name and quantity.isdigit() and price and supplier:
            stock_id = len(stock_data) + 1
            stock_data[stock_id] = {
                "name": name,
                "quantity": int(quantity),
                "price": float(price),
                "supplier": supplier
            }
            messagebox.showinfo("Success", "Stock item added successfully!")
            add_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields with correct values.")

    add_window = tk.Toplevel(root)
    add_window.title("Add Stock Item")
    add_window.geometry("300x250")

    tk.Label(add_window, text="Item Name:").grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=0, column=1)

    tk.Label(add_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
    entry_quantity = tk.Entry(add_window)
    entry_quantity.grid(row=1, column=1)

    tk.Label(add_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
    entry_price = tk.Entry(add_window)
    entry_price.grid(row=2, column=1)

    tk.Label(add_window, text="Supplier:").grid(row=3, column=0, padx=10, pady=10)
    entry_supplier = tk.Entry(add_window)
    entry_supplier.grid(row=3, column=1)

    tk.Button(add_window, text="Save", command=save_item).grid(row=4, column=1, pady=10)

# View stock functionality
def view_stock():
    view_window = tk.Toplevel(root)
    view_window.title("Stock Levels")
    view_window.geometry("400x300")

    row_num = 0
    for stock_id, record in stock_data.items():
        row_num += 1
        tk.Label(view_window, text=f"ID: {stock_id} - {record['name']} (Qty: {record['quantity']}) - ${record['price']:.2f}").grid(row=row_num, column=0)

# Update stock functionality
def update_stock():
    def save_update():
        item_id = entry_id.get()
        new_quantity = entry_quantity.get()
        new_price = entry_price.get()

        if item_id.isdigit() and int(item_id) in stock_data and new_quantity.isdigit() and new_price:
            stock_data[int(item_id)]["quantity"] = int(new_quantity)
            stock_data[int(item_id)]["price"] = float(new_price)
            messagebox.showinfo("Success", "Stock item updated successfully!")
            update_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter valid values for all fields.")

    update_window = tk.Toplevel(root)
    update_window.title("Update Stock Item")
    update_window.geometry("300x200")

    tk.Label(update_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
    entry_id = tk.Entry(update_window)
    entry_id.grid(row=0, column=1)

    tk.Label(update_window, text="New Quantity:").grid(row=1, column=0, padx=10, pady=10)
    entry_quantity = tk.Entry(update_window)
    entry_quantity.grid(row=1, column=1)

    tk.Label(update_window, text="New Price:").grid(row=2, column=0, padx=10, pady=10)
    entry_price = tk.Entry(update_window)
    entry_price.grid(row=2, column=1)

    tk.Button(update_window, text="Save", command=save_update).grid(row=3, column=1, pady=10)

# Delete stock functionality
def delete_stock():
    def delete_item():
        item_id = entry_id.get()
        if item_id.isdigit() and int(item_id) in stock_data:
            del stock_data[int(item_id)]
            messagebox.showinfo("Success", "Stock item deleted successfully!")
            delete_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid item ID.")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Stock Item")
    delete_window.geometry("250x150")

    tk.Label(delete_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
    entry_id = tk.Entry(delete_window)
    entry_id.grid(row=0, column=1)

    tk.Button(delete_window, text="Delete", command=delete_item).grid(row=1, column=1, pady=10)

# Generate low stock report
def generate_report():
    low_stock_items = {stock_id: record for stock_id, record in stock_data.items() if record["quantity"] < 10}

    if low_stock_items:
        df = pd.DataFrame.from_dict(low_stock_items, orient='index')
        df.to_csv('low_stock_report.csv', index=False)
        messagebox.showinfo("Report Generated", "Low stock report saved as low_stock_report.csv")
    else:
        messagebox.showinfo("No Low Stock", "There are no items with low stock levels.")

# Main menu buttons - pack on top of the image
tk.Button(root, text="Add Stock", command=add_stock, width=20).pack(pady=10)
tk.Button(root, text="View Stock", command=view_stock, width=20).pack(pady=10)
tk.Button(root, text="Update Stock", command=update_stock, width=20).pack(pady=10)
tk.Button(root, text="Delete Stock", command=delete_stock, width=20).pack(pady=10)
tk.Button(root, text="Generate Low Stock Report", command=generate_report, width=20).pack(pady=10)

# Run GUI
root.mainloop()

#
#

#
# import tkinter as tk
# from tkinter import messagebox, Label
# from PIL import Image, ImageTk
# import pandas as pd
# import mysql.connector
#
# # MySQL connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Root1234",  # 🔐 Replace with your actual MySQL password
#     database="stock_db"
# )
# cursor = conn.cursor()
#
# # Define window dimensions
# window_width = 500
# window_height = 500
#
# # Main window
# root = tk.Tk()
# root.title("Stock Management System")
# root.geometry(f"{window_width}x{window_height}")
#
# # Background image
# image_path = "stock.jpg"
# image = Image.open(image_path)
# image_resized = image.resize((1600, 800))
# image_tk = ImageTk.PhotoImage(image_resized)
# background_label = tk.Label(root, image=image_tk)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# heading = Label(root, text="GUI-Based Stock Market and Control System", font=("Helvetica", 20, "bold"),
#                 bg="orange", fg="black", padx=10, pady=10)
# heading.pack(pady=20)
#
# # Add stock
# def add_stock():
#     def save_item():
#         name = entry_name.get()
#         quantity = entry_quantity.get()
#         price = entry_price.get()
#         supplier = entry_supplier.get()
#
#         if name and quantity.isdigit() and price and supplier:
#             cursor.execute("INSERT INTO stock_items (name, quantity, price, supplier) VALUES (%s, %s, %s, %s)",
#                            (name, int(quantity), float(price), supplier))
#             conn.commit()
#             messagebox.showinfo("Success", "Stock item added successfully!")
#             add_window.destroy()
#         else:
#             messagebox.showwarning("Input Error", "Please fill all fields correctly.")
#
#     add_window = tk.Toplevel(root)
#     add_window.title("Add Stock Item")
#     add_window.geometry("300x250")
#
#     tk.Label(add_window, text="Item Name:").grid(row=0, column=0, padx=10, pady=10)
#     entry_name = tk.Entry(add_window)
#     entry_name.grid(row=0, column=1)
#
#     tk.Label(add_window, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
#     entry_quantity = tk.Entry(add_window)
#     entry_quantity.grid(row=1, column=1)
#
#     tk.Label(add_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
#     entry_price = tk.Entry(add_window)
#     entry_price.grid(row=2, column=1)
#
#     tk.Label(add_window, text="Supplier:").grid(row=3, column=0, padx=10, pady=10)
#     entry_supplier = tk.Entry(add_window)
#     entry_supplier.grid(row=3, column=1)
#
#     tk.Button(add_window, text="Save", command=save_item).grid(row=4, column=1, pady=10)
#
# # View stock
# def view_stock():
#     view_window = tk.Toplevel(root)
#     view_window.title("Stock Levels")
#     view_window.geometry("400x300")
#
#     cursor.execute("SELECT * FROM stock_items")
#     records = cursor.fetchall()
#
#     row_num = 0
#     for record in records:
#         row_num += 1
#         id, name, quantity, price, supplier = record
#         tk.Label(view_window, text=f"ID: {id} - {name} (Qty: {quantity}) - ₹{price:.2f}").grid(row=row_num, column=0)
#
# # Update stock
# def update_stock():
#     def save_update():
#         item_id = entry_id.get()
#         new_quantity = entry_quantity.get()
#         new_price = entry_price.get()
#
#         if item_id.isdigit() and new_quantity.isdigit() and new_price:
#             cursor.execute("UPDATE stock_items SET quantity=%s, price=%s WHERE id=%s",
#                            (int(new_quantity), float(new_price), int(item_id)))
#             conn.commit()
#             messagebox.showinfo("Success", "Stock item updated successfully!")
#             update_window.destroy()
#         else:
#             messagebox.showwarning("Input Error", "Please enter valid values.")
#
#     update_window = tk.Toplevel(root)
#     update_window.title("Update Stock Item")
#     update_window.geometry("300x200")
#
#     tk.Label(update_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
#     entry_id = tk.Entry(update_window)
#     entry_id.grid(row=0, column=1)
#
#     tk.Label(update_window, text="New Quantity:").grid(row=1, column=0, padx=10, pady=10)
#     entry_quantity = tk.Entry(update_window)
#     entry_quantity.grid(row=1, column=1)
#
#     tk.Label(update_window, text="New Price:").grid(row=2, column=0, padx=10, pady=10)
#     entry_price = tk.Entry(update_window)
#     entry_price.grid(row=2, column=1)
#
#     tk.Button(update_window, text="Save", command=save_update).grid(row=3, column=1, pady=10)
#
# # Delete stock
# def delete_stock():
#     def delete_item():
#         item_id = entry_id.get()
#         if item_id.isdigit():
#             cursor.execute("DELETE FROM stock_items WHERE id=%s", (int(item_id),))
#             conn.commit()
#             messagebox.showinfo("Success", "Stock item deleted successfully!")
#             delete_window.destroy()
#         else:
#             messagebox.showwarning("Input Error", "Please enter a valid item ID.")
#
#     delete_window = tk.Toplevel(root)
#     delete_window.title("Delete Stock Item")
#     delete_window.geometry("250x150")
#
#     tk.Label(delete_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
#     entry_id = tk.Entry(delete_window)
#     entry_id.grid(row=0, column=1)
#
#     tk.Button(delete_window, text="Delete", command=delete_item).grid(row=1, column=1, pady=10)
#
# # Generate low stock report
# def generate_report():
#     cursor.execute("SELECT * FROM stock_items WHERE quantity < 10")
#     low_stock_items = cursor.fetchall()
#
#     if low_stock_items:
#         df = pd.DataFrame(low_stock_items, columns=["ID", "Name", "Quantity", "Price", "Supplier"])
#         df.to_csv('low_stock_report.csv', index=False)
#         messagebox.showinfo("Report Generated", "Low stock report saved as low_stock_report.csv")
#     else:
#         messagebox.showinfo("No Low Stock", "There are no items with low stock levels.")
#
# # Menu Buttons
# tk.Button(root, text="Add Stock", command=add_stock, width=20).pack(pady=10)
# tk.Button(root, text="View Stock", command=view_stock, width=20).pack(pady=10)
# tk.Button(root, text="Update Stock", command=update_stock, width=20).pack(pady=10)
# tk.Button(root, text="Delete Stock", command=delete_stock, width=20).pack(pady=10)
# tk.Button(root, text="Generate Low Stock Report", command=generate_report, width=25).pack(pady=10)
#
# # Start GUI
# root.mainloop()

