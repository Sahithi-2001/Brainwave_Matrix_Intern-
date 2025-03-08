import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

class InventoryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x500")
        self.root.configure(bg="#D5DBDB")  # Light professional background with a soft gray tone
        
        self.users = {"admin": "password"}  # Default user
        self.products = {}
        
        self.show_login()
        
    def show_login(self):
        self.login_frame = tk.Frame(self.root, bg="#D5DBDB")
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(self.login_frame, text="Username:", bg="#D5DBDB", fg="black").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.login_frame, text="Password:", bg="#D5DBDB", fg="black").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(self.login_frame, text="Login", command=self.login, bg="#2ECC71", fg="black").grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')
        tk.Button(self.login_frame, text="Register", command=self.show_register, bg="#3498DB", fg="black").grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
    
    def show_register(self):
        username = simpledialog.askstring("Register", "Enter new username:")
        if not username:
            return
        password = simpledialog.askstring("Register", "Enter new password:", show="*")
        if not password:
            return
        
        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.users[username] = password
            messagebox.showinfo("Success", "User registered successfully!")
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username] == password:
            self.login_frame.destroy()
            self.create_widgets()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#D5DBDB")
        self.main_frame.pack(pady=20)
        
        tk.Label(self.main_frame, text="Product Name:", bg="#D5DBDB", fg="black").grid(row=0, column=0, padx=10, pady=5)
        self.product_name = tk.Entry(self.main_frame)
        self.product_name.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.main_frame, text="Quantity:", bg="#D5DBDB", fg="black").grid(row=1, column=0, padx=10, pady=5)
        self.product_quantity = tk.Entry(self.main_frame)
        self.product_quantity.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.main_frame, text="Price:", bg="#D5DBDB", fg="black").grid(row=2, column=0, padx=10, pady=5)
        self.product_price = tk.Entry(self.main_frame)
        self.product_price.grid(row=2, column=1, padx=10, pady=5)
        
        button_frame = tk.Frame(self.main_frame, bg="#D5DBDB")
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(button_frame, text="Add Product", command=self.add_product, bg="#2ECC71", fg="black").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Product", command=self.delete_product, bg="#E74C3C", fg="black").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Product", command=self.edit_product, bg="#F1C40F", fg="black").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Generate Report", command=self.generate_report, bg="#9B59B6", fg="black").pack(side=tk.LEFT, padx=5)
        
        self.tree = ttk.Treeview(self.main_frame, columns=("Name", "Quantity", "Price"), show='headings')
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    def add_product(self):
        name = self.product_name.get()
        quantity = self.product_quantity.get()
        price = self.product_price.get()
        
        if name and quantity and price:
            self.products[name] = (quantity, price)
            self.tree.insert("", "end", values=(name, quantity, price))
        else:
            messagebox.showerror("Error", "All fields must be filled!")
    
    def edit_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to edit")
            return
        item_values = self.tree.item(selected_item, 'values')
        name = item_values[0]
        new_quantity = simpledialog.askstring("Edit Quantity", "Enter new quantity:", initialvalue=item_values[1])
        new_price = simpledialog.askstring("Edit Price", "Enter new price:", initialvalue=item_values[2])
        self.products[name] = (new_quantity, new_price)
        self.tree.item(selected_item, values=(name, new_quantity, new_price))
    
    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to delete")
            return
        item_values = self.tree.item(selected_item, 'values')
        name = item_values[0]
        if name in self.products:
            del self.products[name]
        self.tree.delete(selected_item)
    
    def generate_report(self):
        report = "Inventory Report:\n\n"
        for name, (quantity, price) in self.products.items():
            report += f"{name}: Quantity = {quantity}, Price = {price}\n"
        messagebox.showinfo("Inventory Report", report)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagement(root)
    root.mainloop()
