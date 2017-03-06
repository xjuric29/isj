#!/usr/bin/env python3

import re


def first_task():
    # trivialni ukol 1 - 1 bod
    objects = 'Mars Jupiter Uran Neptun Pluto'
    tests1 = ['Mars Jupiter Uran Neptun Pluto', 'Jupiter Uran Neptun', 'Jupiter', 'Mars', 'Neptun', 'Uran']
    for test in tests1:
        if re.search(r'^.*\b(Jupiter|Mars|Neptun|Uran)\b.*$', objects).group(1) == test:

            assert True
        else:

            assert False


def second_task():
    # trivialni ukol 2 - 1 bod
    tests2 = ['999==666', '987==987', '765==765', '666==666']
    for test in tests2:
        if re.search(r'([987]{3}|[654]{3})==\1', test):
            assert True
        else:
            assert False


def third_task():
    # mene trivialni ukol - 3 body
    punct = re.compile(r'''(moje reseni  # after a full stop or comma
                            (vyuziva     # ...
                            ))''', re.X)
    assert punct.sub(' ', 'Hello,John.I bought 192.168.0.1 for 100,000 bitcoins') == 'Hello, John. I bought 192.168.0.1 for 100,000 bitcoins'


first_task()
second_task()
third_task()
