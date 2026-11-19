# Project No.: 5
# Author: Mridul Hasan
# Description: Check the compressed character list to check whether it;s a palindrome.


def check_palindrome(compressed_list):
    """Return True if the letters read the same forward and backward."""
    return compressed_list == compressed_list[::-1]
