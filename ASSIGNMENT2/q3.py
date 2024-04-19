#* Write a python program to print all employees, employees of given department, employee with highest and lowest salary
import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    
    host="localhost",
    port=3306, 
    user="sunbeam",
    password="sunbeam",
    database="iotdb"

)
def show():
    query = "select * from employees;"
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()


def show_dept(dept):
    query = "select * from employees where dept=%s;" 
    cursor = connection.cursor()
    cursor.execute(query, (dept, ))
    for row in cursor:
        print(row)
    cursor.close()

def show_highest_salary():
    query = "select * from employees order by salary desc limit 1;"
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()
   


def show_lowest_salary():
    query = "select * from employees order by salary asc limit 1;"
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close()



while True:
        
    choice=int(input("Enter 1 to show all employees, 2 to show employees of given department, 3 to show employee with highest salary, 4 to show employee with lowest salary, 5 to exit: "))
    match choice:
        case 1:
            print("Showing all employees")
            show()
        case 2:
              
            dept=input("Enter department name: ")
            print(f"Showing employees of department: '{dept}'")
            show_dept(dept)

        case 3:
            print("Showing employee with highest salary")
            show_highest_salary()


        case 4:
            print("Showing employee with lowest salary")
            show_lowest_salary()

        case 5:



            print("Exiting")

                    
            break

        case _:
            print("Invalid choice")


#close the connection with mysql server 
connection.close()