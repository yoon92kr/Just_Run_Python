import pandas as pd

csv_filename = 'family.csv'
json_filename = 'family.json'

csv_filename.drop_duplicates(inplace = True)
# 파일의 모든열에 대한 중복성 검사 후 삭제, inplace 속성을 true 로 설정할경우 원본 데이터도 삭제

familyf_df = pd.read_csv(csv_filename)

print(familyf_df)
print()

print("pandas - head")
# 데이터들 중 처음 다섯 개의 데이터를 확인
print(familyf_df.head())
print()

print("pandas - info")
# 데이터의 갯수와 각 열에 대한 정보 출력
print(familyf_df.info())
print()

print("pandas - describe")
# 숫자 자료형 행의 통계적인 정보를 출력(max, count ...)
print(familyf_df.describe())
print()

print("pandas - tail")
# 마지막 다섯 개의 데이터를 확인
print(familyf_df.tail())


family_df = pd.read_json(json_filename)
print(family_df)
 
