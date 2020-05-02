from collections import Counter
text_ = input("Введите слова через пробел: ")
print (sorted(Counter(text_.replace(' ', '')).most_common()))