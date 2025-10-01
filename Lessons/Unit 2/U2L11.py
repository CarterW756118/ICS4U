def date(_input):
    (year, month, day) = _input.split("-")
    date_tuple = (int(year), month, int(day))
    return date_tuple

def print_date_tuple(date_tuple):
    (year, month, day) = date_tuple
    suffix = "th"
    if day % 10 == 1 and day != 11:
        suffix = "st"
    if day % 10 == 2 and day != 12:
        suffix = "nd"
    if day % 10 == 3 and day != 13:
        suffix = "rd"
    print("Today's date is the %d%s of %s, %d" % (day, suffix, month, year))
    
date_tuple = date(input("Enter a date in the form 2025-Sep-19: "))
print(date_tuple)
print_date_tuple(date_tuple)
