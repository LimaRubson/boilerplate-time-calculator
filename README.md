# Time Calculator

This is the boilerplate for the Time Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator


# My collaboration in the project:

# Add Time Function

This Python function, `add_time`, takes in a start time, a duration time, and an optional starting day of the week. It adds the duration time to the start time and returns the result, considering both the 12-hour clock format and the day of the week.

## Functionality

### Parameters

- **start:** A start time in the 12-hour clock format (ending in AM or PM).
- **duration:** A duration time that indicates the number of hours and minutes.
- **start_day (optional):** A starting day of the week (case insensitive).

### Output

- The function adds the duration time to the start time and returns the result.
- If the result is the next day, it shows `(next day)` after the time.
- If the result is more than one day later, it shows `(n days later)` after the time, where "n" is the number of days later.
- If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. The day of the week in the output appears after the time and before the number of days later.

### Examples

```python
from add_time import add_time

# Example Usage
result = add_time("3:00 PM", "3:10")
# Returns: "6:10 PM"

result = add_time("11:30 AM", "2:32", "Monday")
# Returns: "2:02 PM, Monday"

result = add_time("11:43 AM", "00:20")
# Returns: "12:03 PM"

result = add_time("10:10 PM", "3:30")
# Returns: "1:40 AM (next day)"

result = add_time("11:43 PM", "24:20", "tueSday")
# Returns: "12:03 AM, Thursday (2 days later)"

result = add_time("6:30 PM", "205:12")
# Returns: "7:42 AM (9 days later)"
