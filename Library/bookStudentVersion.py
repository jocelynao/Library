'''
Jocelyn Ao
jao1@binghamton.edu
Lab Section B57 Jia Yang
Assignment 11 Exercise Book
'''

'''
This class represents a book with a title, author, status,
a patron to whom the book is checked out, and a list
of patrons waiting for it
'''
class Book:
  # Class Variables ----------------------------------------------------------
  # index when book is first created (int)
    NONE = 0
    
  # index when book is loaned successfully (int)
    SUCCESSFUL = 1

  # index when patron is put on waiting list (int)  
    WAIT = 2

  # index when request for loan is unsuccessful (int)
    UNSUCCESSFUL = 3

  # index when book is returned (int)
    RETURNED = 4

  # index when request for loan is invalid (int)
    INVALID = 5

  # status of most recent transaction with respect to this book (str)
  # Will be combined with name of patron participating in transaction and
  #   and title of this book"""
    TRANS_STATUS = [" No transactions yet",
                  " successfully checked out ",
                  " has been put on waiting list for ",
                  " must return books before taking out ",
                  " has returned ",
                  " has recorded an invalid transaction re:  "]
# Constructor --------------------------------------------------------------

  # Creates a new book with the given title and author
  # params:  title (str) and author (str) of book
  # initialize:  self.__title (str) and self.__author (str) to value of
  #                incoming parameters
  #              self.__transactionStatus (str) to no transactions yet,
  #              self.__patron (Patron) & self.__waitList (list of Patrons) 
  #                 to null/empty values
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__transactionStatus = Book.TRANS_STATUS[0]
        self.__patron = None
        self.__waitList = []

  # Predicates ---------------------------------------------------------------

  # returns: True when book is already loaned out, False otherwise (bool)
    def isCheckedOut(self):
        return bool(self.__patron)

  # invokes len()
  # returns: True if Patron(s) are waiting for book, False otherwise (bool)
    def isReserved(self):
        return len(self.__waitList) > 0

  # params: patron - a particular patron (Patron)
  # returns: True when Patron has checked out book, False otherwise (bool)
    def hasBook(self, patron):
        return self.__patron == patron

  # params: patron - a particular patron (Patron)
  # returns: True when given Patron is on waiting list, False otherwise (bool)
    def isInWaitList(self, patron):
        return patron in self.__waitList

  # Both return and lend
  # returns: True when previous transaction is "returned" and current 
  #            transaction is "lend", False otherwise (bool)  
    def __isTwoPartStatus(self):
        return "returned" in self.__transactionStatus and "\n" not in\
           self.__transactionStatus

  # Accessors ----------------------------------------------------------------

  # returns: title of book (str)
    def getTitle(self):
        return (self.__title)

  # returns: author of book (str)
    def getAuthor(self):
        return (self.__author)

  # returns: Patron who has checked out book (Patron)
    def getPatron(self):
        return self.__patron

  # returns: record of latest book transaction (str)
    def getTransactionStatus(self):
        return str(self.__transactionStatus)

  # invokes: str()
  # returns: str representation of waiting list for book (str)
    def getWaitListStr(self):
        ret = ""
        for patron in self.__waitList:
            ret += str(patron) + '\n'
        return ret
  # Mutators -----------------------------------------------------------------

  # This method delegates all responsibilities to private methods of class
  # invokes: hasBook(), isInWaitList(), canCheckOutBooks(), isCheckedOut(),
  #          __lendBook(), __putInWaitList(), and __setTransactionStatus()
  # params:  patron - patron trying to borrow book (Patron)
    def borrowMe(self, patron):
        if self.hasBook(patron) or self.isInWaitList(patron):
            self.__setTransactionStatus(patron.getName(), Book.INVALID)
        elif patron.canCheckOutBooks():
            if not self.isCheckedOut():
                self.__lendBook(patron)
                self.__setTransactionStatus(patron.getName(), \
                                            Book.SUCCESSFUL)
            else:
                self.__putInWaitList(patron)
                self.__setTransactionStatus(patron.getName(), Book.WAIT)
        else:
            self.__setTransactionStatus(patron.getName(), Book.UNSUCCESSFUL)

  # Return book: release current patron, try to lend to waiting patron
  # This method delegates all responsibilities to private methods of class
  # invokes: isCheckedOut(), isReserved(), getName(),
  #          __resetPatron,(), __lendToNextPatron(), and
  #          __setTransactionStatus()
    def returnMe(self):
        if self.isCheckedOut():
            self.__setTransactionStatus(self.__patron.getName(),\
                                        Book.RETURNED)
            self.__resetPatron()
            if self.isReserved():
                self.__lendToNextPatron()
        else:
            self.__setTransactionStatus("Unknown", Book.INVALID)

  # invokes: increment() (Patron class)
  # params: patron - Patron borrowing book (Patron)
    def __lendBook(self, patron):
        patron.increment()
        self.__patron = patron

  # invokes: decrement() (Patron class)
    def __resetPatron(self):
        self.__patron.decrement()
        self.__patron = None

  # Lend book to waiting patron if eligible; if not, remove from wait List
  # invokes: isCheckedOut(), isReserved(),
  #          pop() (from list), borrowMe()
    def __lendToNextPatron(self):
        if not self.isCheckedOut() and self.isReserved():
            self.borrowMe(self.__waitList.pop(0))

  # params:  patron - Patron to put in waiting list (Patron)
  # invokes: append() (to list)
    def __putInWaitList(self, patron):
        self.__waitList.append(patron)

  # Creates string describing latest transaction
  # Combines name of patron participation in transaction with
  #   status of most recent transaction and title of this book 
  # params: name - name of Patron participating in transaction (str)
  #         index - index of transaction in TRANS_STATUS (int)
  # invokes: __isTwoPartStatus()
    def __setTransactionStatus(self, name, index):
        if self.__isTwoPartStatus:
          self.__transactionStatus = name + Book.TRANS_STATUS[index] + \
                               self.__title
        else:
          self.__transactionStatus = ""

  # Comparators --------------------------------------------------------------

  # Already written for you:
  # Include these in order to sort Book objects


  # Shows how two Books can be compared with respect to the < relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when they are not same Book and other is Book object and
  #            title of this Book is lexicographically lower than title of
  #            other Book, False otherwise (bool)"""   
    def __lt__(self, other):
        return (not self is other) and (type(self) == type(other)) and \
               self.__title < other.__title

  # Shows how two Books can be compared with respect to the == relationship
  # params:  other - another object
  # invokes: type()
  # returns: True when both are same Book or both are Book objects and
  #            title and author are equal, False otherwise (bool)
    def __eq__(self, other):
        return self is other or \
               (type(self) == type(other) and \
                self.__title == other.__title) and\
                self.__author == other.__author

  # Convert to Str -----------------------------------------------------------

  # invokes:  str(), getWaitListStr()
  # returns:  str representation of Book object (str)
    def __str__(self):
        
        return "Title: %s \nAuthor: %s \n%s\nWait List: %s" % (self.__title,\
                                                            self.__author,\
                                                            str(self.__patron) if self.__patron else "Not Checked Out"
                                                            ,self.getWaitListStr())
