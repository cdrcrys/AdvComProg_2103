fname = input("Enter your fathre's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday (YYYY-MM-DD): ")

from datetime import datetime

birth_date = datetime.strptime(birthday, '%Y-%m-%d')
current_date = datetime.now()
age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

print(f"{fname}'s age is {age} years old. He was born in {birthplace}.")