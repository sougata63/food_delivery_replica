import json
class Restaurant:

    store=0
    def __init__(self, name):
        self.restro_name = name
        self.food = {}
        self.food_ID = len(self.food) + 1
        self.user_details = {}
        self.ordered_item = []
        self.amt=0

    # Admin functionalities

    def admin_details(self):
        with open("admin.json") as f:
            data = json.load(f)
        name = input("Enter Admin name : ").upper()
        password = input("Enter Admin Password : ")

        if name == data["name"] and password == data["password"]:
            print("Admin Logged in SuccessFully....")
            Restaurant.store=True
        else: 
            print("Incorrect Admin Details")
            Restaurant.store=False


    def add_food_item(self):
            try:
                name = input("Enter the food name : ")
                quantity = float(input("Enter the quantity in values only : "))
                price = float(input("Enter the price in Rs only : "))
                discount = float(input("Enter the discount in Rs only : "))
                stock = float(input("Enter the available stock in values only : "))
                food_item = {"Item Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
                self.food_ID = len(self.food) + 1
                self.food[self.food_ID] = food_item
                print("\n!! Food Item added successfully !!\n")
                print("Newly Added items :", self.food, "\n")
            except Exception as e:
                print("\n!! Something went wrong please try again !!\n")

    def edit_food_item(self):
        try:
            x = int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y = input("Enter the number only : ")
                if y == "1":
                    self.food[x]["Item Name"] = input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y == "2":
                    self.food[x]["Quantity"] = float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y == "3":
                    self.food[x]["Price"] = float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y == "4":
                    self.food[x]["Discount"] = float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y == "5":
                    self.food[x]["Stock"] = float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")

    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food) != 0:
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("--> Sorry No Food Items is Added <--\n")

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x = int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n", self.food)
            else:
                print("---> Incorrect Food ID\n <---")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")

    # user functionalities

    def user_register(self):
        try:
            while True:
                user_name = input("Enter your full name : ")
                a=False    
                while a==False:
                    phone_no = input("Enter your 10 digit phone number : ")
                    if len(phone_no)==10:
                        a=True
                        break
                    else:
                        print('please enter a phone no with 10 digit')
                b=False    
                while b==False:
                    email = input("Enter your email id : ")
                    if '@' in email:
                        a=True
                        break
                    else:
                        print('please enter a email id which contains @')
                
                password = input("Enter your password : ")
                address = input("Enter your address with area PIN code ")
                self.user_details = {"User Name": user_name, "Phone No.": phone_no, "Email_ID": email,
                                     "Password": password, "Address": address}
                print("\n!! Your Account is Created Successfully !!\n")
                print(f"Welcome TO {self.restro_name} Restaurant\n")
                print("User Details : ")
                for i in self.user_details:
                    print(i, ":", self.user_details[i])
                break

        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ")

    def user_login(self):
        try:
            while True:
                print(f"Welcome TO {self.restro_name} Restaurant\n\n")
                email = input("Enter Your Email ID : ")
                pas = input("Enter Your Password : ")
                if len(self.user_details) != 0:
                    if email == self.user_details["Email_ID"] and pas == self.user_details["Password"]:
                        print("\n!! Login successfully !!")
                        while True:
                            print("\nEnter the Below Options\n")
                            print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                            z = input('enter a choice : ')
                            if z == "1":
                                self.place_order()
                            elif z == "2":
                                self.ordered_history()
                            elif z == "3":
                                self.update_details()
                            elif z == "4":
                                break
                            else:
                                print("invalid Number")
                    else:
                        print("\n!! Incorrect Email or Password!!\n")
                else:
                    print("\n! There is no Account with this Email ID !\n\n!! Please Create Your Account First!!\n")
                    break
                break
        except Exception as e:
            print("\n error in log_in")

    def place_order(self):
        try:
            if len(self.food) != 0:
                menu = []
                for items in self.food:
                    menu.append([self.food[items]["Item Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
                for i in menu:
                    print(i)
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x = input('enter a choice : ')
                    if x == "1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y = input().split(",")
                        for i in y:
                            z = int(i)
                            if z <= len(menu):
                                print (f"{self.food[z]['Item Name']}  ---------->  stock  : {self.food[z]['Stock']}")
                                if self.food[z]['Stock']>=self.food[z]['Quantity']:
                                    self.ordered_item.append(menu[z - 1])
                                    self.food[z]['Stock']-=self.food[z]["Quantity"]
                                    self.amt+=self.food[z]["Quantity"]*((self.food[z]["Price"])-(self.food[z]["Discount"]))
                                else:
                                    print(f'{self.food[z]["Item Name"]} is out of stock as your order amount {self.food[z]["Quantity"]} is more than stock ')
                                    
                            else:
                                 print("We Don't have this Food Item : ", z)
                    
                        print('List of food item you ordered : \n')
                        for j in self.ordered_item:
                            print(j)
                        print(f'Total amount is {self.amt}')
                        
                    elif x == "2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")

        except Exception as e:
            print("\n something wrong in placing the order")

    def ordered_history(self):
        print("\nList of Previous ordered : ")
        for i in self.ordered_item:
            print(i)
        print(f'Total amount is {self.amt}')

    def update_details(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x = input('enter a choice : ')
                if x == "1":
                    self.user_details["User Name"] = input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "2":
                    self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")
                elif x == "3":
                    self.user_details["Email_ID"] = input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")

                elif x == "4":
                    self.user_details["Password"] = input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "5":
                    self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")

                elif x == "6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")

                if x in ["1", "2", "3", '4', "5"]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!")     
try:
    def main():
        FD = Restaurant("FOOD HUB")
        print(f"__/\__  Welcome To {FD.restro_name}  __/\__\n")
        print("------------------------------------------------------------")
        print("\nHello and Welcome \nWhat do you want to order in my Restuarant ?")
        print("--------------------------------------------------------------------\n")

        while True:
            print("1. Admin\n2. User\n3. Exit\n")
            x = input('enter a choice : ')
            if x == "1":
                FD.admin_details()
                while Restaurant.store==True:
                    print(
                     "1. Add New Food Items\n2. Edit Food Items\n3. View Food Items \n4. Delete Food Items\n5. Exit")
                    y = input('ADMIN enter a choice : ')
                    if y == "1":
                        FD.add_food_item()
                    elif y == "2":
                        FD.edit_food_item()
                    elif y == "3":
                        FD.view_food_item()
                    elif y == "4":
                        FD.delete_food_item()
                    elif y == "5":
                        break
                    else:
                        print("Invalid Number")
            elif x == "2":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y = input()
                    if y == "1":
                        FD.user_register()
                    elif y == "2":
                        FD.user_login()
                    elif y == "3":
                        break
                    else:
                        print("\nInvalid Number ")
            
            elif x == "3":
                break
            else:
                print("Invalid Number")
except Exception as e:
        print("something went wrong please give input carefully")
    

# calling the main function
if __name__ == '__main__':
    main()