import re
import datetime


def main():
	print_header()
	birthday = get_birthday_from_user()
	number_of_days = compute_days_between_dates(birthday)
	print_birthday_info(number_of_days)


def is_valid(birthday):
	if re.match(r'\d{4}/\d{1,2}/\d{1,2}', birthday):  # yyyy/mm/dd
		return True
	else:
		return False


def get_birthday_from_user():
	birthday = input("When is your birthday?[yyyy/mm/dd]: ")
	if not is_valid(birthday):
		print("It is not accepted format.")
		exit()
	return birthday


def print_header():
	print("-------------------------------------------------")
	print("           HOW DAYS OLD YOU ARE?")
	print("-------------------------------------------------")
	print()


def compute_days_between_dates(birthday):
	year, month, date = birthday.split('/')
	birthday = datetime.date(int(year), int(month), int(date))
	today = datetime.datetime.today().date()
	# print(type(birthday), birthday)
	# print(type(today), today)
	number_of_days = (today - birthday).days
	return number_of_days


def print_birthday_info(number_of_days):
	print("{} days has passed since you were born.".format(number_of_days))


if __name__ == '__main__':
	main()
