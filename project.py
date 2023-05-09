class Lib():

    def __init__(self, list):
        self.all_list = list
        self.available_books= list[:]
        self.lent_books={}
        

    def dis_all_list(self):
        for boo in self.all_list:
            print(boo)
    
    def dis_available(self):
        for bo in self.available_books:
            print(bo)
    
    def lend(self, book, name):
        if book not in self.all_list:
            print("\nPLEASE CHECK-'AVAILABLE BOOKS'")
            return
        
        if book in self.available_books:
            self.lent_books.update({book:name})
            self.available_books.remove(book)
            print("\nYou can take the book.........")
            print("\nNow the book is belongs to you........")
        
        else:
            print("\nThe book is taken by"" "+self.lent_books[book]) 
            print("\nPLEASE CHECK-'AVAILABLE BOOKS'")
    
    
    def return_book(self, book):
        del self.lent_books[book.upper()]
        self.available_books.append(book.upper())
    
    
    

pro=Lib(["BOOK1", "BOOK2", "BOOK3", "BOOK4"])
li= "welcome to jey's library"

while True:
    print(li.upper().center(100))
    print("1.BOOKS LIST")
    print("2.AVAILABLE BOOKS")
    print("3.BORROW BOOKS")
    print("4.RETURN BOOKS")
    print("5.EXIT")
    
    try:
        user_cho= int(input("ENTER THE ABOVE OPTION:"))

        if user_cho==1:
            bl="these books are belongs to jey's library"
            print(bl.upper().center(100))
            pro.dis_all_list()
            print("**************************")
        elif user_cho==2:
            av= "below books ARE available now"
            print(av.upper().center(100))
            pro.dis_available()
            print("**************************")
        elif user_cho==3:
            name=input("\nEnter your name:")
        
            book=input("\nEnter book name:")

            pro.lend(book.upper(), name.upper())
            print("**************************")

    
        elif user_cho==4:
            book= input("\nEnter the name of book:")
        

            pro.return_book(book)
            print("\nThe book is returned.")
            print("**************************")
    
        elif user_cho==5:
            break
        else:
            print("\n****************************")
            print("INVALID ATTEMPT, 'TRY AGAIN'")
            print("***************************")
    
    except ValueError:
            print("\n***********************")
            print("KINDLY ENTER APPROPRIATE OPTION")     
            print("***********************")   
    except KeyError:
            print("\nENTER THE OBTAINED BOOK NAME ")



