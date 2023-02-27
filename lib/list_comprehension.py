#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [num for num in num_list if num % 2 == 0]
    return(even_elements)
    print(even_elements)

# return_evens(num_list=[0, 1, 3, 5, 7, 8, 9, 10])

def make_exclamation(sentence_list):
    exclaimed_list = [item + "!" for item in sentence_list]
    print(exclaimed_list)
    return(exclaimed_list)


# make_exclamation(["Hello", "I'm doing great", "Python is fun"])
