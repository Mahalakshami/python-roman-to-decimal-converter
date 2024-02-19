# Define a function to convert Roman numerals to decimal numbers
def roman_to_decimal(roman):
    # Create a dictionary mapping Roman numerals to their decimal values
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize a variable to store the decimal equivalent
    decimal = 0
    
    # Iterate over the Roman numeral string in reverse order
    for i in range(len(roman) - 1, -1, -1):
        # If the decimal value of the current character is less than the previous character, subtract its value
        if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
            decimal -= roman_numerals[roman[i]]
        else:
            # Otherwise, add its value to the total
            decimal += roman_numerals[roman[i]]

    # Return the final decimal equivalent
    return decimal

# Get user input for a Roman numeral
roman_input = input("Enter a Roman numeral: ").upper()

# Call the conversion function and display the result
try:
    decimal_equivalent = roman_to_decimal(roman_input)
    print(f"Decimal equivalent: {decimal_equivalent}")
except KeyError:
    # Handle the case where an invalid Roman numeral is entered
    print("Error: Invalid Roman numeral entered.")
