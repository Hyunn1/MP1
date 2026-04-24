total_seconds = int(input("Enter the total number of seconds: "))

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

days = total_seconds // seconds_per_day
remainder = total_seconds % seconds_per_day

hours = remainder // seconds_per_hour
remainder = remainder % seconds_per_hour

minutes = remainder // seconds_per_minute
seconds = remainder % seconds_per_minute

print(f"The equivalent time is {days}:{hours:02d}:{minutes:02d}:{seconds:02d}")