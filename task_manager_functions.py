from datetime import date
import datetime

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


def reg_user():
   
    if user_interface == "r": #If user enters r, run the loop below
        new_username = str(input("Enter a new username here: "))
        while new_username in users_dictionary:
            print("Username already exists")
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

#reg_user()

def add_task():
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

#add_task()

def view_all():
    
    file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing
    if user_interface == "va": #If user enters va, run the loop below
        for lines in file_object2:
            lines = lines.replace("\n", "") #Replace the newline character with an empty space\
            task_list = lines.split(", ") #Convert into a list
            print("\n" + "Username: " + task_list[0] + "\n" +
            "Name of Task: " + task_list[1] + "\n" +
            "Description of Task: " + task_list[2] + "\n" +
            "Date of Assignment: " + task_list[3] + "\n" +
            "Due Date: " + task_list[4] + "\n" +
            "Task completion: " + task_list[5])
    file_object2.close()

#view_all()

def view_mine():
    file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing

    if user_interface == "vm":
        all_tasks = []
        tracker = 0
        for lines in file_object2:
            lines = lines.replace("\n", "") #Replace the newline character with an empty space
            task_list = lines.split(", ") #Convert into a list
            all_tasks.append(task_list)
            
            if users == task_list[0]: #If user is the same as list item 1, run the loop below
                print("\n" + str(tracker))
                print("Username: " + task_list[0] + "\n" + 
                "Name of Task: " + task_list[1] + "\n" + 
                "Description of Task: " + task_list[2] + "\n" + 
                "Date of Assignment: " + task_list[3] + "\n" + 
                "Due Date: " + task_list[4] + "\n" + 
                "Task completion: " + task_list[5])
            tracker += 1 #Increment tracker by 1
    file_object2.close()


    while 1:
        file_object2 = open("tasks.txt", "r+") #Open tasks file for reading and writing
        user_input = int(input("\n" + "Enter the number of the task or input -1 if you would like to exit: "))
        if user_input >= 0 and user_input <= tracker:
            select_task_edit = all_tasks[user_input]
            #print(select_task_edit)
            if select_task_edit[5].lower() == "no":
                print("\n" + "Input: 0 to change the username " + "\n" #Print this user interfcae for the user
                "Input: 4 to change the due date" + "\n"
                "Input: 5 to change if the task is completed")
                user_input2 = input("What would you like to edit? ")
                if user_input2 == "0":
                    changed_user = input("Enter a current user to change username: ")
                    if changed_user in users_dictionary:
                        select_task_edit[0] = changed_user
                        all_tasks[user_input] = select_task_edit
                    else:
                        print("Username is not valid")
                if user_input2 == "4":
                    date_change = input("Enter a new due date here: ")
                    select_task_edit[4] = date_change
                    all_tasks[user_input] = select_task_edit
                if user_input2 == "5":
                    check_complete = input("Would you like to mark task as complete? ")
                if check_complete == "yes":
                    select_task_edit[-1] = "yes"
                    all_tasks[user_input] = select_task_edit
            else:
                print("This task has already been completed!")
        elif user_input == -1:
            break
        else:
            print("Invalid input!")
    strdata = ""
    file_object2.flush() #Remove old contect to add new content
    for line in all_tasks:
        strdata += line[0] + ", " + line[1] + ", " + line[2] + ", " + line[3] + ", " + line[4] + ", " + line[5]+'\n' 
    strdata = strdata.strip("\n")
    file_object2.write(strdata) #Write to file_object2
    file_object2.close()

#view_mine()

def user_review(username, num_tasks):
    
    file_object2 = open("tasks.txt", "r") #Open tasks file for reading
    #Initialize variables below
    total_assigned_tasks = 0
    task_completed = 0
    task_uncompleted = 0
    percent_completed_all = 0.0
    percent_complete_my = 0.0
    percent_uncomplete = 0.0
    overdue_tasks = 0
    percent_overdue = 0.0
    for lines in file_object2:
        lines = lines.strip("\n") #Strip the lines of \n
        task_list = lines.split(", ") #Convert into a list
        if username == task_list[0]:
            total_assigned_tasks += 1 #Increment total assigned tasks by 1
            if task_list[-1].lower() == "yes":
                task_completed += 1 #Increment tasks complete by 1
                percent_completed_all = (task_completed * 100) / num_tasks  #Calculate the percentage of completed tasks
            if task_list[-1].lower() == "no":
                task_uncompleted += 1 #Increment tasks uncomplete by 1
                percent_uncomplete = (task_uncompleted * 100) / total_assigned_tasks #Calculate the percentage of uncomplete tasks
            percent_complete_my = (task_completed * 100) / total_assigned_tasks #Calculate the percentage of completed tasks
            current_date = datetime.datetime.now() #Get current date
            due_date = datetime.datetime.strptime(task_list[4], "%d %b %Y") #Formate date into readable formate
            if current_date > due_date: 
                overdue_tasks += 1 #Increment overdue tasks by 1
                if task_list[-1].lower() == "no":
                    percent_overdue = (overdue_tasks * 100) / total_assigned_tasks #Calculate the percentage of overdue tasks
    return("\n" + "Username: " + username + ", has " + str(total_assigned_tasks) + " tasks assigned to them" + "\n" +
    "\t" + " - has completed " + str(percent_completed_all) + " percent of all tasks" + "\n" + 
    "\t" + " - has completed " + str(percent_complete_my) + " percent of the tasks assigned" + "\n" +
    "\t" + " - has " + str(percent_uncomplete) + " percent of assigned tasks not complete" + "\n" +
    "\t" + " - has " + str(percent_overdue) + " percent of assigned tasks over due")


def generate_reports():
    
    file_object2 = open("tasks.txt", "r") #Open tasks file for reading
    if user_interface == "gr":
        num_tasks = 0
        for lines in file_object2:
            num_tasks += 1 #Intrement num tasks by 1
        #print("Number of tasks: " + str(num_tasks))
        file_object2.close()
        
        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        num_tasks_complete = 0
        for lines in file_object2:
            lines = lines.strip("\n") #Strip the lines of \n
            task_list = lines.split(", ") #Convert into a list
            if task_list[-1].lower() == "yes":
                num_tasks_complete += 1 #Increment num tasks complete by 1
        #print("Number of completed tasks: " + str(num_tasks_complete))
        file_object2.close()

        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        num_tasks_uncomplete = 0
        for lines in file_object2:
            lines = lines.strip("\n") #Strip the lines of \n
            task_list = lines.split(", ") #Convert into a list
            if task_list[-1].lower() == "no":
                num_tasks_uncomplete += 1 #Intrement num task complete by 1
        #print("Number of uncompleted tasks: " + str(num_tasks_uncomplete))
        file_object2.close()

        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        overdue_tasks = 0
        for lines in file_object2:
            lines = lines.strip("\n") #Strip the lines of \n
            task_list = lines.split(", ") #Convert into a list
            current_date = datetime.datetime.now() #Get the current date
            due_date = datetime.datetime.strptime(task_list[4], "%d %b %Y") #Formate date into readable formate
            if current_date > due_date: 
                overdue_tasks += 1 #Increment overdue date by 1
                #print(task_list[4])
        #print("Number of overdue tasks: " + str(overdue_tasks))
        file_object2.close()

        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        percent_comp_tasks = (num_tasks_complete * 100) / num_tasks_uncomplete #Calculate the percentage of completed tasks
        #print("Percentage of completed tasks: " + str(percent_comp_tasks))
        # file_object2.close()

        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        percent_overdue_tasks = (overdue_tasks * 100) / num_tasks #Calculate the percentage of overdue tasks
        #print("Percentage of overdue tasks: " + str(percent_overdue_tasks))
        file_object2.close()

        file_object3 = open("task_overview.txt", "w") #Open task overview for writing
        file_object3. write("Number of tasks: " + str(num_tasks) + "\n" +
        "Number of completed tasks: " + str(num_tasks_complete) + "\n" +
        "Number of uncompleted tasks: " + str(num_tasks_uncomplete) + "\n" +
        "Number of overdue tasks: " + str(overdue_tasks) + "\n" +
        "Percentage of completed tasks: " + str(percent_comp_tasks) + "\n" +
        "Percentage of overdue tasks: " + str(percent_overdue_tasks))
        file_object3.close()

        file_object1 = open("user.txt", "r") #Opent user file for reading
        num_user = 0
        for lines in file_object1:
            num_user += 1 #Increment num user by 1
        #print("Number of users: " + str(num_user))
        file_object1.close()

        file_object2 = open("tasks.txt", "r") #Open tasks file for reading
        num_tasks = 0
        for lines in file_object2:
            num_tasks += 1 #Intrement num tasks by 1
        #print("Number of tasks: " + str(num_tasks))
        file_object2.close()

        file_object4 = open("user_overview.txt", "w") #Open user overview file for writing
        file_object4.write("Number of users: " + str(num_user) + "\n" +
        "Number of tasks: " + str(num_tasks))
        user_info = ""
        for k in users_dictionary.keys():
            user_info += user_review(k,num_tasks)
        file_object4.write(user_info)
        file_object4.close()

#generate_reports()  

def display_statistics():
    
    generate_reports()

    file_object3 = open("task_overview.txt", "r") #Open task overview for reading
    print("\n" + "Task statistics below: ")
    lines = file_object3.read()
    print(lines)
    file_object3.close()

    file_object4 = open("user_overview.txt", "r") #Open user overview file for reading
    print("\n" + "User statistics below: ")
    lines = file_object4.read()
    print(lines)
    file_object4.close()

#display_statistics()
while 1:
    #Once user has logged in successfully display these messages
    print("welcome!", users)
    if users == "admin":
        print("Please select one of the following options" + "\n" +
        "r" + " - " + "register user" + "\n" +
        "a" + " - " + "add task" + "\n" +
        "va" + " - " + "view all tasks" + "\n" +
        "vm" + " - " + "view my tasks" + "\n" +
        "gr" + " - " + "Generate reports" + "\n" +
        "ds" + " - " + "Display statistics" + "\n" +
        "e" + " - " + "exit")
    else:
        print("Please select one of the following options" + "\n" +
        "a" + " - " + "add task" + "\n" +
        "va" + " - " + "view all tasks" + "\n" +
        "vm" + " - " + "view my tasks" + "\n" +
        "e" + " - " + "exit")

    user_interface = input("Please enter the letter/letters corrisponding with what you want to do: ") #Ask user to enter the a letter corrisponding to waht they would like to do
    
    #If any of the letters are inputted, run the corrisponding function
    if user_interface == "r":
        reg_user()
    elif user_interface == "a":
        add_task()
    elif user_interface == "va":
        view_all()
    elif user_interface == "vm":
        view_mine()
    elif user_interface == "gr":
        generate_reports()
    elif user_interface == "ds":
        display_statistics()
    elif user_interface == "e":
        exit()
