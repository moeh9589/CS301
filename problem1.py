# CS 301 Assignment 1
from itertools import permutations


def problem1():

    sum = 0
    for i in range(n + 1):
        sum += 1
    return sum


def problem2(desiredword):

    fin = open("words.txt")

    for word in fin:
        word.strip()
        if word == desiredword:
            print(word)


# def problem3():
#
#     fin = open("words.txt")
#     letter_list = ["a", "p", "p", "l", "e"]
#     perm = permutations(letter_list)
#     list(perm)
#
#     for i in perm:
#         for j in fin:
#             if j == i:
#                 print(i)
#                 print('***')

problem2("apple")

#problem3()
