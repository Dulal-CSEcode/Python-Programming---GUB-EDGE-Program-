short_name = input("Enter short name of a week (e.g., Mon, Tue, etc.): ").lower()

weekdays = {
    'mon': 'Monday',
    'tue': 'Tuesday',
    'wed': 'Wednesday',
    'thu': 'Thursday',
    'fri': 'Friday',
    'sat': 'Saturday',
    'sun': 'Sunday'
}

if short_name in weekdays:
    print(f"It is {weekdays[short_name]}")
else:
    print("Invalid input! Please enter a valid short name of the week.")
