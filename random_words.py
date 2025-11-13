ramdom_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "violet grape", "watermelon", "xigua", "yellow passionfruit", "zucchini"]

count_of_char = {}


for i in ramdom_words:
    for j in i:
        if j in count_of_char:
            count_of_char[j] += 1
        else:
            count_of_char[j] = 1

# the most frequent latter
max_count = 0
max_char = ""
for i in count_of_char:
    if count_of_char[i] > max_count:
        max_count = count_of_char[i]
        max_char = i

count_of_char.sort(key=lambda x: x[1], reverse=True)

print(count_of_char)

print(max_char, max_count)
