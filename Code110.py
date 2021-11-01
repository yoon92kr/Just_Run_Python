import Code094
import numpy as n
quest = n.array(Code094.switch(Code094.opencsv('quest.csv')))

quest[quest > 5] = 5
print(quest)

Code094.writecsv('resultcsv.csv', list(quest))
