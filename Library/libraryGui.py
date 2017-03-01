

from tkinter import *
from libraryStudentVersion import *
from patronStudentVersion import *
from bookStudentVersion import *
from modelClassFile import *

class libraryStuff:

#Class Variables -------------------------------------------------------------
# These are for giving measurements for the entry boxes or the label and entry
#  placements when using grid()
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11
    TWELVE = 12
    THIRTEEN = 13
    FOURTEEN = 14
    FIFTEEN = 15
    SIXTEEN = 16
    SEVENTEEN = 17
    EIGHTEEN = 18
    NINETEEN = 19
    FORTY = 40

#Constructor ---------------------------------------------------------------
# Creates a library and it's ability to add books and authors, remove books and
#  return them, and to check out a book and patron
#initialize: self.__mainWindow to a Tk object
#            self.__library to a Library type
#            self.__addBook, self.__removeBook, self.__checkoutBook,
#              self.__checkoutPatron, and self.__returnBook to null values

    def __init__(self):
        self.__mainWindow = Tk()
        self.__library = Library("Pythonville Hometown Library")
        self.__addBook = None
        self.__addAuthor = None
        self.__removeBook = None
        self.__checkoutBook = None
        self.__checkoutPatron = None
        self.__returnBook = None

#PYTHONVILLE HOMETOWN LIBRARY ---------------------------------------------
        self.__pythonLabel = Label(text = "PYTHONVILLE HOMETOWN LIBRARY").\
                             grid(column = libraryStuff.THREE)
    #Checkout Section
        self.__checkoutLabel = Label(text = "Checkout Books").grid(row = 1,\
                                                                   column = 1)
        self.__titlelabelOne = Label(text = "Title").grid(row = libraryStuff.TWO, \
                                                          column = 0)
        self.__titleentryOne = Entry(width = libraryStuff.FORTY)
        self.__titleentryOne.grid(row = libraryStuff.TWO, column = 1)
        self.__titleentryOne.bind("<Return>", self.cancheckoutTitle)
        self.__patronlabelOne = Label(text = "Patron").grid(row = \
                                                            libraryStuff.THREE,\
                                                            column = 0)
        self.__patronentryOne = Entry(width = libraryStuff.FORTY)
        self.__patronentryOne.grid(row = libraryStuff.THREE, column = 1)
        self.__patronentryOne.bind("<Return>", self.cancheckoutPatron)
        self.__checkoutButton = Button(text = "Checkout Book", state =\
                                       "disabled", command = self.checkOut)
        self.__checkoutButton.grid(row = libraryStuff.FOUR, column = 1)
        self.__statuslabelOne = Label(text = "Status").grid(row = libraryStuff.FIVE, \
                                                            column = 0)
        self.__statusCheckout = StringVar()
        self.__statusCheckout.set(self.__library.getTransactionStatus())
        self.__statuscheckoutLabel = Label(textvariable = self.__statusCheckout)\
                                     .grid(row = libraryStuff.FIVE, column = 1)
    #Return Section
        self.__returnLabel = Label(text = "Return Books").grid(row = 1,\
                                                               column = libraryStuff.FOUR)
        self.__titlelabelTwo = Label(text = "Title").grid(row = libraryStuff.TWO,\
                                                          column = libraryStuff.THREE)
        self.__titleentryTwo = Entry(width = libraryStuff.FORTY)
        self.__titleentryTwo.grid(row = libraryStuff.TWO, column = libraryStuff.FOUR)
        self.__titleentryTwo.bind("<Return>", self.canreturnTitle)
        self.__patronlabelTwo = Label(text = "Patron").grid(row = libraryStuff.THREE,\
                                                            column = libraryStuff.THREE)
        self.__returnButton = Button(text = "Return Book", state =\
                                     "disabled", command = self.returnBook)
        self.__returnButton.grid(row = libraryStuff.FOUR, column = libraryStuff.FOUR)
        self.__statuslabelTwo = Label(text = "Status\n").grid(row = libraryStuff.FIVE, \
                                                              column = libraryStuff.THREE)
        self.__statusReturn = StringVar()
        self.__statusReturn.set("No transaction")
        self.__statusreturnLabel = Label(textvariable = self.__statusReturn).\
                                   grid(row = libraryStuff.FIVE, column = \
                                        libraryStuff.FOUR)

#SEARCH --------------------------------------------------------------------
        self.__searchLabel = Label(text = "SEARCH").grid(row = libraryStuff.SIX,\
                                                         column = libraryStuff.THREE)
    #Book Section
        self.__bookLabel = Label(text = "Book").grid(row = libraryStuff.SEVEN,\
                                                     column = 1)
        self.__titlelabelThree = Label(text = "Title").grid(row =\
                                                            libraryStuff.EIGHT, \
                                                            column = 0)
        self.__titleentryThree = Entry(width = libraryStuff.FORTY)
        self.__titleentryThree.grid(row = libraryStuff.EIGHT, column = 1)
        self.__titleentryThree.bind("<Return>", self.setBook)
        self.__statuslabelThree = Label(text = "Status").grid(row = libraryStuff.NINE,\
                                                              column = 0)
        self.__statusBook = StringVar()
        self.__statusBook.set("No transaction")
        self.__statusbookLabel = Label(textvariable = self.__statusBook).grid\
                                 (row = libraryStuff.NINE, column = 1)
    #Patron Section
        self.__patronLabel = Label(text = "Patron").grid(row = libraryStuff.SEVEN,\
                                                         column = libraryStuff.FOUR)
        self.__namelabelOne = Label(text = "Name").grid(row = libraryStuff.EIGHT,\
                                                        column = libraryStuff.THREE)
        self.__nameentryOne = Entry(width = libraryStuff.FORTY)
        self.__nameentryOne.grid(row = libraryStuff.EIGHT, column = \
                                 libraryStuff.FOUR)
        self.__nameentryOne.bind("<Return>", self.setPatron)
        self.__statuslabelFour = Label(text = "Status\n").grid(row = libraryStuff.NINE,\
                                                             column = libraryStuff.THREE)
        self.__statusPatron = StringVar()
        self.__statusPatron.set("No transaction")
        self.__statuspatronLabel = Label(textvariable = self.__statusPatron).\
                                   grid(row = libraryStuff.NINE, \
                                        column = libraryStuff.FOUR)

#MEMBERSHIP -------------------------------------------------------------------
        self.__membershipLabel = Label(text = "MEMBERSHIP").grid(row = \
                                                                 libraryStuff.TEN,\
                                                                 column =\
                                                                 libraryStuff.THREE)
    #Join Section
        self.__joinLabel = Label(text = "Join").grid(row = libraryStuff.ELEVEN,\
                                                     column = 1)
        self.__namelabelTwo = Label(text = "Name").grid(row = \
                                                        libraryStuff.TWELVE,\
                                                        column = 0)
        self.__nameentryTwo = Entry(width = libraryStuff.FORTY)
        self.__nameentryTwo.grid(row = libraryStuff.TWELVE, column = 1)
        self.__nameentryTwo.bind("<Return>", self.setJoin)
        self.__statuslabelFive = Label(text = "Status").grid(row = \
                                                             libraryStuff.THIRTEEN,\
                                                             column = 0)
        self.__joinStatus = StringVar()
        self.__joinStatus.set("No transaction")
        self.__joinStatusLabel = Label(textvariable = self.__joinStatus).\
                                 grid(row = libraryStuff.THIRTEEN, column = 1)
    #Leave Section
        self.__leaveLabel = Label(text = "Leave").grid(row = libraryStuff.ELEVEN,\
                                                       column = libraryStuff.FOUR)
        self.__namelabelThree = Label(text = "Name").grid(row = libraryStuff.TWELVE,\
                                                          column = libraryStuff.THREE)
        self.__nameentryThree = Entry(width = libraryStuff.FORTY)
        self.__nameentryThree.grid(row = libraryStuff.TWELVE, column = \
                                   libraryStuff.FOUR)
        self.__nameentryThree.bind("<Return>", self.setLeave)
        self.__statuslabelSix = Label(text = "Status\n").grid(row = libraryStuff.THIRTEEN,\
                                                            column = libraryStuff.THREE)
        self.__leaveStatus = StringVar()
        self.__leaveStatus.set("No transaction")
        self.__leavestatusLabel = Label(textvariable = self.__leaveStatus).\
                                  grid(row = libraryStuff.THIRTEEN, column =\
                                       libraryStuff.FOUR)
#BOOK COLLECTION ---------------------------------------------------------------
        self.__collectionLabel = Label(text = "BOOK COLLECTION").grid\
                                 (row = libraryStuff.FOURTEEN, \
                                  column = libraryStuff.THREE)
    #Add Book
        self.__addLabel = Label(text = "Add Book").grid(row = libraryStuff.FIFTEEN,\
                                                        column = 1)
        self.__titlelabelFour = Label(text = "Title").grid(row = \
                                                           libraryStuff.SIXTEEN,\
                                                           column = 0)
        self.__titleentryFour = Entry(width = libraryStuff.FORTY)
        self.__titleentryFour.grid(row = libraryStuff.SIXTEEN, column = 1)
        self.__titleentryFour.bind("<Return>", self.canaddBook)
        self.__authorlabelOne = Label(text = "Author").grid(row = \
                                                            libraryStuff.SEVENTEEN,\
                                                            column = 0)
        self.__authorentryOne = Entry(width = libraryStuff.FORTY)
        self.__authorentryOne.grid(row = libraryStuff.SEVENTEEN, column = 1)
        self.__authorentryOne.bind("<Return>", self.canaddAuthor)
        self.__addButton = Button(text = "Add Book", state = "disabled", \
                                  command = self.addBook)
        self.__addButton.grid(row = libraryStuff.EIGHTEEN, column= 1)
        self.__statuslabelSeven = Label(text = "Status").grid(row = \
                                                              libraryStuff.NINETEEN, \
                                                              column = 0)
        self.__addStatus = StringVar()
        self.__addStatus.set("No transaction")
        self.__addstatusLabel = Label(textvariable = self.__addStatus).grid\
                                (row = libraryStuff.NINETEEN, column = 1)
    #Remove Section
        self.__removeLabel = Label(text = "Remove Book").grid(row = \
                                                              libraryStuff.FIFTEEN,\
                                                              column =\
                                                              libraryStuff.FOUR)
        self.__titlelabelFive = Label(text = "Title").grid(row = \
                                                           libraryStuff.SIXTEEN, \
                                                           column = \
                                                           libraryStuff.THREE)
        self.__titleentryFive = Entry(width = libraryStuff.FORTY)
        self.__titleentryFive.grid(row = libraryStuff.SIXTEEN, \
                                   column = libraryStuff.FOUR)
        self.__titleentryFive.bind("<Return>", self.canremoveTitle)
        self.__authorlabelTwo = Label(text = "Author").grid(row =\
                                                            libraryStuff.SEVENTEEN,\
                                                            column =\
                                                            libraryStuff.THREE)
        self.__removeButton = Button(text = "Remove Book", state = "disabled",\
                                     command = self.removetheBook)
        self.__removeButton.grid(row = libraryStuff.EIGHTEEN, column =\
                                 libraryStuff.FOUR)
        self.__statuslabelSeven = Label(text = "Status").grid(row = \
                                                              libraryStuff.NINETEEN,\
                                                              column = \
                                                              libraryStuff.THREE)
        self.__removeStatus = StringVar()
        self.__removeStatus.set("No transaction")
        self.__removestatusLabel = Label(textvariable = self.__removeStatus).\
                                   grid(row = libraryStuff.NINETEEN, column = \
                                        libraryStuff.FOUR)
                
        mainloop()

#FUNCTIONS -----------------------------------------------------------------

    #checks if the user put in something in the books title box and if
    #  there's an entry for the patron box
    #Makes the button state normal as long as the conditions above are met
    #Invokes get()
    def cancheckoutTitle(self, event):
        self.__checkoutBook = self.__titleentryOne.get()
        if bool(self.__checkoutPatron):
            self.__checkoutButton.configure(state = "normal")

    #checks if the user put in something in the books title column and if
    #  there's an entry for the patron box
    #Makes the button state normal as long as the conditions above are met
    #Invokes get()
    def cancheckoutPatron(self, event):
        self.__checkoutPatron = self.__patronentryOne.get()
        if bool(self.__checkoutBook):
            self.__checkoutButton.configure(state = "normal")

    #checks if the user put in something in the entry box
    #Makes the button state normal if there is something in the box
    #Invokes get()
    def canreturnTitle (self, event):
        self.__returnBook = self.__titleentryTwo.get()
        if bool(self.__returnBook):
            self.__returnButton.configure(state = "normal")

    #checkcs if the user put in something in the author box and if the user
    # put in something in the book box
    #Makes the button state normal as long as the above conditions are met
    #Invokes get()
    def canaddBook(self, event):
        self.__addBook = self.__titleentryFour.get()
        if bool(self.__addAuthor):
            self.__addButton.configure(state = "normal")

    #checkcs if the user put in something in the author box and if the user
    # put in something in the book box
    #Makes the button state normal as long as the above conditions are met
    def canaddAuthor(self, event):
        self.__addAuthor = self.__authorentryOne.get()
        if bool(self.__addBook):
            self.__addButton.configure(state = "normal")

    #checks if the user put in something in the book entry box
    #Makes the button state normal if there is something typed in the box
    #Invokes get()
    def canremoveTitle(self, event):
        self.__removeBook = self.__titleentryFive.get()
        if bool(self.__removeBook):
            self.__removeButton.configure(state = "normal")

    #gets the book from the entry box and then sets the status of the book
    #  by getting the book's from the library
    #invokes library.getBook() and get()
    def setBook(self, event):
        theBook = self.__titleentryThree.get()
        self.__statusBook.set(self.__library.getBook(theBook))

    #gets the patron name from the entry box and then displays the status of
    #  that person by getting the patron from the library
    #invokes library.getPatron() and get()
    def setPatron(self, event):
        thePatron = self.__nameentryOne.get()
        self.__statusPatron.set(self.__library.getPatron(thePatron))

    #gets the patron from the entry box and then removes the patron from the
    #  library and displays this status
    #invokes library.removePatron() and library.getTransactionStatus()
    #  and get()
    def setLeave(self, event):
        thePatron = self.__nameentryThree.get()
        self.__library.removePatron(thePatron)
        self.__leaveStatus.set(self.__library.getTransactionStatus())

    #gets the patron from the entry box and then adds the patron to the patron
    #  dictionary in the library. Sets the status of this as well
    #invokes library.addPatron() and library.getTransactionStatus()
    #  and get()
    def setJoin(self, event):
        thePatron = Patron(self.__nameentryTwo.get())
        self.__library.addPatron(thePatron)
        self.__joinStatus.set(self.__library.getTransactionStatus())

    #removes the book from the library and then disables the button
    #invokes library.removeBook(), configure(), and 
    #  library.getTransactionStatus()
    def removetheBook(self):
        theBook = self.__titleentryFive.get()
        if self.__library.inLibrary(theBook):
            self.__library.removeBook((self.__removeBook))
            self.__removeStatus.set(self.__library.getTransactionStatus())
        else:
            self.__removeStatus.set("That book is not in the library")
        self.__removeBook = None
        self.__removeButton.configure(state = "disable")

    #adds a book and its author to the library and sets this transaction
    #  status. It also sets the button state to disable
    def addBook(self):#buttons aren't events
        self.__library.addBook(Book(self.__addBook, self.__addAuthor))
        self.__addStatus.set(self.__library.getTransactionStatus())
        self.__addBook = None
        self.__addAuthor = None
        self.__addButton.configure(state = "disable")

    #checks if the book and patron is valid and if so, allows the patron to
    #  borrow the book he/she wants. Sets the button to disabled afterward
    #  displays the status 
    #Invokes library.isMember(), set(), librar.getBook(), library.getPatron()
    def checkOut(self): 
        if not self.__library.inLibrary((self.__checkoutBook)) and not\
                                        self.__library.isMember(\
                                            self.__checkoutPatron):
            self.__statusCheckout.set((self.__checkoutBook) + " is not in\
 library and " + (self.__checkoutPatron) + " is not a member")
        elif not(self.__library.inLibrary(self.__checkoutBook)):
            self.__statusCheckout.set((self.__checkoutBook) + \
                                      " is not in library")
        elif not(self.__library.isMember(self.__checkoutPatron)):
            self.__statusCheckout.set((self.__checkoutPatron) + \
                                      " is not a member")
        else:
            theBook = self.__library.getBook(self.__checkoutBook)
            theBook.borrowMe(self.__library.getPatron(self.__checkoutPatron))
            self.__statusCheckout.set(theBook.getTransactionStatus())
        self.__checkoutBook = None
        self.__checkoutPatron = None
        self.__checkoutButton.configure(state = "disable")

    #Gets the book from the entry box and returns the book if it is checked
    #  out. It then sets the status for this
    #Invokes isCheckedOut(), getBook(), getTransactionStatus(), set()
    def returnBook(self):
        theBook = self.__titleentryTwo.get()
        if self.__library.inLibrary(theBook):
            theBook = (self.__library.getBook(self.__returnBook))
            if theBook.isCheckedOut:
                theBook.returnMe()
                self.__statusReturn.set(theBook.getTransactionStatus())
            else:
                self.__statusReturn.set(theBook.getTransactionStatus())
        else:
            self.__statusReturn.set("That book is not in the library")
        self.__returnBook = None

        
libraryStuff()
        
