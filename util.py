import shelve 

file1 = open("emails.txt")


def get_emails():
    x = []
    for line in file1:
        line = line.strip()
        line = line.split(",")
        for z in line:
            email = z
            x.append(email)
    
    return x
    

