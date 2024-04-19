# Write a python program to add, delete, update employees into table

import dbconn

connection=dbconn.get_connection()

def add():
    # create a query
    empid = int(input("Enter empid : "))
    name = input("Enter name : ")
    dept = input("Enter dep : ")
    email = input("Enter email :")
    salary = input("Enter salary : ")
    doj=input("Enter Doj : ")

    query = f"insert into employees values({empid}, '{name}', '{dept}', '{email}', '{salary}' ,'{doj}');"

    
# create a cursor to execute the query
    cursor = connection.cursor()

# execute query using cursor
    cursor.execute(query)

# after execution of query commit your changes
    connection.commit()

# close the cursor
    cursor.close()

#close the connection with mysql server 
    connection.close()


def update_person(empid, salary):
    # get connection
    # connection = get_connection()

    # form a query
    query = f"update employees SET salary = %s where empid = %s;"
    val = ( salary,empid)

    # create a cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    connection.commit()

    # close cursor as well as connection
    cursor.close()
    connection.close()

def retrive():
    # form a qery
    query = "select * from employees;"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    print(records)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()
    
def delete_employee(empid):
    # get connection
    # connection = get_connection()

    # form a query
    query = f"delete from employees where empid = %s;"
    val = (empid,)

    # create a cursor
    cursor = connection.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    connection.commit()

    # close cursor as well as connection
    cursor.close()
    connection.close()    


print("1:add")
print("2.update")
print("3.retrive")
print("4.delete")
print("Enter your Choice ")
choice=int(input("Enter a number :"))



match choice:
    case 1:
        add()
    case 2:
        update_person(1, "30000")
    case 3:
        retrive()
    case 4:
        delete_employee(1)   
    case _:
        print("Unknown Class")

