import pymysql

from ReadConfig import read_db_config

db=None

try:
    dbParam = read_db_config()
    db = pymysql.connect(**dbParam)
    cursor = db.cursor()
    f_name = input("enter your first name:")
    l_name = input("enter your last name:")
    age = int(input("enter your age:"))
    gender = input("enter your gender:")
    income = eval(input("enter your income:"))

    sql = "INSERT INTO employees(FirstName, LastName, Age, Income) \
        VALUES ('%s', '%s', '%d', '%d')" % (f_name, l_name, age, income)

    cursor.execute(sql)
    db.commit()
    print("Employee added successfully.")
    db.close()
except ValueError:
 print("one of your inputs is invalid")
except Exception as err:
    print("Error:{0}".format(err))


