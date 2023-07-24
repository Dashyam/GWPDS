import mysql.connector as db


def main():
    sql1 = "update Customer set name = 'John Watson', age = 26 where cid=1"
    sql2 = "delete from Customer where cid=2"
    sql3 = "select * from Customer"

    connection = db.connect(user='root',
                            password='12345678',
                            host='127.0.0.1',
                            database='gwpds')

    cursor = connection.cursor()

    # cursor.execute(sql1)
    # cursor.execute(sql2)
    # connection.commit()

    cursor.execute(sql3)
    rows = cursor.fetchall()
    print("CID\t Name")
    for row in rows:
        # print(row)
        print(row[0], "\t", row[1])
if __name__ == "__main__":
    main()
