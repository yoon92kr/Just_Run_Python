import pandas as pd

df2 = pd.read_csv('survey.csv')

print(df2.head())

print(df2.income.mean())
print(df2.income.sum())


print(df2.income.median())
#중간값 구하기

print(df2.income.describe())
# 수입 기초통계량
print(df2.describe())
# 데이터 프레임 기초통계량
print(df2.sex.value_counts())
print(df2.groupby(df2.sex).mean())
# 두 집단 평균 구하기
print(df2.groupby(df2.stress).mean())
