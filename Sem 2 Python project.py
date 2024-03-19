import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Lewis Manor Bistro")
        self.root.geometry("1000x1000")

        # Load the image file
        self.bg_image = tk.PhotoImage(file="C:/Users/celes/Desktop/background_image.png")
        # Create a Label widget to display the background image
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)  # Set label size to fill the window
        
        self.customer_name = tk.StringVar()
        self.customer_contact = tk.StringVar()
        self.payment_mode = tk.StringVar()  # Variable to store payment mode
        self.payment_info = tk.StringVar()  # Variable to store payment info (UPI ID or card number)
        self.selected_time = tk.StringVar()  # Variable to store selected time
        self.create_registration_page() # Calls the create_registration_page method to create the registration page


    def create_registration_page(self):
        # Creates a frame for the registration page
        registration_frame = tk.Frame(self.root)
        registration_frame.pack(padx=30, pady=30, side=tk.LEFT)
        # Creates and display the title label
        title_label = tk.Label(registration_frame, text="Lewis Manor Bistro", font=("Helvetica", 18, "bold"))
        title_label.grid(row=0, columnspan=2, padx=5, pady=5)

        # Creates and display the name label and entry field
        name_label = tk.Label(registration_frame, text="Name:")
        name_label.grid(row=1, column=0, padx=5, pady=5)
        name_entry = tk.Entry(registration_frame, textvariable=self.customer_name)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Creates and display the contact label and entry field
        contact_label = tk.Label(registration_frame, text="Contact:")
        contact_label.grid(row=2, column=0, padx=5, pady=5)
        contact_entry = tk.Entry(registration_frame, textvariable=self.customer_contact)
        contact_entry.grid(row=2, column=1, padx=5, pady=5)

        # Creates and display the payment mode label and dropdown
        mode_label = tk.Label(registration_frame, text="Payment Mode:")
        mode_label.grid(row=3, column=0, padx=5, pady=5)
        payment_modes = ["Cash", "Card", "UPI"]
        payment_mode_dropdown = ttk.Combobox(registration_frame, values=payment_modes, textvariable=self.payment_mode)
        payment_mode_dropdown.grid(row=3, column=1, padx=5, pady=5)
        payment_mode_dropdown.bind("<<ComboboxSelected>>", self.show_payment_info_entry)

        # Creates and display the payment info label and entry field (Initially hidden)
        self.payment_info_label = tk.Label(registration_frame, text="Card No./UPI ID:")
        self.payment_info_label.grid(row=4, column=0, padx=5, pady=5)
        self.payment_info_entry = tk.Entry(registration_frame, textvariable=self.payment_info)
        self.payment_info_entry.grid(row=4, column=1, padx=5, pady=5)
        self.payment_info_label.grid_remove()
        self.payment_info_entry.grid_remove()

        # Creates and display the time label and entry field
        time_label = tk.Label(registration_frame, text="Select Time (HH:MM):")
        time_label.grid(row=5, column=0, padx=5, pady=5)
        time_entry = tk.Entry(registration_frame, textvariable=self.selected_time)
        time_entry.grid(row=5, column=1, padx=5, pady=5)

        register_button = tk.Button(registration_frame, text="Register", command=self.go_to_menu_window)
        register_button.grid(row=6, columnspan=2, padx=5, pady=5)

        # Left box for description
        description_frame = tk.Frame(self.root, bg="lightgrey", bd=5)
        description_frame.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.6, anchor="n")

        description_label = tk.Label(description_frame, text="A Glimp's about this Restaurant:", font=("Helvetica", 14, "bold"))
        description_label.pack(side=tk.TOP, padx=10, pady=10)

        description_text = tk.Text(description_frame, wrap=tk.WORD, bg="Magenta",font=("Helvetica", 12), padx=10, pady=10)
        description_text.pack(fill=tk.BOTH, expand=True)

        description_text.insert(tk.END, "Welcome to the Lewis Family Restaurant!\n\n")
        description_text.insert(tk.END,"""Experience the rich tapestry of flavors at Lewis,\nWhere each dish tells a story of tradition,craftsmanship,and culinary excellence.\nIndulge in our delectable creations,\nMeticulously crafted using authentic recipes passed down through generations,\nand embark on a gastronomic journey that tantalizes the taste buds and warms the soul."
\n Note: Please register your details and select the time to proceed to the menu.\n
We serve food as per our respected time\nBREAKFAST  8:00 am To 11:30am\nLUNCH  12:00pm To 15:30pm\nSNACK's 15:40pm TO 19:30pm\nDINNER  19:30pm TO 23:00pm""")
        
    def show_payment_info_entry(self, event):
        # If payment mode is "UPI" or "Card", show the payment info label and entry
        if self.payment_mode.get() == "UPI" or self.payment_mode.get() == "Card":
            self.payment_info_label.grid()
            self.payment_info_entry.grid()
        # If payment mode is not "UPI" or "Card" this will hide the payment info label and entry
        else:
            self.payment_info_label.grid_remove()
            self.payment_info_entry.grid_remove()

    def go_to_menu_window(self):
        # Validate if the customer name and contact are provided
        if not self.customer_name.get().strip() or not self.customer_contact.get().strip():
            messagebox.showwarning("Warning", "Please enter both name and contact.")
            return

        # Validate payment info if payment mode is UPI
        if (self.payment_mode.get() == "UPI" or self.payment_mode.get() == "Card") and not self.payment_info.get().strip():
            messagebox.showwarning("Warning", "Please enter required payment information.")
            return

        # Validate time format
        try:
            datetime.strptime(self.selected_time.get(), "%H:%M")
        except ValueError:
            messagebox.showwarning("Warning", "Invalid time format. Please enter time in HH:MM format.")
            return

        # Destroy registration window
        self.root.destroy()

        # Open menu window
        self.menu_window = tk.Tk()
        self.menu_window.title("Menu")
        self.menu_window.geometry("1500x800")
        menu_system = MenuSystem(self.menu_window, self.selected_time.get(), self.customer_name.get(), self.customer_contact.get(), self.payment_mode.get(), self.payment_info.get())
        self.menu_window.mainloop()

class MenuItem:
    def __init__(self, name, price, description):
        self.name = name #it will store the name of the menu item
        self.price = price# this will store the price of the menu item
        self.description = description # Store the description of the menu item

class MenuSystem:
    def __init__(self, root, selected_time, customer_name, customer_contact, payment_mode, payment_info):
        self.root = root
        self.root.title("Menu")# The title of the root window

        # Stores customer information 
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.payment_mode = payment_mode
        self.payment_info = payment_info
        self.selected_time = selected_time  

        # This is to create a canvas and a frame to display menu items
        self.canvas = tk.Canvas(self.root)
        self.menu_frame = tk.Frame(self.canvas)
        # Creates a scrollbar for the canvas
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        # Packs the scrollbar and canvas widgets
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        # Creates a window inside the canvas to hold the menu frame
        self.canvas.create_window((0, 0), window=self.menu_frame, anchor="nw")
        # Bind an event handler to adjust the scroll region of the canvas when the menu frame is resized
        self.menu_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.items = {
            "Breakfast": {
                "Idli": {"price": 40, "description": "Steamed rice cakes served with chutney and sambar."},
                "Poha": {"price": 30, "description": "Flattened rice cooked with onions, peas, and spices."},
                "Upma": {"price": 35, "description": "Semolina cooked with vegetables and seasoned with spices."},
                "Paratha": {"price": 50, "description": "Flaky Indian bread served with yogurt or pickle."},
                "Aloo Puri": {"price": 45, "description": "Fried Indian bread served with spicy potato curry."},
                "Dosa": {"price": 60, "description": "Crispy rice crepe served with chutney and sambar."}, 
                "Vada Pav": {"price": 50, "description": "Spicy potato dumplings served in a bread roll."},
                "Masala Chai": {"price": 20, "description": "Spiced Indian tea served with milk and sugar."},
                "Mojito": {"price": 120, "description": "Refreshing lime and mint drink."},
                "Cold Coffee": {"price": 100, "description": "Chilled coffee with milk and sugar."},
                "Lemonade": {"price": 80, "description": "Sweet and tangy lemon-flavored drink."},
                "Filter Coffee": {"price": 40, "description": "South Indian style coffee made with freshly ground coffee beans and boiled milk, served hot."},
                "Cappuccino": {"price": 50, "description": "Espresso coffee topped with equal parts of steamed milk foam and hot milk, sprinkled with cocoa powder."},
                "Café Latte": {"price": 45, "description": "Espresso coffee with steamed milk and a small amount of milk foam on top."},
                "Espresso": {"price": 30, "description": "Strong black coffee made by forcing steam through finely-ground coffee beans."},
                "Americano": {"price": 40, "description": "Espresso coffee diluted with hot water, resulting in a similar strength to traditional brewed coffee."},
            },
            "Lunch": {
                "Chicken Biryani": {"price": 180, "description": "Fragrant basmati rice cooked with succulent chicken pieces and aromatic spices."},
                "Butter Chicken": {"price": 200, "description": "Tender chicken pieces cooked in a creamy tomato-based sauce with butter and spices."},
                "Chicken Tikka Masala": {"price": 190, "description": "Grilled chicken tikka cooked in a rich and flavorful tomato-based gravy."},
                "Chicken Korma": {"price": 180, "description": "Chicken pieces simmered in a creamy, mildly-spiced gravy with nuts and yogurt."},
                "Tandoori Chicken": {"price": 210, "description": "Marinated chicken drumsticks grilled to perfection in a traditional tandoor oven."},
                "Mutton Rogan Josh": {"price": 220, "description": "Tender pieces of mutton cooked in a rich and aromatic gravy with traditional Kashmiri spices."},
                "Mutton Curry": {"price": 200, "description": "Mutton pieces cooked in a flavorful gravy with onions, tomatoes, and spices."},
                "Mutton Biryani": {"price": 230, "description": "Basmati rice cooked with tender mutton pieces and a blend of aromatic spices, served with raita."},
                "Chole Bhature": {"price": 100, "description": "Spicy chickpea curry served with fried bread."},
                "Rajma Chawal": {"price": 90, "description": "Kidney beans curry served with rice."},
                "Paneer Tikka": {"price": 150, "description": "Grilled cottage cheese marinated in spices."},
                "Veg Biryani": {"price": 120, "description": "Fragrant rice cooked with mixed vegetables and spices."},
                "Butter Chicken": {"price": 180, "description": "Chicken cooked in a rich tomato-based buttery sauce."},
                "Thali": {"price": 200, "description": "Assorted Indian meal with rice, bread, curry, and dessert."}, 
                "Fish Curry": {"price": 160, "description": "Fish cooked in a spicy coconut-based gravy."},  
                "Coca-Cola": {"price": 30, "description": "Refreshing carbonated soft drink."},
                "Pepsi": {"price": 30, "description": "Carbonated soft drink with a hint of citrus flavor."},
                "Chocolate Brownie": {"price": 150, "description": "Warm chocolate brownie served with vanilla ice cream."},
                "Cheesecake": {"price": 180, "description": "Creamy cheesecake with fruit topping."},
                "Gulab Jamun": {"price": 120, "description": "Sweet dumplings in sugar syrup."},
                "Rasgulla": {"price": 100, "description": "Soft, spongy balls of cottage cheese in sugar syrup."},
                "Ice Cream Sundae": {"price": 160, "description": "Vanilla ice cream topped with chocolate sauce, nuts, and cherries."},
                "Fruit Tart": {"price": 180, "description": "Buttery pastry crust filled with custard and fresh fruit slices."},
            },
            "Snacks": {
                "Samosa": {"price": 20, "description": "Deep-fried pastry filled with spiced potatoes and peas."},
                "Pakora": {"price": 25, "description": "Assorted vegetables battered and deep-fried."},
                "Paneer Tikka": {"price": 80, "description": "Grilled cottage cheese cubes marinated in spices."},
                "French Fries": {"price": 50, "description": "Crispy potato fries served with ketchup."},
                "Onion Rings": {"price": 60, "description": "Crispy fried onion rings."},
                "Orange Juice": {"price": 90, "description": "Freshly squeezed orange juice."},
                "Apple Juice": {"price": 100, "description": "100% pure apple juice."},
                "Pineapple Juice": {"price": 100, "description": "Refreshing pineapple juice."},
                "Masala Chai": {"price": 20, "description": "Spiced Indian tea served with milk and sugar."},
                "Cold Coffee": {"price": 60, "description": "Chilled coffee made with espresso or instant coffee, milk, sugar, and ice cubes, blended until smooth."},
                "Iced Caramel Macchiato": {"price": 70, "description": "Espresso with cold milk and vanilla syrup, topped with caramel drizzle and ice."},
                "Mocha Frappuccino": {"price": 65, "description": "Blended coffee drink made with espresso, chocolate syrup, milk, and ice, topped with whipped cream."},
                "Affogato": {"price": 80, "description": "A dessert consisting of a scoop of vanilla ice cream topped with a shot of hot espresso."},
                "Irish Coffee": {"price": 80, "description": "Hot coffee cocktail made with Irish whiskey, hot coffee, and sugar, topped with cream."},
            },
            "Dinner": {
                "Chicken 65": {"price": 160, "description": "Spicy and tangy deep-fried chicken appetizer, tossed in a flavorful masala."},
                "Chicken Chettinad": {"price": 190, "description": "Chicken cooked in a spicy and aromatic curry with roasted spices and coconut."},
                "Chicken Malai Tikka": {"price": 180, "description": "Creamy and succulent chicken pieces marinated in a blend of spices and grilled to perfection."},
                "Mutton Kebab": {"price": 220, "description": "Tender mutton pieces marinated in spices and grilled or roasted to perfection."},
                "Mutton Do Pyaza": {"price": 210, "description": "Mutton curry made with onions, tomatoes, and a blend of spices, garnished with fried onions."},
                "Mutton Korma": {"price": 220, "description": "Tender mutton pieces cooked in a rich and creamy gravy with yogurt, nuts, and aromatic spices."},
                "Dal Makhani": {"price": 120, "description": "Creamy lentils slow-cooked with spices and butter."},
                "Paneer Butter Masala": {"price": 150, "description": "Cottage cheese cubes in a creamy tomato-based sauce."},
                "Chicken Curry": {"price": 180, "description": "Chicken cooked in a flavorful gravy."},
                "Veg Pulao": {"price": 100, "description": "Fragrant rice cooked with mixed vegetables."},
                "Naan": {"price": 30, "description": "Soft and fluffy leavened Indian bread."},
                "Veg Hakka Noodles": {"price": 110, "description": "Stir-fried noodles with mixed vegetables in a tangy sauce."},
                "Paneer Fried Rice": {"price": 130, "description": "Fried rice cooked with paneer and vegetables."},
                "Chicken Manchurian": {"price": 160, "description": "Batter-fried chicken in a spicy and tangy sauce."},
                "Garlic Naan": {"price": 40, "description": "Leavened Indian bread flavored with garlic and herbs."},
                "Coca-Cola": {"price": 30, "description": "Refreshing carbonated soft drink."},
                "Pepsi": {"price": 30, "description": "Carbonated soft drink with a hint of citrus flavor."},
                "Chocolate Brownie": {"price": 150, "description": "Warm chocolate brownie served with vanilla ice cream."},
                "Cheesecake": {"price": 180, "description": "Creamy cheesecake with fruit topping."},
                "Gulab Jamun": {"price": 120, "description": "Sweet dumplings in sugar syrup."},
                "Rasgulla": {"price": 100, "description": "Soft, spongy balls of cottage cheese in sugar syrup."},
                "Ice Cream Sundae": {"price": 160, "description": "Vanilla ice cream topped with chocolate sauce, nuts, and cherries."},
                "Fruit Tart": {"price": 180, "description": "Buttery pastry crust filled with custard and fresh fruit slices."},
            }
        }

        self.selected_items = {}  # Dictionary to store selected items and their quantities

        self.create_gui(selected_time)# Calls the create_gui method with the selected_time as an argument

    def create_gui(self, selected_time):
        current_time = datetime.strptime(selected_time, "%H:%M").time()
        # Checks the current time to determine the selected menu
        if current_time >= datetime.strptime("08:00", "%H:%M").time() and current_time <= datetime.strptime("11:30", "%H:%M").time():
            selected_menu = "Breakfast"
        elif current_time >= datetime.strptime("12:00", "%H:%M").time() and current_time <= datetime.strptime("16:00", "%H:%M").time():
            selected_menu = "Lunch"
        elif current_time >= datetime.strptime("16:00", "%H:%M").time() and current_time <= datetime.strptime("19:30", "%H:%M").time():
            selected_menu = "Snacks"
        elif current_time >= datetime.strptime("19:40", "%H:%M").time() and current_time <= datetime.strptime("23:00", "%H:%M").time():
            selected_menu = "Dinner"
         # If the current time doesn't fall within any of the specified ranges, show a message and close the window
        else:
            self.root.destroy()
            messagebox.showinfo("Restaurant Closed", "Sorry, we are closed at this time.")
            return

        # It Creates a labeled frame to display the menu for the selected menu category
        menu_frame = tk.LabelFrame(self.canvas, text=f"Menu for {selected_menu}", bg="cyan")
        menu_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Iterate over each category and its items in the menu
        for category, items in self.items.items(): # Check if the category matches the selected menu
            if category == selected_menu:
                # Creates a label for the category and display it in the menu frame
                category_label = tk.Label(menu_frame, text=category, font=('Helvetica', 14, 'bold'), pady=5)
                category_label.pack(side="top", fill="x")

                for item, details in items.items(): # Create a frame to display each item and its details
                    item_frame = tk.Frame(menu_frame)
                    item_frame.pack(side="top", fill="x", padx=5, pady=5)

                    # Create a label for the item name and display it in the item frame
                    item_label = tk.Label(item_frame, text=item, width=20, anchor="w")
                    item_label.pack(side="left", padx=(0, 10))

                    # Create a label for the item description and display it in the item frame
                    description_label = tk.Label(item_frame, text=details["description"], width=40, anchor="w")
                    description_label.pack(side="left")

                    # Create a label for the item price (converted to Indian Rupees) and display it in the item frame
                    price_label = tk.Label(item_frame, text=self.convert_to_inr(details["price"]), width=10, anchor="e")
                    price_label.pack(side="right")

                    # Create a spinbox for selecting the quantity of the item and display it in the item frame
                    quantity_entry = tk.Spinbox(item_frame, from_=0, to=10, width=5)
                    quantity_entry.pack(side="right")

                    # Store the Spinbox widget in the selected_items dictionary with the item name as key
                    self.selected_items[item] = quantity_entry

        print_bill_button = tk.Button(menu_frame, text="Print Bill", command=lambda: self.print_bill(selected_menu))
        print_bill_button.pack(side="bottom")

        back_button = tk.Button(menu_frame, text="Back to Registration", command=self.go_back_to_registration)
        back_button.pack(side="bottom", pady=10)

    def print_bill(self, selected_menu):
        total_price = 0  # Initialize total price
        bill_content = f"Menu for {selected_menu}:\n\n"

        for item, quantity_entry in self.selected_items.items():
            quantity = int(quantity_entry.get())  # Get the quantity selected for the item
            if quantity > 0:
                # Check if the item exists in the menu for the selected menu category
                if item in self.items[selected_menu]:
                    details = self.items[selected_menu][item]  # Get item details
                    price = details["price"]  # Get item price
                    subtotal = price * quantity  # Calculate subtotal for the item
                    total_price += subtotal  # Add subtotal to total price
                    bill_content += f"{item} - {quantity} - {self.convert_to_inr(subtotal)}\n"  # Add item details to bill
                else:
                    messagebox.showwarning("Warning", f"{item} is not available in the {selected_menu} menu.")
                    return

        if total_price == 0:
            messagebox.showwarning("Warning", "Please select at least one item.")
            return

        # This Concatenate registration information to the bill content
        bill_content += f"\n\nRegistration Information:\nName: {self.customer_name}\nContact: {self.customer_contact}\nPayment Mode: {self.payment_mode}\nPayment Info: {self.payment_info}\nSelected Time: {self.selected_time}\n\n"
        # this Add total amount to the bill content in Indian Rupees format
        bill_content += f"Total Amount: {self.convert_to_inr(total_price)}\n"
        # This Add a closing message to the bill content
        bill_content += "\nThank You for choosing Lewis Manor Bistro! We look forward to serving you again."

        messagebox.showinfo("Bill", bill_content) # Shows bill in a messagebox

        # This Reset bill_content variable to a greeting message
        bill_content = "GREETING'S USER'S"
        
        # Creates a custom dialog box with message and feedback button
        feedback = messagebox.askyesno("Bill", bill_content + "\n\nWould you like to provide feedback?")

        # Check if the user wants to provide feedback
        if feedback:
            self.open_feedback_form()


    def open_feedback_form(self):
        # Creates and display a feedback form
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("Feedback Form")# Set the title of the feedback form window
        
        # Creates a label prompting the user to provide feedback and display it in the feedback window
        feedback_label = tk.Label(feedback_window, text="Please provide your feedback:")
        feedback_label.pack()

        # Creates an entry widget for the user to input feedback and display it in the feedback window
        feedback_entry = tk.Entry(feedback_window, font=("Arial", 14), width=50)
        feedback_entry.pack()

        # Creates a submit button to close the feedback window when clicked and display it in the feedback window
        submit_button = tk.Button(feedback_window, text="Submit", command=feedback_window.destroy)
        submit_button.pack()

        
    def go_back_to_registration(self):
        self.root.destroy()
        root = tk.Tk()# Creates a new tkinter window
        restaurant_system = RestaurantManagementSystem(root)# Creates an instance of the RestaurantManagementSystem class with the new tkinter window
        # Sets customer information in the new instance
        restaurant_system.customer_name.set(self.customer_name)
        restaurant_system.customer_contact.set(self.customer_contact)
        restaurant_system.payment_mode.set(self.payment_mode)
        restaurant_system.payment_info.set(self.payment_info)

    @staticmethod
    def convert_to_inr(amount):
        return "₹" + str(amount)


def main():
    root = tk.Tk()
    restaurant_system = RestaurantManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
