# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:07:46 2021.

Use  recursive binary search to locate an item in an array.

@author: Tindi.Sommers
"""

import numpy as np

def binary_search(data, key, start, end):
    """Perform binary search of data looking for key."""
    
    middle = (start + end + 1) // 2  # middle element index
    print(middle) # debugging
    print() # debugging
    
    if end == start: #  if there is only one element left
        print(middle, 'in if') # debugging
        if data[middle] == key:
            return middle
        else:
            return (-1) # return -1 if key not found
    
    if data[middle] == key:
        print('here') # debugging purpose
        return middle
    elif key < data[middle]:
        end = middle - 1
        return binary_search(data, key, start, end)
    else:
        start = middle + 1
        return binary_search(data, key, start, end)



def main():
    # create and display array of random values
    data = np.random.randint(10, 91, 10)
    data.sort()
    print(data, '\n')

    search_key = int(input('Enter an integer value (-1 to quit): ')) 

    # repeatedly input an integer; -1 terminates the program
    while search_key != -1:
        location = binary_search(data, search_key, 0, len(data) - 1)  # perform search
        print(location)
        if location == -1:  # not found
            print(f'{search_key} was not found\n') 
        else:
            print(f'{search_key} found in position {location}\n')

        search_key = int(input('Enter an integer value (-1 to quit): '))

# call main if this file is executed as a script
if __name__ == '__main__':
    main()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
