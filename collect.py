from searcher import *
from scraper import *
import pandas as pd

#states to search through
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine', 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',
         'Oklahoma','Oregon','Pennsylvania','Rhode Island',
         'South  Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming']

fields = ['Title', 'Style:', 'WEIGHTED', 'IBU', 'CALORIES', 'ABV', 'Descr', 'Place']

state_error = []

for state in states:
    links = []
    rows = []
    try:
        links = search_state(state)
        for i, link in enumerate(links):
            print(i)
            row = extract_info(link, fields, state)
            rows.append(row)
        df = pd.DataFrame(rows, columns=fields)
        df.to_csv('data_' + state + '.csv', encoding='utf-8', index=False)
    except:
        state_error.append(state)

print(state_error)

#df.to_csv('data2.csv', encoding='utf-8', index=False)
