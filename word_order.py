n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    # word_dict[word] = word_dict.get(word, 0) + 1
    word_dict[word] = word_dict[word] + 1 if word in word_dict else 1
    word_list.append(word)

# print(n)
# print(word_dict)
# print(word_list)
print(len(word_dict))
print(' '.join([str(x) for x in word_dict.values()]))
