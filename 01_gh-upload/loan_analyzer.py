# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

"""
loan_costs = [500, 600, 200, 1000, 450]

loan_count = len(loan_costs)
loan_total = sum(loan_costs)
loan_average = loan_total/loan_count

print("Total number of loans:", loan_count)
print(f"Total loan cost: ${loan_total}")
print(f"Average loan cost: ${loan_average:.2f}")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Using get() function to retrieve future value & remaining months
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Printing future value and remaining months of the loan
print(f"Future value of the loan: ${future_value}")
print("Months remaining on loan:", remaining_months)


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.

present_value = future_value / (1 + .20/remaining_months)


# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.

# Retrieving loan price from "loan" dictionary
loan_price = loan.get("loan_price")

if present_value >= loan_price:
    print("Loan worth at least the cost to buy.")
else:
    print("Loan too expensive; not worth the price")



"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

def calc_pv(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/remaining_months)

    return present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

annual_discount_rate = .2

present_value = calc_pv(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan is: {present_value:.2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    loan_price = loan.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan_price)

# @TODO: Print the `inexpensive_loans` list
print("The list of inexpensive loans (from loan list):", inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
