from utilities.db.db_manager import dbManager


class UserDataPuller:
    def pulldata(self, user_id):
        temp = dbManager.fetch("SELECT * FROM customers WHERE Customer_ID=%s", (user_id,))[0]
        user = {
            'email': temp.Email,
            'password': temp.Password,
            'first_name': temp.First_Name,
            'last_name': temp.Last_Name,
            'phone_number': temp.Phone_Number,
            'username': temp.username
        }
        return user

    def userscount(self,):
        users = dbManager.fetch("SELECT Customer_ID FROM customers")
        res = 0
        for user in users:
            res = res + 1
        return res

    def insert(self, email, password, first_name, last_name, phone_number, username):
        if userDataPuller.checkUsernameexist(username):
            return False
        else:
            insert = dbManager.commit("""INSERT INTO customers 
                (Customer_ID, Email, Password, First_Name, Last_Name, Phone_Number, username) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, (userDataPuller.userscount()+1, email, password, first_name, last_name, phone_number, username))
            return insert

    def update(self, email, password, first_name, last_name, phone_number, user_id):
        querysucsses = dbManager.commit("""update customers 
        set Email = "%s", Password = "%s", First_Name = "%s", 
        Last_Name = "%s", Phone_Number = "%s"  
        where customer_ID =  %s ;
        """ % (email, password, first_name, last_name, phone_number, user_id))
        return  querysucsses

    def checkUsernameNPassword(self, username, password):
        user = dbManager.fetch("SELECT * FROM customers WHERE username=%s AND password=%s", (username, password))
        return user

    def checkUsernameexist(self, username):
        user = dbManager.fetch("SELECT * FROM customers WHERE username=%s", (username,))
        return user

    def Summary(self, customer_id):
        res = dbManager.fetch("""
        select (select count(*) from orders where orders.customer_ID=c.customer_ID) as 'Total_Orders',
        (select sum(p.price) from products as p join orders as o on p.product_id=o.product_ID where o.customer_ID=c.customer_ID) as 'Total_cost',
        (select count(*) from wish_lists where wish_lists.customer_ID=c.customer_ID) as 'Total_Favorited'
        from customers as c
        where c.customer_ID= %s
        group by c.customer_ID
        """ % (customer_id,))
        return res[0]






# Creates an instance for the DBManager class for export.
userDataPuller = UserDataPuller()