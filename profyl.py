import string
import random

def get_details():
    first_name = input("Enter your First Name below \n")
    last_name = input("Enter your Last Name below \n")
    user_email = input("Enter your Email below \n")

    details = [first_name,last_name,user_email]

    return details
    
#generate random password using user details
def gen_password(details):  

    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters)for i in range(length))

    password = str(details[0][0:2] + details[1][-2:] + random_password)

    return password
 

#main program
status = True
container = []

while status:

    #get user detail
    details = get_details()

    #show generated password
    password = gen_password(details)
    print ("Your password is: " + str(password))

    #ask if user like the password
    password_like = input(str("Do you like the generated password, If yes enter Yes if no, enter No and supply you password: \n"))

    password_loop = True

    while password_loop:
        if password_like == "Yes":
            #add password to user details
            details.append(password)
		
            #add user detail to overall container
            container.append(details)
		
            password_loop = False
		
        else:
	    #enter a password longer than or equal to 7
            user_password = input(str("Enter password longer than or equal to 7: \n"))
	    
            #password length loop
            pass_len = True
					
            while pass_len:
                if len(user_password) >= 7:
                    #add password to user details
                    details.append(user_password)

                    #add user details to container
                    container.append(details)

                    #break out of the while length check loop
                    pass_len = False

                    #break out of the while password loop
                    password_loop = False
            
                else:
                    print("Your password is less than 7: ")
                    user_password = input(str("Enter password longer than or equal to 7: \n"))        
   

    #new user
    new_user = input(str("Would you like to enter a new user? Yes or No: "))
    if (new_user =="No"):
        status = False
        for item in container:
            print(item)
    else:
        status = True
