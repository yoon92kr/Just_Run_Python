import re, Code094

English ='i am a boy. i like meat. i love meat. give me meat'

Korean = '나는 남자다. 나는 고기를 좋아한다. 나는 고기를 사랑한다. 고기를 달라'

Korean_list = re.split('\.', Korean)
English_list = re.split('\.', English)

print(Korean_list)

total = []
total.append
for i in range(len(English_list)):
    total.append([English_list[i], Korean_list[i]])
Code094.writecsv("Korean_english.csv", total)