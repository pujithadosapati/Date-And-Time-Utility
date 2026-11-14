from datetime import date, datetime, timedelta
# 1. Calculate Age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
# 2. Calculate Days Between Two Dates
def days_between(date1, date2):
    return abs((date2 - date1).days)
# 3. Calculate Working Days
def working_days(start_date, end_date):
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    count = 0
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)
    return count
# 4. Format Date and Time
def format_datetime():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%d-%m-%Y %H:%M:%S"))
    print("Date:", now.strftime("%d %B %Y"))
    print("Time:", now.strftime("%I:%M %p"))
# Validate Date Input
def get_date(message):
    while True:
        try:
            value = input(message)
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date! Enter in YYYY-MM-DD format.")
# Main Program
while True:
    print("\n===== DATE AND TIME UTILITY =====")
    print("1. Calculate Age")
    print("2. Days Between Two Dates")
    print("3. Calculate Working Days")
    print("4. Display Formatted Date and Time")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        dob = get_date("Enter your date of birth (YYYY-MM-DD): ")
        print("Your Age:", calculate_age(dob), "years")

    elif choice == "2":
        d1 = get_date("Enter first date (YYYY-MM-DD): ")
        d2 = get_date("Enter second date (YYYY-MM-DD): ")
        print("Days Between Dates:", days_between(d1, d2))

    elif choice == "3":
        start = get_date("Enter start date (YYYY-MM-DD): ")
        end = get_date("Enter end date (YYYY-MM-DD): ")
        print("Working Days:", working_days(start, end))

    elif choice == "4":
        format_datetime()

    elif choice == "5":
        print("Thank you for using Date and Time Utility!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
