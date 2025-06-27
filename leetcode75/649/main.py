senate = "DRRDRDRDRDDRDRDR"

result = [1] * len(senate)
countRadiant = 0
countDire = 0


i = 0
while i < len(senate):
    if result[i] == 0:
        i += 1
    elif result[i] != 0 and (i == len(senate) - 1) and senate[i] != senate[0]:
        result[0] = 0
        i += 1
    elif result[i] != 0 and (i == len(senate) - 1) and senate[i] == senate[0]:
        i += 1
    elif result[i] != 0 and senate[i] != senate[i + 1]:
        result[i + 1] = 0
        i += 1
    elif result[i] != 0 and senate[i] == senate[i + 1]:
        i += 1
    else:
        i += 1

print(result)

for i in range(len(result)):
    if result[i] == 1 and senate[i] == 'R':
        countRadiant += 1
    elif result[i] == 1 and senate[i] == 'D':
        countDire += 1

if countRadiant > countDire:
    print('Radiant')
else:
    print('Dire')
