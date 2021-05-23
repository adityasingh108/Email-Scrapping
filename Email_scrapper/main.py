def email_slicing():
    ''' This function
    read  from a text file and give your entire email in the file
    '''
    import re
    try:
        file_name = input("Enter the file name :")
        Email_string = open(file_name, "r")
    except:
        print("Enter file name Correctly!!")
        exit()

    Email_read = Email_string.read()
    email = re.findall(r"\w+@\S+\w", Email_read)
    list1 = list(email)
    i = 1
    with open("Email.txt", "w") as file:
        for item in list1:
            file.write(f"{i} {item}\n")
            i = i+1
if __name__ == '__main__':
    email_slicing()
