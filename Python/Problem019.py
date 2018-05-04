import operator
years = range(1901, 2001);
daysInMonth = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

totalDays = 0;
contLeap = 0;
for year in years:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        # print (year);
        totalDays += 1;
    for days in daysInMonth:
        # print month, days
        totalDays += days;

# sorted_x = sorted(daysInMonth.items(), key = operator.itemgetter(0))
print totalDays;
# print(daysInMonth)
