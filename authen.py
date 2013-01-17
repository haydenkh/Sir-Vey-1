import shelve 

file1 = open("emails.txt")


def get_emails():
    x = []
    for line in file1:
        line = line.strip()
        line = line.split(",")
        print line
        for z in line:
            email = z
            x.append(email)
    print x
    print x[0]
    print x[4]
    y = x[0]
    z = "amanpreet123@gmail.com"
    if z == y:
        print "hellO"
    return x
    
    
            

def isAKey(email):
    emails = get_emails()
    for y in emails:
        print "\n" + x
        if  x == email:
            print "yay"
            return True
        if ' ' + x == email:
            print "yay"
    
    print "no"
    return False


#get_emails()
x = "dlevylambert@gmail.com"
isAKey(x)