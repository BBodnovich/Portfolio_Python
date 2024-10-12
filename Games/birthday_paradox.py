"""Birthday Paradox Simulation
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem"""

import datetime
import random


def introduction():
    """Print the introduction for the Birthday Paradox game"""

    print('''
Birthday Paradox

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
    ''')


def generate_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""

    birthday_list = []
    current_year = datetime.datetime.today().year
    start_of_year = datetime.date(current_year, 1, 1)

    for _ in range(int(number_of_birthdays)):
        random_day = datetime.timedelta(random.randint(0, 364))
        random_birthday = start_of_year + random_day
        formatted_date = random_birthday.strftime('%b %d')
        birthday_list.append(formatted_date)

    return birthday_list


def find_duplicates(birthdays_list):
    """Return a sorted list of duplicate birthdays."""

    match = list({i for i in birthdays_list if birthdays_list.count(i) > 1})
    return sorted(match)


def simulate_matches(number_of_birthdays):
    """Return the match count in 100000 simulations given the number of birthdays"""

    simulated_match_count = 0
    for i in range(100000):
        if i % 10000 == 0:
            print(f'{i} simulations run...')

        sim_birthdays = generate_birthdays(number_of_birthdays)
        sim_repeat_birthdays = find_duplicates(sim_birthdays)

        if len(sim_repeat_birthdays) > 1:
            simulated_match_count +=1

    return  simulated_match_count


def main():
    """Run the main program for simulating the Birthday Paradox"""

    introduction()

    while True:
        print('How many birthdays shall I generate? (Max 100)')
        num_birthdays = input('> ')

        if num_birthdays.isdecimal() and (0 < int(num_birthdays) <= 100):
            break

    birthdays = generate_birthdays(num_birthdays)
    print(f'\nHere are {num_birthdays} birthdays:')
    print(', '.join(birthdays))

    repeat_birthdays = find_duplicates(birthdays)

    if len(repeat_birthdays) > 1:
        print(f'\nIn this simulation, multiple people have a birthday on {", ".join(repeat_birthdays)}\n')
    else:
        print('\nIn this simulation, nobody shares a repeat birthday\n')

    print(f'Generating {num_birthdays} random birthdays 100,000 times...')
    input('Press Enter to begin...')
    print('\nLets run another 100,000 simulations.')

    simulated_match = simulate_matches(num_birthdays)
    print(simulated_match)

    probability = round(((int(simulated_match) / 100000) * 100), 2)
    print(f'\nOut of 100,000 simulations of {num_birthdays} people, there was a matching birthday')
    print(f'in that group {simulated_match} times. This means that {num_birthdays} people ')
    print(f' have a {probability} % chance of having a matching birthday in their group')


if __name__ == '__main__':
    main()
