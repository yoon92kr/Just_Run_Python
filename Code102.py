import pandas as pd

data = {
    'name': ['yoon', 'sang', ' hyun'],
    'job': ['father', 'mother', 'son'],
    'age':   ['35', '34',  '1']
}

famil = pd.DataFrame(data)

print(famil)
