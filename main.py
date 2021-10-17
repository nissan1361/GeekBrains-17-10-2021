from pythonping import ping


# 1
print('TASK1 *************')

word1 = 'разработка'
word1_utf = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
word2 = 'сокет'
word2_utf = '\u0441\u043e\u043a\u0435\u0442'
word3 = 'декоратор'
word3_utf = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

# тип строковых переменных
print(type(word1))
print(type(word2))
print(type(word3))

# юникод
print(word1_utf)
print(word2_utf)
print(word3_utf)

# тип юникода
print(type(word1_utf))
print(type(word2_utf))
print(type(word3_utf))

# 2
print('TASK2 *************')

b_word1 = b'class'
b_word2 = b'function'
b_word3 = b'method'

print(type(b_word1))
print(len(b_word1))
print(b_word1)

print(type(b_word2))
print(len(b_word2))
print(b_word2)

print(type(b_word3))
print(len(b_word3))
print(b_word3)

# 3
print('TASK3 *************')

w1 = b'attribute'
# w2 = b'класс'
# w3 = b'функция'
w4 = b'type'
print('В байтовом типе невозможно записать слова: \n "класс", "функция"')

# 4
print('TASK4 *************')

str1 = 'разработка'
str1_bytes = str1.encode('utf-8')
print(str1_bytes)
str1_new = str1_bytes.decode('utf-8')
print(str1_new)

str2 = 'администрирование'
str2_bytes = str2.encode('utf-8')
print(str2_bytes)
str2_new = str2_bytes.decode('utf-8')
print(str2_new)

str3 = 'protocol'
str3_bytes = str3.encode('utf-8')
print(str3_bytes)
str3_new = str3_bytes.decode('utf-8')
print(str3_new)

str4 = 'standard'
str4_bytes = str4.encode('utf-8')
print(str4_bytes)
str4_new = str4_bytes.decode('utf-8')
print(str4_new)

# 5
print('TASK5 *************')
# МОЙ ПРОВАЙДЕР БЛОКИРУЕТ ПИНГ с помощью DNS :(
# ping('https://yandex.ru/', verbose=True)
print('МОЙ ПРОВАЙДЕР БЛОКИРУЕТ ПИНГ с помощью DNS :(')

# 6
print('TASK6 *************')
f = open('test_file.txt', 'r')
print(f)
data = f.read()
print(data)
f.close()
