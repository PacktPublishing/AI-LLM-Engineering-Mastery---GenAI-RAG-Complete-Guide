from datetime import datetime, timedelta

now = datetime.now()
print(f" Current date and time {now}")

future_date = now + timedelta(days=10)
print(f"Date 10 days from now: {future_date}")

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted current date and time: {formatted_date}")
