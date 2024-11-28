# Function to display a welcome message to the user
def welcome_message():
    print("Welcome to the Python Expense Tracker!")
    
# Function to log a new expense entry
def log_expense():
    # Ask the user for the expense amount and validate it
    amount = float(input("Enter expense amount: "))
    while amount <= 0:
        print("Please enter a positive number.")  # Ensure the amount is positive
        amount = float(input("Enter expense amount: "))

    # Define the available categories and ask the user to choose one
    categories = ["Food", "Transport", "Entertainment", "Others"]
    print(f"Available categories: {categories}")
    
    # Validate that the user selects a valid category
    category = input("Enter the category: ")
    while category not in categories:
        print("Invalid category. Try again.")  # Ensure the category is valid
        category = input("Enter the category: ")
    
    # Ask for a description of the expense
    description = input("Enter expense description: ")
    
    # Return the expense data as a dictionary
    return {"amount": amount, "category": category, "description": description}

# Initialize an empty list to store all expenses
expenses = []

# Function to store an expense in the expenses list
def store_expense(expense):
    expenses.append(expense)  # Add the expense dictionary to the list

# Function to display a summary of all expenses
def display_summary(expenses):
    # Calculate the total amount spent across all expenses
    total_spent = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spent: ${total_spent:.2f}")  # Display total spending

    # Calculate and display the amount spent in each category
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        # Accumulate the total amount per category
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    
    print("\nAmount spent per category:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")  # Display spending per category

    # Display the detailed list of all expenses
    print("\nDetailed Expense List:")
    for exp in expenses:
        print(f"{exp['category']}: ${exp['amount']:.2f} - {exp['description']}")

# Function to display a thank-you message when the program ends
def thank_you_message():
    print("\nThank you for using the Python Expense Tracker!")

# Main function to control the overall program flow
def main():
    welcome_message()  # Display the welcome message at the start
    while True:
        # Log and store each expense
        expense = log_expense()
        store_expense(expense)
        
        # Ask if the user wants to add another expense
        another = input("Add another expense? (yes/no): ").lower()
        if another != "yes":
            break  # Exit the loop if the user doesn't want to add more expenses

    # Display the summary of all logged expenses
    display_summary(expenses)
    thank_you_message()  # Display the thank-you message before exiting

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
