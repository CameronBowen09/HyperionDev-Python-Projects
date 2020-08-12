file_object1 = open("user.txt", "r+") #Open user file object for reading and writing
#Initialize variables below
users_dictionary = {}
username = ""
passwords = ""
for lines in file_object1:
    lines = lines.replace("\n", "") #Replace the newline character with an empty space
    user_list = lines.split(", ") #Convert into a list
    #print(user_list) #Check if it changed to a list
    users_dictionary[user_list[0]] = user_list[1] #Store first list item as username
#print(users_dictionary)

users = str(input("Enter username here: ")) #Ask user to enter their username
while not users in users_dictionary:
    print("Error, wrong username!") #If username does not match display message
    users = str(input("Enter username here: "))
user_passwords = input("Enter your password here: ") #Ask user to enter their password
while user_passwords != users_dictionary[users]:
    print("Error, wrong password!") #If password does not match display this message
    user_passwords = input("Enter your password here: ")

#Once user has logged in successfully display these messages
print("welcome!", users)
if users == "admin":
    print("Please select one of the following options" + "\n" + "r" + " - " + "register user" + "\n" + "a" + " - " + "add task" + "\n" + "va" + " - " + "view all tasks" + "\n" + "vm" + " - " + "view my tasks" + "\n" + "s" + " - " + "View statistics" + "\n" + "e" " - " + "exit")
else:
    print("Please select one of the following options" + "\n" + "r" + " - " + "register user" + "\n" + "a" + " - " + "add task" + "\n" + "va" + " - " + "view all tasks" + "\n" + "vm" + " - " + "view my tasks" + "\n" + "e" " - " + "exit")

user_interface = input("Please enter the letter/letters corrisponding with what you want to do: ") #Ask user to enter the a letter corrisponding to waht they would like to do
if user_interface == "r": #If user enters r, run the loop below
    new_username = str(input("Enter a new username here: "))
    new_password = input("Enter a new password here: ")
    password_check = input("Enter password again for check: ")
    while new_password != password_check: #If the paswords do not match, run the loop below
        print("The passwords do not match!")
        password_check = input("Enter password again for check: ")
    file_object1.read() #Read the existing contents of the file
    file_object1.write("\n" + "" + new_username + "," + " " + new_password) #Add additional information to the file
    print("Your password and user name have successfully been changed!")
file_object1.close()

file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing
 
from datetime import date #Import the date function from datetime

if user_interface == "a": #If user enters a, run the loop below
    username = str(input("Enter username here: "))
    title_of_task = str(input("Enter the title of the task here: "))
    description_of_task = input("Enter a description of the task here: ")
    assigned_date = date.today() #Input the current date read from computer
    print(assigned_date)
    due_date = input("Enter the due date of the task here: ")
    task_completion = "No"
    file_object2.read() #Read the existing contents of the file
    file_object2.write("\n" + "" + username + ", " + title_of_task + ", " + description_of_task + ", " + str(assigned_date) + ", " + due_date + ", " + task_completion)
file_object2.close()

file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing

if user_interface == "va": #If user enters va, run the loop below
    for lines in file_object2:
        lines = lines.replace("\n", "") #Replace the newline character with an empty space
        task_list = lines.split(", ") #Convert into a list
        print("\n" + "Username: " + task_list[0] + "\n" + "Name of Task: " + task_list[1] + "\n" + "Description of Task: " + task_list[2] + "\n" + "Date of Assignment: " + task_list[3] + "\n" + "Due Date: " + task_list[4] + "\n" + "Task completion: " + task_list[5])
file_object2.close()

file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing

if user_interface == "vm":
    for lines in file_object2:
        lines = lines.replace("\n", "") #Replace the newline character with an empty space
        task_list = lines.split(", ") #Convert into a list
        if users == task_list[0]: #If user is the same as list item 1, run the loop below
            print("\n" + "Username: " + task_list[0] + "\n" + "Name of Task: " + task_list[1] + "\n" + "Description of Task: " + task_list[2] + "\n" + "Date of Assignment: " + task_list[3] + "\n" + "Due Date: " + task_list[4] + "\n" + "Task completion: " + task_list[5])
file_object2.close()

file_object1 = open("user.txt", "r+") #Open user file object for reading and writing
file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing

if user_interface == "s": #If the user enters s, run the loop below
    num_user = 0
    for lines in file_object1:
        num_user += 1 #Increment lines by 1
    print("Number of users: " + str(num_user))
    num_tasks = 0
    for lines in file_object2:
        num_tasks += 1 #Intrement lines by 1
    print("Number of tasks: " + str(num_tasks))
file_object1.close()
file_object2.close()

if user_interface == "e": #If user enters e, run the loop below
    exit() #Exit the program