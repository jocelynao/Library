'''
Rose Williams
rosew@binghamton.edu
CS110
Assignment 11
'''

# This module contains useful collaborating classes for libraries
# See if you can figure out how they work!

import pickle

DIVIDER = '\n' + ('-' * 70) + '\n'  # useful string for output

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# This is a utility class that generates a string representaion of an 
# entire dictionary"""
class StringGeneratorForDictionaries(object):

  #-- Constructor ------------------------------------------------------------
  
  #  Creates new string generator for given dictionary with given label
  def __init__(self, dictionary, dictionaryLabel):

    self.__dictionary = dictionary # dictionary
    self.__dictionaryLabel = dictionaryLabel # title of dictionary
 
  #-- Accessors --------------------------------------------------------------

  # Returns a string representation of the dictionary,
  # basically a 'to string' for dictionaries
  def getDictString(self):
    dList = list(self.__dictionary.values())
    dList.sort()
    return '\n' + self.__dictionaryLabel + ':\n' + \
           ('\n'.join(map(str, dList)))        
  
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    
# Binary file I/O class for libraries (Saves/loads BINARY NOT TEXT file)
class LibraryRecords(object):

  #-- Constructor ------------------------------------------------------------

  # Creates file I/O object for libraries
  # params:  fileName - name of physical file on storage media  
  def __init__(self, fileName):
    self.__fileName = fileName    # give it a .dat extension!

  #-- Accessors --------------------------------------------------------------

  # Loads library from file 
  # returns:  library that was stored in file
  def load(self):
    libraryFileObj = open(self.__fileName, 'rb')
    library = pickle.load(libraryFileObj)
    libraryFileObj.close()
    return library

  #-- Mutators ---------------------------------------------------------------

  # Creates binary representation of library and stores in file
  # params:  library - entire library object 
  def save(self, library):
    libraryFileObj = open(self.__fileName, 'wb')
    pickle.dump(library, libraryFileObj)
    libraryFileObj.close()
