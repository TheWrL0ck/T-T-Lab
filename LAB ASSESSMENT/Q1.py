import pickle

def createFile():
    fobj = open("Book.dat","ab")
    BookNo = int(input("Book Number : "))
    Book_name = input("Name :")
    author = input("Author: ")
    Price = int(input("Price : "))
    rec=[BookNo,Book_name,author,Price]
    pickle.dump(rec,fobj)
    fobj.close()   
    
def countRec(author):
    file = open("book.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2] == author:
                count+=1
    except EOFError:
        pass
    
    return count
    file.close()
    
def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n) ? ")
        if choice in 'No':
            break
    author = input("Enter Author name to search: ")
    n = countRec(author)
    print("Total no of books are",n)
    
testProgram()
