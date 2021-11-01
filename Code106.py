import Code094
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 회귀분석

df = pd.read_csv('survey.csv')

male = df.income[df.sex == 'm']
female = df.income[df.sex == 'f']

result_1 = stats.levene(male, female)

if result_1[1] > .05:
    print('P value는 %f 로 95 수준에 유의하지 않음' %result_1[1])

else :
    print('P value는 %f 로 95 precent 수준에서 유의함' %result_1[1])

print ('남성', round(male.mean(),2), '여성', round(female.mean(),2), '\n등분산감정 결과 LevenResult(F) : %.3f p-value : %.3f' % (result_1))

model = smf.ols(formula= 'jobSatisfaction ~ English + stress + income', data = df)
result = model.fit()
print(result.summary())
