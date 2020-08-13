Task Manager Functions: Capstone IV

This is a program that stores users information in a text file,
this is inofrmation on tasks for each individual user. However, 
this time the program is put together using functions. 

When the program starts running it will ask the user to enter their
username, if the username is not recognised the program will display
error, wrong username. If the username is recognised the program will
then ask the user to enter their password, if the passoword is not
correct then the program will display error, wrong password and ask
the user t enter their password again.

If the username entered is admin then a menu will display the
following: Please select the following options. "r" to register a 
new user, "a" to add a task, "va" to view all task, "vm" to view 
my tasks, "gr" to gererate reports, "ds" to display statistics 
and "e" to exit the program.

If the username entered is not admin then a menu will display the
following: Please select the following: "a" to add a task, "va" to 
view all tasks, "vm" to view my tasks and "e" to exit the program.

If admin enters "r" the program will ask to enter a new username, once 
done it will ask to enter a new password, then ask to verify the 
password entered, if they not the same ask again. This will now also
show an error if the new username being added is the same as an 
existing username.

If the user enters "a" the program will ask the user to enter their
username, enter the title of the task, enter a discription of the
task, enter the due date of the task. Once all information is entered
it is saved.

If the user enters "va" the program will display all the task 
information for the user.

If the user enters "vm" the program will display all your tasks
information. This will now display message requiring input and 
a menu after the task iformation that displays enter the number of
a task you would like to edit, the ,menu displays input 0 to change
username, input 4 to change the due date, input 5 to change the task
to complete. Tasks can only be edited if they have not yet been 
completed. If the user enters -1 the program will display the main 
menu once again.

If admin enters "ds" the program will display all the information 
and statistics about the tasks and display all the information and
statistics about the users.

If admin enters "gs" the program will gather all the information
about the tasks and users ready to be displayed.

If the user enters "e" the program will exit and end.