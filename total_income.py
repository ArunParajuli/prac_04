def generate_income_report(incomes, num_months):
    """Generate and print the income report."""
    # Print the header for the income report
    print("\nIncome Report\n-------------")
    total = 0  # Initialize total income to zero
    # Iterate over each month
    for month in range(1, num_months + 1):
        income = incomes[month - 1]  # Get the income for the current month
        total += income  # Add the income for the current month to the total
        # Print the income and total for the current month
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []  # Initialize an empty list to store incomes
    num_months = int(input("How many months? "))  # Get the number of months from the user

    # Loop to input income for each month
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Get income for the current month
        incomes.append(income)  # Add the income to the list of incomes

    generate_income_report(incomes, num_months)  # Generate and print the income report


if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
