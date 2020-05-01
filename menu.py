import os

os.system("tput setaf 2")
print("""\t\t\tWelcome to TUI of Linux
\t\t\t-----------------------""")
os.system("tput setaf 7")

print("""Press 1 : For local host access
Press 2 : For remote host access""")

location = int(input("Enter your choice: "))

if location == 2:
    remote_ip = input("Enter Remote Client IP Address: ")

tries = 0

while True:
    
    if location == 1:
        print("""\nPrees 1 : to see date
Press 2 : to see cal 
Press 3 : to confg web server
Press 4 : to launch docker 
Press 5 : to create partition 
Press 6 : to add user 
Press 7 : exit\n""")

        usr_selection = int(input("Enter your choice: "))
    
        if usr_selection == 1:
            os.system("date")
        if usr_selection == 2:
            os.system("cal")
        if usr_selection == 3:
            os.system("dnf install httpd -y")
            os.system("systemctl start httpd")
            os.system("systemctl stop firewalld")
        if usr_selection == 4:
            os.system('date')
        if usr_selection == 5:
            os.system("date")
        if usr_selection == 6:
            os.system("date")
        if usr_selection == 7:
            break
    
    elif location == 2 :
        print("""\nPrees 1 : to see date
Press 2 : to see cal 
Press 3 : to confg web server
Press 4 : to launch docker 
Press 5 : to create partition 
Press 6 : to add user 
Press 7 : exit\n""")

        usr_selection = int(input("Enter your choice: "))
    
        if usr_selection == 1:
            os.system('ssh {0} date'.format(remote_ip))
        if usr_selection == 2:
            os.system('ssh {0} cal'.format(remote_ip))
        if usr_selection == 3:
            os.system('ssh {0} dnf install httpd -y'.format(remote_ip))
            os.system('ssh {0} systemctl start httpd'.format(remote_ip))
            os.system('ssh {0} systemctl stop firewalld'.format(remote_ip))
        if usr_selection == 4:
            os.system('ssh {0} date'.format(remote_ip))
        if usr_selection == 3:
            os.system("date")
        if usr_selection == 4:
            os.system("date")
        if usr_selection == 5:
            os.system("date")
        if usr_selection == 6:
            os.system("date")
        if usr_selection == 7:
            break
    else:
        if tries < 2:
            print("Please Enter Again...")
            location = int(input("Enter your choice: "))
            tries += 1
            continue
        else:
            print("You have exhausted max limit")
            break
    input("\nPress any key to Continue...")
    os.system("clear")
