# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:15:35 2021.

Recursive palindromes

@author: Tindi.Sommers
"""

def test_palindromes(txt):
    """Test if a string is a palindrome. Return true or false"""
    # clean the text: remove all white spaces
    txt = txt.strip().replace(' ', '')
    print(txt)
    
    def t_p(s):
        # base case. If the length of s is 1, return true. If there are two
        # characters remaining and they are the same, return true, else false
        if len(s) <= 1:
            return True
        elif len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        
        # if the first and last characters are the same, return true and
        # test the palindrome of the remaining middle text
        if s[0] == s[len(s) - 1]:
            return True and t_p(s[1:len(s) - 1])
        else:
            return False
    
    return t_p(txt)


if __name__ == '__main__':
    print(test_palindromes('jhyfurj'))