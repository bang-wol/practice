# 이동할 수 있는 경우의 수 카운트
current = input()
y = int(current[1])
x = int(ord(current[0])) - int(ord('a')) + 1
# ord() 함수 : 문자의 아스키 값 반환

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1),
         (2, 1)]

result = 0
for step in steps:
  ny = y + step[0]
  nx = x + step[1]
  if ny >= 1 and ny <= 8 and nx >= 1 and nx <= 8:
    result += 1

print(result)
