# 객체 object : 여러가지 속성을 가질 수 있는 대상
# list 안에 dictionary를 대입

students = [
    {"name":"윤인성", "korean":87, "math":98, "english":88, "science" : 95 },
    {"name":"연하진", "korean":92, "math":98, "english":96, "science" : 98 },
    {"name":"구지연", "korean":76, "math":96, "english":94, "science" : 90 },
    {"name":"나선주", "korean":98, "math":92, "english":96, "science" : 92 },
    {"name":"윤아린", "korean":95, "math":98, "english":98, "science" : 98 },
    {"name":"윤명월", "korean":64, "math":88, "english":92, "science" : 92 },
    {"name":"김미화", "korean":82, "math":86, "english":98, "science" : 88 },
    {"name":"김연화", "korean":88, "math":74, "english":78, "science" : 92 },
    {"name":"박아현", "korean":97, "math":92, "english":88, "science" : 95 },
    {"name":"서준서", "korean":45, "math":52, "english":72, "science" : 78 }
   
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / (len(student)-1)
    print(student["name"], score_sum, score_avg, sep="\t")
  
