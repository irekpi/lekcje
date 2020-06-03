# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.


def check_ten(n1,n2):
    return n1+n2 == 10


print(check_ten(10,0))

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.


def check_ten_sum(n1,n2):
    if n1+n2 == 10:
        return True
    else:
        return n1+n2


print(check_ten_sum(1,9))


# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.


def first_upper(mystring):
    mystring = mystring[0].upper()
    return mystring


print(first_upper('jez'))

# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)


def last_two(mystring):
    if len(mystring) < 2:
        return "error"
    else:
        return mystring[-1], mystring[-2]


print(last_two("wiertarka"))
print(last_two("e"))

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.



def seq_check(nums):

    seq = [1,2,3]
    for number in nums:
        for item in seq:
            if number == item:
                return True
            else:
                return "not in list"

print(seq_check([444,4]))


# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**


def compare_len(s1,s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:
        dif = len_s1 - len_s2
        return dif, "roznica"
    if len_s1 < len_s2:
        dif = int(len_s2) - len_s1
        return dif, "roznica"
    else:
        return "rowne"


print(compare_len('janek', 'janek'))
