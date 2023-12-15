def add_time(start, duration, start_day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute
    total_minutes += duration_hour * 60 + duration_minute
    
    # Calculate new time and days
    new_hour = total_minutes // 60 % 12
    new_minute = total_minutes % 60
    new_period = "PM" if total_minutes // 60 >= 12 else "AM"
    
    # Adjust for 12-hour clock format
    if new_hour == 0:
        new_hour = 12
    
    # Calculate days later
    days_later = total_minutes // (12 * 60)
    
    # Adjust for next day or multiple days later
    if days_later == 1:
        days_str = " (next day)"
    elif days_later > 1:
        days_str = f" ({days_later} days later)"
    else:
        days_str = ""
    
    # Calculate the day of the week if provided
    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_str = f", {new_day}"
    else:
        day_str = ""
    
    # Format the result
    new_time = f"{new_hour}:{new_minute:02} {new_period}{day_str}{days_str}"
    
    return new_time
