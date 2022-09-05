
array_words = []
count_words = int(input("Введите количество слов: "))

for item in range(count_words):
    word =input("Введите слово (on english): ")
    array_words.append(word)

min_item = '0'*1000
for item in array_words:
    if item < min_item:
        min_item = item

for item in range(len(array_words)-1):
     for j in range(len(min_item)):
         if array_words[item][:j] == array_words[item+1][:j]:
             prefix = array_words[item][:j]

if len(prefix) >= 2:
    print(prefix)
else:
    print("''")