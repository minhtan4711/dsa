temperatures = [73,74,75,71,69,72,76,73]
# [1,1,4,2,1,1,0,0]

answers = [0] * len(temperatures)
stack = []

for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
            answers[stack[-1]] = i - stack[-1]
            stack.pop()
    stack.append(i)

print(answers)