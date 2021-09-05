# 시간 기반으로 반복
import time

output = 0
target_tik = time.time() + 5


while time.time() < target_tik:
    output += 1
    print("5초 동안 반복한 횟수 : {}".format(output))

