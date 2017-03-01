

from libraryModule import StringGeneratorForDictionaries


class Library:

#-- Class Variables ----------------------------------------------------

  # Index when book not in library
  NOT_IN_LIBRARY = 0

  # Index when book added to library
  ADD = 1

  # Index when book removed from library
  REMOVE = 2

  # Index when patron not a member of library
  NOT_A_MEMBER = 3

  # Index when patron becomes member of library
  JOIN = 4

  # Index when patron ends membership in library
  LEAVE = 5

  # Index when book information is accessed
  ACCESS = 6

  # Index when patron information is accessed
  LOOK_UP = 7

  # Most recent transaction with respect to either a book or a patron
  TRANS_STATUS = [" is not in library",
                  " has been added to the library",
                  " has been removed from the library ",
                  " is not a library member ",
                  " has been added as a library member",
                  " has been removed as a library member",
                  " has been accessed", 
                  " member files have been accessed"]

  #-- Constructor --------------------------------------------------------

  # Creates new dictionaries to hold books and patrons
  # params:  name - name of Library(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__books (dict of Book)  and
  #              self.__patrons() (dict of Patron) to empty dictionaries,
  #              self.__transactionStatus (str) to TRANS_STATUS with respect to
  #                book participating in transaction or
  #                patron participating in transaction 
  def __init__(self, name):
    self.__name = name
    self.__books = {}
    self.__patrons = {}
    self.__transactionStatus = Library.TRANS_STATUS[0]

#-- Accessors ----------------------------------------------------------

  # returns:  name of library (str)
  def getName(self):
    return self.__name 

  # returns:  record of latest transaction (str)
  def getTransactionStatus(self):
    return self.__transactionStatus 

  # params:  title of Book (str)
  # invokes:  inLibrary(), __setTransactionStatus()
  # returns:  Book stored in library (Book)
  def getBook(self, title):
    book = None
    if self.inLibrary(title):
      book = self.__books[title]
      self.__setTransactionStatus(title, "", Library.ACCESS)
    else:
      self.__setTransactionStatus(title, "", Library.NOT_IN_LIBRARY)
    return book

  # params: name of Patron who is member of library (str)
  # invokes:  isMember(),  __setTransactionStatus()
  # returns:  name of Patron (Patron) or None
  def getPatron(self, name):
    patron = None
    if self.isMember(name):
      patron = self.__patrons[name]
      self.__setTransactionStatus("", name, Library.LOOK_UP)
    else:
      self.__setTransactionStatus("", name, Library.NOT_A_MEMBER)
    return patron
  #return name
  
#-- Predicates ---------------------------------------------------------

  # Checks if book is in library
  # params: title - title of Book to search for in library (str)
  # returns:  True if in library, False otherwise (bool)
  def inLibrary(self, title):
    return title in list(self.__books.keys())

  # Checks if person is member of library
  # params: name - name of Patron to search for in library (str)
  # returns:  True if member of library, False otherwise (bool)
  def isMember(self, patronName):
    return patronName in list(self.__patrons.keys())

  # Checks if library has any books
  # invokes:  len()
  # returns:  True if library has any books, False otherwise (bool)
  def hasBooks(self):
    return len(list(self.__books.keys())) > 0

  # Checks if library has any members
  # invokes:  len()
  # returns:  True if library has any members, False otherwise (bool)
  def hasMembers(self):
    return len(list(self.__patrons.keys())) > 0

#-- Mutators -----------------------------------------------------------

  # Set status for latest transaction  
  # params:  title - title of Book participating in transaction (str)
  #          name = name of Patron participating in transaction (str)
  #          Note:  one of the above should be an empty string
  #          index into TRANS_STATUS (int)
  def __setTransactionStatus(self, title, name, index):
    self.__transactionStatus = title + name + Library.TRANS_STATUS[index]

  # Adds book to library using its title as a key  
  # params:  book - new Book to be added to library (Book)
  # invokes:  getTitle() (Book), __setTransactionStatus()
  def addBook(self, book):
    self.__books[book.getTitle()] = book
    self.__setTransactionStatus("", str(book.getTitle()), Library.ADD)

  # Removes the patron and returns borrowed books if any
  # params:  name - name of Patron to remove from library (str)  
  # invokes:  pop() (list),
  #           hasCheckedOutBooks() (Patron) 
  #           getPatron (Book), returnMe (Book)
  #           isMember(), __setTransactionStatus()
  def removePatron(self, name):
      if self.isMember(name):
        valuesPatron = self.__patrons.pop(name, None)
        self.__setTransactionStatus('',name,Library.LEAVE)
        if valuesPatron.hasCheckedOutBooks():
          for book in list(self.__books.values()):
            if book.getPatron() == valuesPatron:
              book.returnMe()
      else:
        self.__setTransactionStatus('',name,Library.NOT_A_MEMBER)

  # Removes book from library and releases borrower if applicable
  # params:  title - title of Book to remove from library (str)
  # invokes:  pop() (list),
  #           isCheckedOut() (Book), getPatron (Book)
  #           decrement () (Patron)
  #           inLibrary(), __setTransactionStatus()      
  def removeBook(self, title):
    if self.inLibrary(title):
      valuesBook = self.__books[title]
      if valuesBook.isCheckedOut():
        patronOnBook = valuesBook.getPatron()
        patronOnBook.decrement()
      self.__setTransactionStatus(title,'',Library.REMOVE)
      self.__books.pop(title, None)

  # Adds patron to library using its name as a key
  # params:  patron - new Patron to add to library (Patron)
  # invokes:  getName (Patron), __setTransactionStatus()
  def addPatron(self, patron):
    self.__patrons[patron.getName()] = patron
    self.__setTransactionStatus("", patron.getName(), Library.JOIN)

#-- Convert to Str -----------------------------------------------------

  # Generates string representation of library
  # creates:  StringGeneratorForDictionaries objects
  # invokes:  str(), getName(), hasBooks(), hasMembers(),
  #           getDictString() (StringGeneratorForDictionaries)
  # returns:  str representation of Library object (str)  
  def __str__(self):
    bookDict = StringGeneratorForDictionaries(self.__books, "Books")
    x = bookDict.getDictString()
    nameDict = StringGeneratorForDictionaries(self.__patrons, "Patrons")
    y = nameDict.getDictString()
    return "%s\n%s\n%s" % (self.__name, x if self.hasBooks() else "There\
are no books in the library", y if self.hasMembers() else "There are no \
members in the library")

