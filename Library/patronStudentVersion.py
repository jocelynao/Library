


class Patron:
    
  # Class Variables ----------------------------------------------------------

  # Maximum number of books Patron can take out (int)
    NUM_BOOKS_BORROW = 3
  # Current status of this Patron (str)
  # Will be combined with name of Patron
    STATUS = ["can borrow up to 3 books", "can borrow two more books", \
            "can borrow one more book", "must return book(s)"]

  # Constructor --------------------------------------------------------------

  # params:  name - name of Patron(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__numBooksOut (int) to 0, and self.__status() (str)
  #                to STATUS[0]
    def __init__(self, name):
        self.__status = Patron.STATUS[0]
        self.__name = name
        self.__booksOut = 0

  # Predicates ---------------------------------------------------------------

  # True if less then max books checked out, False otherwise
    def canCheckOutBooks(self):
        return self.__booksOut < Patron.NUM_BOOKS_BORROW

  # True if books checked out, False otherwise
    def hasCheckedOutBooks(self):
        return self.__booksOut > 0

  # Accessors ----------------------------------------------------------------

  # returns: name (str)
    def getName(self):
        return self.__name

  # returns: status (str)
    def getStatus(self):
        return str(self.__status)

  # returns: number of books out (int)
    def getNumBooksOut(self):
        return self.__booksOut
    
  # Mutators -----------------------------------------------------------------

  # set to STATUS indexed by number of books out
    def __updateStatus(self):
        self.__status = Patron.STATUS[self.__booksOut]

  # invokes: updateStatus()
    def increment(self):
        self.__booksOut = self.__booksOut + 1
        self.__updateStatus()

  # invokes updateStatus()
    def decrement(self):
        self.__booksOut = self.__booksOut - 1
        self.__updateStatus()

  # Comparators --------------------------------------------------------------

  # Already written for you:
  # You will need to include these in order to sort Patron objects

  # Shows how two Patrons can be compared with respect to the < relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when they are not the same Patron and other is a Patron
  #          object and name of this Patron is lexicographically less than 
  #          name of other Patron, False otherwise (bool)
    def __lt__(self, other):
        return (not self is other) and (type(self) == type(other)) and \
           self.__name < other.__name

  # Shows how two Patrons can be compared with respect to the == relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when both are same Patron OR both are Patron objects AND
  #          all attributes are equal, False otherwise (bool)
    def __eq__(self, other):
        return self is other or \
           (type(self) == type(other) and \
            self.__name == other.__name and \
            self.__status == other.__status and \
            self.__numBooksOut == other.__numBooksOut)
    
# Convert to str ---------------------------------------------------    
    def __str__(self):
        return "%s %s, %s book(s) out" % (self.__name, self.__status, \
                                          self.__booksOut)
