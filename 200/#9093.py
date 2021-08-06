testcase = int(input())
sentences = []

for _ in range(testcase):
    sentence = input()
    sentences.append(sentence.split(" "))

for x in sentences:
    for y in x:
        print(y[::-1], end=' ')
    print()
