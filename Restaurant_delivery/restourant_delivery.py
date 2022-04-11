
"""

Program Restourant with delivery

"""

class Restaurant:
    """
    Create class Restaurant with its own variables.

    """

    def __init__(self, menu, table, employees, delivery, customers):
        self.menu = menu
        self.table = table
        self._employees = employees
        self.delivery = delivery
        self.customers = customers

    @staticmethod
    def get_table_status(condition):
        """
        create method 'get_table_status' for getting information about free place in restaurant
        """
        return f"You did got information about tables and now {condition} "

    def get_table(self):
        """

        method 'get_table' customer get table in restaurant

        """
        print(f"You did got table with number {self.table}")

    @staticmethod
    def show_menu():
        """

        Create method 'show_menu' for watching customers by menu.

        """
        print("You can watch restaurants's menu.")

    @staticmethod
    def catering():
        """

        Create method 'catering' for customers could have had waiter service.

        """
        print("You could have had waiter service.")

    @staticmethod
    def add_customers(name, last_name):
        """
        create method 'add_employeis'
        """
        return f"The customer was added ai list with name {name} {last_name}"

    @staticmethod
    def delivery_food(time):
        """
        create method 'delivery_food' for this restaurant
        """
        print(f"This foods will be delivered for customers, wait {time} minutes.")

    @staticmethod
    def add_employees(name):
        """
        create method 'add_employees'
        """
        return f"A new employee named {name}"

    @staticmethod
    def dismiss_employees(name):
        """
        create method 'dismiss_employees'
        """
        return f"An employee {name} was dismiss"


class Employees:
    """"
    Create class Employees which inherited from Restaurant.
    This class consist with parameters: name,age, position and salary.
    """

    def __init__(self, name, age, position):
        self._name = name
        self.age = age
        self._position = position
        self._salary = None

    def __str__(self):
        information = f"name = {self._name}, age = {self.age}, position = {self._position}"
        return information

    def work_day(self, _name):
        """
        Create method work_day with parameters _name.
        """
        self._name = _name
        print(f"{self._name} today is working")

    def day_of(self, _name):
        """
        Create method day_of with parameters _name.
        """
        self._name = _name
        print(f"{self._name} is day of.")

    def get_salary(self, value, _name):
        """
        Create method get_salary with parameters _name and value.
        """
        self._salary = value
        self._name = _name
        return print(f"{value} it is salary for this employee {self._name}")

class Waiter(Employees):
    """
    Create class Waiter which inherited from class Employees.
    This class consist with parameters from Employees class and have own parameters.
    """

    def __init__(self, name, age, position, table, order, food, bill):
        super().__init__(name, age, position)
        self.table = table
        self.order = order
        self.food = food
        self.bill = bill
        self.condition = None

    def table_info(self, condition):
        """
        Create method table_info with parameter condition.
        """
        self.condition = condition
        if condition == "fully":
            print(f"Now not free place Restaurant {self.condition}. Sorry!")
        else:
            print("I will show you your table.")

    @staticmethod
    def accept_order():
        """
        Create method accept_order.
        """
        print("Waiter accept your order")

    def complete_an_order(self, order):
        """
        Create method complete_an_order with parameters order.
        """
        self.order = order
        print(f"Waiter was completed an order with number {self.order}")

    def get_bill(self, order, bill):
        """
        Create method get_bill with parameters order and bill.
        """
        self.order = order
        self.bill = bill
        print(f"Waiter calculate order with number {self.order} and you need pay {self.bill}$")

    def get_order_delivery(self, order):
        """
        Create method get_delivery_order with parameters order.
        """
        self.order = order
        print(f"Waiter accepted order for delivery with number {self.order}")

    def take_order_delivery(self, order):
        """
        Create method take_order_delivery with parameters order.
        """
        self.order = order
        print(f"Number {self.order} was gave to the courier.")


class Kitchen(Employees):
    """
    Create class Kitchen which inherited from class Employees.
    This class consist with parameters from Employees class and have own parameters.
    """

    def __init__(self, name, age, position, menu):
        super().__init__(name, age, position)
        self.menu = menu

    @staticmethod
    def cooking_food():
        """
        Create method cooking_food.
        """
        print("The kitchen doing food for orders.")

    def update_menu(self, menu):
        """
        Create method update_menu with parameter menu.
        """
        self.menu = menu
        if menu == "new":
            print(f"Our menu {self.menu} and it was updated.")
        else:
            print("Our menu remains the same.")

    @staticmethod
    def give_food_to_the_waiter():
        """
        Create method give_food_to_the_waiter.
        """
        print("Kitchen give order to the waiter.")


class Customers:
    """
    Create class Customers with own parameters: customer_id, customer_name, customer_order.
    """

    def __init__(self, customer_id, customer_name, customer_order):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_order = customer_order

    def __str__(self):
        information_about_customer = f"name_customer = {self.customer_name},\
         customer = {self.customer_id}, order = {self.customer_order}"
        return information_about_customer

    @staticmethod
    def pay_for_on_order(order, food, bill):
        """
        Create pay_for_on_order with parameters: order, food, bill.
        """
        print(f"Customer pay your order number {order} and sum cash for {food} \
        equel {bill} hrivens")


class CustomerDelivery:
    """
    Create class CustomerDelivery with own parameters: customer_address, customer_name,
    customer_phone, customer_order.
    """
    def __init__(self, customer_name, customer_address, customer_order, customer_phone):
        self.customer_address = customer_address
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_order = customer_order
        self.bill = None

    def place_on_order(self, customer_phone):
        """
        Create method place_on_order_delivery with parameter customer_phone.
        """
        self.customer_phone = customer_phone
        print(f"Customer make an order by phone number {self.customer_phone}")

    def get_on_order_status(self, customer_order, customer_name, customer_address):
        """
        Create method get_order_status with parameters: customer_order, customer_name,
    customer_address.
        """
        self.customer_address = customer_address
        self.customer_name = customer_name
        self.customer_order = customer_order
        print(f"Number order {self.customer_order} now going to {self.customer_address} \
for customer with named {self.customer_name}")

    def get_order(self, customer_name, customer_order):
        """
        Create method get_order with parameters: customer_order, customer_name.
        """
        self.customer_name = customer_name
        self.customer_order = customer_order
        print(f"Customer named {self.customer_name} get your order with number\
{self.customer_order}")

    def pay_on_for_order(self, customer_name, customer_order, customer_address, bill):
        """
        Create method pay_on_for_order with parameters: customer_order,
    customer_name,customer_address, bill.
        """
        self.customer_name = customer_name
        self.customer_order = customer_order
        self.customer_address = customer_address
        self.bill = bill
        print(f"Order number {self.customer_order} was paid {self.customer_name}\
        by address {self.customer_address}. Sum for paid equel {self.bill} hrivents.")


class Delivery(CustomerDelivery):
    """
    Create class Delivery which inherited CustomerDelivery.
    """

    def get_order_delivery(self, customer_order):
        """
        Create method get_order_delivery with parameter customer_order.
        """
        self.customer_order = customer_order
        print(f"A curier get order number {customer_order}")


class Order():
    """
    Create class Order this own parameters.
    """
    def __init__(self, table, order, food, condition):
        self.table = table
        self.order = order
        self.food = food
        self.condition = condition

    def del_order(self, order):
        """
        Create method get_order with parameter order.
        """
        self.order = order
        print(f"Order number {self.order} is done, can delete")

    def get_status_order(self, order, food, condition):
        """
        Create method get_status_order with parameters: order, food, condition.
        """
        self.order = order
        self.food = food
        self.condition = condition
        print(f"Your order {self.order} consist with {self.food} now {self.condition}.")

    @staticmethod
    def get_order():
        """
        Create method get_order with parameter.
        """
        print("You your order.")

class Bill():
    """
    Create class Bill which used class Waiter.
    """

    def __init__(self, order, bill):
        self.order = order
        self.bill = bill

    @staticmethod
    def calculate_bill():
        """
        Create method calculate_bill.
        """
        print("Your order now is calculating.")

    def get_bill(self, order, bill):
        """
        Create method get_bill with parameters: order, bill.
        """
        self.order = order
        self.bill = bill
        print(f"Your order with number {self.order} and sum for pay {self,bill} hrivents.")

    def pay_a_bill(self, bill):
        """
        Create method pay_a_bill with parameter bill.
        """
        self.bill = bill
        print(f"Payable is {self.bill} hrivents")


class Table():
    """
    Create class Table with own parameters.
    """

    def __init__(self, table_info, table):
        self.table_info = table_info
        self.table = table

    def get_table_info(self, table_info):
        """
        Create method get_table_info with parameter table_info.
        """
        self.table_info = table_info
        print(f"Now at restourant {self.table_info}.")

    @staticmethod
    def set_table():
        """
        Create method set_table.
        """
        print("Waiter prepare your table.")

    def get_table(self, table):
        """
        Create method get_table with parameter table.
        """
        self.table = table
        print(f'You get table with number {self.table}')


class Menu():
    """
    Create class Menu.
    """
    def __init__(self, menu):
        self.menu = menu

    @staticmethod
    def show_menu():
        """
        Create method show_menu.
        """
        print("Customer watching menu.")

    @staticmethod
    def get_menu():
        """
        Create method get_menu.
        """
        print("Customer got menu and making order.")

    def update_menu(self, menu):
        """
        Create method update_menu with parameter menu.
        """
        self.menu = menu
        print(f"Now at our restaurant {self.menu} menu.")


# rest = Restaurant(None, None, None, None, None,)
# rest.table = 10
# print(rest.get_table_status("fully"))
# rest.get_table()
# staff = rest.add_employees("Nick")
# print(staff)
# staff_del = rest.dismiss_employees("Andy")
# print(staff_del)
# print(rest.add_customers("Will", "Smith"))
# rest.delivery_food(30)

# staff1 = Employees("Nikky", 38, "shef")
# print(staff1._name, staff1.age, staff1._position)
# staff1.work_day("Vally")
# staff1.get_salary(3000, "Andry")

# waiter = Waiter("Sam", 26, "waiter", 11, 520, "beef with potato", 450)
# waiter.get_table()
# !!!!! waiter.table_info("We have free tables")
# waiter.accept_order()
# waiter.complete_an_order(137)
# waiter.bill = 15
# waiter.get_bill(137, 15)

kit = Kitchen("Zak", 41, "shef", "old")
print(kit.__str__())
print(waiter.__str__())
kit.show_menu()
kit.update_menu("old")

# cust1 = Customers(15, 534, "Napoleon", 120, 8, "Oleh Vinik", 534)
# print(cust1.__str__())
# cust1.show_menu()
# cust1.pay_for_on_order(534, "Chicken soup", 100)

# cust_del = CustomerDelivery("Symskya 51", "Bladimir", "095-123-45-55", 579)
# cust_del.get_order("Vladimir",579)
# cust_del.pay_on_for_oerder("Semen", 190, "Khrecshatik 32", 560)
# cust_del.get_on_order_status(890, "Marina", "Olma 128")
#
# delivery = Delivery("Frunze 87", "Mitya", "098-456-32-12", 1290)
# delivery.get_on_order_status(1290, "Mitya", "Frunze 87")

# order = Order(30, 1720, "ice-cream, cola, pizza", "Done")
# order.get_status_order(237, "Cesar, vine, cake", "not ready yet")
# order.get_order()
# bill = Bill(510, 1000)
# bill.calculate_bill()
# bill.get_bill(510, 1100)
# bill.pay_a_bill(1000)

table_name = Table("have free place", 41)
