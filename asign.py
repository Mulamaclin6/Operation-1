def math_operations(w, z):
    """
    This function takes two numbers as input and performs the following tasks:
    - Calculates the sum of the two numbers using a lambda function and returns it.
    - Calculates the product of the two numbers using a lambda function and returns it.

    Parameters:
    w (int, float): The first number.
    z (int, float): The second number.

    Returns:
    tuple: A tuple containing the sum and the product of the two numbers.
    """
    sum_operation = lambda x, y: x + y
    product_operation = lambda x, y: x * y
    
    return sum_operation(w, z), product_operation(w, z)

def main():
    # Get sample numbers from user input
    w = int(input("Enter the first number: "))
    z = int(input("Enter the second number: "))
    
    # Call the math_operations function with the sample numbers
    sum_result, product_result = math_operations(w, z)
    
    # Print the returned sum and product
    print(f"The sum of {w} and {z} is: {sum_result}")
    print(f"The product of {w} and {z} is: {product_result}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
