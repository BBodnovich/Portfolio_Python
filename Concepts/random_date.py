import datetime
import random

def generate_random_date(number_of_days):
    """Returns a list of number random date objects for birthdays."""

    day_list = []
    current_year = datetime.datetime.today().year
    start_of_year = datetime.date(current_year, 1, 1)

    for _ in range(number_of_days):
        random_day_offset = datetime.timedelta(random.randint(0, 364))
        random_day = start_of_year + random_day_offset
        day_list.append(random_day)

    return day_list
