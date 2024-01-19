from datetime import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SecureP@ss1",
    database="libary"
)


def login():
    print("Enter your account data to sign in !!!")
    username = input("Enter UserName : ")
    password = input("Enter PassWord : ")
    mycursor = mydb.cursor()
    sql_select_query = f'select password from users where username = "{username}"'
    mycursor.execute(sql_select_query)
    record = mycursor.fetchone()
    pas = str(record[0])
    if pas == password:
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        myPage(username)
    else:
        print("wrong password!!!\nRun the program again :(")


def signup():
    mycursor = mydb.cursor()
    name = input("Enter your Name : ")
    username = input("Enter UserName : ")
    password = input("Enter password : ")
    sql = "INSERT INTO users (name, username , password) VALUES (%s, %s , %s)"
    val = (name, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    firstpage()


def availableBooks(token):
    print("here is a list of our available books to borrow Enter the name of the book at the console below!!!\n")
    mycursor1 = mydb.cursor()
    mycursor2 = mydb.cursor()
    mycursor3 = mydb.cursor()
    mycursor4 = mydb.cursor()
    query1 = "select name from books where available = 1"
    mycursor1.execute(query1)
    record = mycursor1.fetchall()
    for row in record:
        print(row[0])

    insert = input("\nEnter name : ")
    query2 = f"select count(username) from history where username = '{token}' and available = '1'"
    mycursor2.execute(query2)
    count = mycursor2.fetchone()
    num_of_borrowed = int(count[0])
    if num_of_borrowed > 3:
        print("you have borrowed the max amount of books!!!\n"
              "return some then come back later :)")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        myPage(token)
    elif num_of_borrowed < 3:
        query3 = f"UPDATE books SET available = '0' WHERE name = '{insert}'"
        mycursor3.execute(query3)
        date = datetime.today().strftime('%Y-%m-%d')
        query4 = f"insert into history values ('{insert}', '{token}', '{date}', '1')"
        mycursor4.execute(query4)
        mydb.commit()
        print("Book added to your list !")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        myPage(token)


def history(token):
    mycursor = mydb.cursor()
    query = f"select tarikh from history where username = '{token}'"
    mycursor.execute(query)
    record = mycursor.fetchall()
    print("here is a record of the dates where you borrowed books")
    for row in record:
        print(row[0])
    myPage(token)


def myPage(token):
    mycursor = mydb.cursor()
    sql_select_query = f'select name from users where username = "{token}"'
    mycursor.execute(sql_select_query)
    record = mycursor.fetchone()
    name = str(record[0])
    print("welcome " + name + "\nto see available books press : 1"
                              "\nto see your history press : 2"
                              "\nto see your book press : 3"
                              "\nExit press : 4")
    press = input("press : ")
    if press == "1":
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        availableBooks(token)
    if press == "2":
        history(token)
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        history(token)
    if press == "3":
        returnbook(token)
    if press == "4":
        print("Have a good day :)")


def returnbook(token):
    print("you have borrowed this books write their names below to return them")
    mycursor = mydb.cursor()
    query = f"select bookname from history where username = '{token}' and available = '1'"
    mycursor.execute(query)
    record = mycursor.fetchall()
    for row in record:
        print(row[0])
    insert = input("Enter name to return : ")
    query2 = f"UPDATE books SET available = '1' WHERE name = '{insert}'"
    query3 = f"UPDATE history SET available = '0' WHERE username = '{token}' and bookname = '{insert}'"
    mycursor.execute(query2)
    mycursor.execute(query3)
    mydb.commit()
    myPage(token)


def officerpage():
    print(" Enter 1 for customers history")
    print(" Enter 2 to see Book list")
    print(" Enter 3 to Exit")
    press = input("Enter : ")
    if press == "1":
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM history")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
    if press == "2":
        mycursor = mydb.cursor()
        mycursor.execute("select name from books where available = '1'")
        myresult = mycursor.fetchall()
        print("available books : ")
        for i in myresult:
            print(i[0])
        mycursor.execute("select name from books where available = '0'")
        myresult = mycursor.fetchall()
        print("borrowed books : ")
        for i in myresult:
            print(i[0])


    if press == "3":
        firstpage()


def firstpage():
    print("Welcome to public library!!! \nto login press : 1 \nto create account press : 2 \nto sign in as officer "
          "press : 3 \nto exit press : 4")
    press = input('press : ')
    if press == '1':
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        login()
    if press == '2':
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------")
        signup()
    if press == '3':
        officerpage()
    if press == '4':
        print('4')


firstpage()
1
