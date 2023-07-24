"""
    SQl
    create table Customer(cid text primary key auto_increment, name text, phone text, email text)

    describe Customer;
    insert into customer values(null, 'John', '+91 99853 23110', 'john@example.com');
"""
import mysql.connector as db


class Customer:

    def __init__(self):
        self.name = input("Enter Customer name:")
        self.phone = input("Enter Customer phone:")
        self.email = input("Enter Customer email:")


def main():
    customer = Customer()
    print(vars(customer))
    # Database Connectivity
    # Step 1 : to create connection with db
    connection = db.connect(user='root',
                            password='12345678',
                            host='127.0.0.1',
                            database='gwpds')

    # Step 2 : Obtain cursor to perform SQL operations
    cursor = connection.cursor()

    # Step 3 : Create SQL statement
    sql = "insert into customer values(null, '{name}', '{phone}', '{email}');".format_map(vars(customer))

    # Execute SQL command
    cursor.execute(sql)
    connection.commit()

    print("Customer Inserted")

if __name__ == "__main__":
    main()
