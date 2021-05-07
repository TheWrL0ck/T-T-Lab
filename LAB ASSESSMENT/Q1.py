import pickle
def createFile():
    fobj=open("Book.dat","ab")
    BookNo=int(input("Book Number : "))
    Book_name=input("Name :")
    Author = input("Author: ")
    Price = int(input("Price : "))
    rec=[BookNo,Book_name,Author,Price]
    pickle.dump(rec,fobj)
    fobj.close()   
def countRec(Author):
    file = open("book.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2]==Author:
                count+=1
    except EOFError:
        pass
    return count
    file.close()
def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'No':
            break
    Author = input('Enter author name to search: ')
    n = countRec(Author)
    print("No of books are",n)
testProgram()