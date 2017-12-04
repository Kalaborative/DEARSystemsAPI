from datetime import datetime
my_date = input("Supply a date in the format MM-DD-YYYY: ")

d = datetime.strptime(my_date, "%m-%d-%Y")
print(d.isoformat())