#Matthew Tyler
#09/12/25
def temp_conversion(celsius):

    #enter formula
    fahrenheit = (9/5)*celsius + 32
    # Return the variable to the calling function
    return fahrenheit

#if statement to get the user's temperature and assign values
if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
    # Get the Celsius temperature.
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    # Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
