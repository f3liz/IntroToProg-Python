# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# FChen,2.13.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
        lstTable += [dicRow]
    objFile.close()
    print("Task|Priority")
    for row in lstTable:
        print(row["Task"] + '|' + row["Priority"].strip())
    print("^Current Data listed above^")

except:
    print('''
    ToDoList.exe file currently not found
    One has now been created for you
    ''')
    objFile = open("ToDoList.txt", "w")
    objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Current data is: ")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"].strip())
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("Please enter a task and it's priority from 1 (high) to 5(low)")
        strTask = str(input("Name of task: "))
        while (True):
            strPriority = int(input("Priority of the task: "))
            if strPriority not in range(1,6):
                print("Please choose from 1 being high priority to 5 being lowest priority")
            else:
                break
        strPriority = str(strPriority)
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable += [dicRow]
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask = str(input("Name of the task you'd like removed: "))
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("Task has now been removed!")
                break
            else:
                print("Task not found.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("Your data has been saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("\tThank you for your time!!!")
        break  # and Exit the program
    else:
        print("Please choose options 1 to 5")
