from Session14A import *
from Session14B import DBHelper


def main():

    db = DBHelper()
    print("Welcome to VetsApp")
    message = """
    1: Add new Customer
    0: Quit
    """
    print(message)
    choice = int(input("Enter your choice:"))

    while True:
        if choice == 1:

            customer = Customer()
            customer.read_customer_data()
            print(vars(customer))

            sql = customer.get_insert_sql_query()

            db.execute_sql(sql)

        elif choice == 0:
            print("Thank you for using Vets app")
            break

        else:
            print("Invalid Choice")
        print(message)
        choice = int(input("Enter your choice:"))

if __name__ == "__main__":
    main()
