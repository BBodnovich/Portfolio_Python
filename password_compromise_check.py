'''
Docstring
'''

from getpass import getpass
from hashlib import sha1
import sys
from requests import get


API_URL = 'https://api.pwnedpasswords.com/range/'
TIMEOUT = 10


def get_password():
    password = getpass(prompt='What is your password? ')
    return password


def request_api_data(query_characters):
    url = API_URL + query_characters
    response = get(url, timeout=TIMEOUT)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status}')
    return response


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def check_password(password):
    sha1password = sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = check_password(password)
        if count:
            print(f'{password} was found {count} times.')
        else:
            print(f'{password} was NOT found.')
    return 'Done!'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(sys.argv)

    else:
        main([get_password()])
