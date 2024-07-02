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