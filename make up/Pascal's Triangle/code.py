s = 9
listed = []
second_listed = []
final_answer = []
for i in range(s + 1):
    boolean_variable = False
    second_listed = []
    second_listed.append(1)
    if i - 1 > 0:
        for j in range(i - 1):
            if boolean_variable:
                break
            for k in range(len(listed)):
                if k + 1 == len(listed):
                    boolean_variable = True
                    break
                else:   
                    second_listed.append(listed[k] + listed[k + 1])

    if i != 0:
        second_listed.append(1)
    final_answer.append(second_listed)
    listed = second_listed

for i in range(len(final_answer)):
    print(str(i) + ":", end="---------------------------")
    print("---" * (len(final_answer) - 1 - i), end = "")
    for j in range(len(final_answer[i])):
        print(final_answer[i][j], end = "     ")
    print()

