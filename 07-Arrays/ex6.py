def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

for day in [1, 4, 7]:
    print(f"Day {day}: {weekday(day)}")
