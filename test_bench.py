days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = "Sunday"
new_days = days_of_the_week.copy()
popper = days_of_the_week.index(day.lower())

for _ in range(len(days_of_the_week[:])):
    new_days.insert(_, new_days.pop(popper))
    popper += 1
    if popper == 7:
        break

print(new_days)

f'''A timer has been set for {f"{hrs:02d}:{mins:02d}:{secs:02d}" if hrs > 0 else f"{f'{mins:02d}:{secs:02d}' if mins > 0 else f'{secs} seconds'}"}!'''