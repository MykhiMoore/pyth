Customer_name = input("welcome, what is your name? " )
starting_balance = 5000.25
def start_balance_greet(user_name, balance):
    print(f"Hello {user_name} you're starting balance is {balance}.")
start_balance_greet(Customer_name, starting_balance)
pay_check =float(input("how much of your paycheck would you like to deposit"))
expenditure_item = input("looks like you went shopping what did you buy? ")
# print(expenditure)
expenditure = float(input(f"how much does {expenditure_item} cost"))
ending_balance = starting_balance + pay_check - expenditure
print(ending_balance)