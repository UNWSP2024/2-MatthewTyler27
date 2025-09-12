#Average Age
#Matthew Tyler 09/12
def average_age():
    # Get User Input for all friends' ages
    Age1 = int(input("Enter age of friend 1"))
    Age2 = int(input("Enter age of friend 2")) 
    Age3 = int(input("Enter age of friend 3"))
    Age4 = int(input("Enter age of friend 4"))
    Age5 = int(input("Enter age of friend 5"))

    # Sum ages
    Age_Total = (Age1 + Age2 + Age3 + Age4 + Age5)
    # Average the ages
    Ave_age = Age_Total/5
    # Print the results
    print('the average age of your friends:', Ave_age)
# Line which calls the above function.
average_age()
