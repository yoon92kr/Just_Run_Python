import pandas as pd

family_df = pd.read_csv('family.csv')
family_add_df = pd.read_csv('family_new.csv')
family_df.append(family_add_df, ignore_index= True)
print(family_df)

mean_age = family_df['나이'].mean().astype('int')
family_df['나이'].fillna(mean_age, inplace=True)


family_df.to_csv('가족.csv', index= False)
family_df.to_json('가족.json') 
