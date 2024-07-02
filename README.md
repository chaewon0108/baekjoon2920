# baekjoon2920

🍀 들어가며 ...
> 이번 방학에는 코딩테스트 준비를 하기 위해 학교에서 하는 일명 pps 캠프를 신청했다.
c언어는 익숙한데, 이번에는 파이썬을 제대로 해보기 위해서 파이썬으로 코딩을 해보고자 한다!
아마 print, scan부터 찾아가며 시작해야 할 것 같다!
4주동안 80문제 이상 풀고, 다른 학우의 코드를 리뷰해야 하는데 모쪼록 끝까지 완주할 수 있길 바란다.
나자신 화이팅!

---

# 문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

## 입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.


---

##  내가 생각한 과정

1. 사용자가 입력한 8개 숫자 입력받기
2. 8개의 숫자들을 배열에 정리
3. 반복문을 통해서 순차적으로 배열에 있는 숫자를 확인
4. 반복문 안에 조건문을 통해서 ascending, descending, minxed로 판별하기

---
# 사용할 파이썬 문법 정리
## 1. 입력받기
```
num = input()
print (num)
```
- input을 num에 저장 가능

## 2. 배열 형변환
```
input_string = num
input_list = input_string.split()
int_list = list(map(int, input_list))
```
- 입력받은 input을 Input_string에 저장하고
- 이것을 split()를 사용해서 int로 변환 전 공백을 처리함
- int_list = list(map(int, input_list))를 통해 ['1,', '2,', '3']에서 [1,2,3]으로 변환함

## 3. for문 (in python)
```
for 카운터변수 in range(반복횟수):
    반복해서 실행할 명령
```
- 이 문법을 사용하여 for문을 정의할 수 있음


---
# 결과
```
num = input()  # 사용자 숫자 입력받기

input_string = num
input_list = input_string.split()
int_list = list(map(int, input_list))

ascending = True
descending = True

for i in range(len(int_list) - 1):
    if int_list[i] + 1 != int_list[i + 1]:
        ascending = False
    if int_list[i] - 1 != int_list[i + 1]:
        descending = False

if ascending:
    result = "ascending"
elif descending:
    result = "descending"
else:
    result = "mixed"

print(result)
```
<img width="708" alt="image" src="https://github.com/chaewon0108/baekjoon2920/assets/174469937/7b6a5cb0-0e60-4949-933a-d86f60599baa">


