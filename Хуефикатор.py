word = input("Введите слово, указав ударение большой буквой: ")
word.index('')
for number in range(len(word)):
    if word[number] in 'УЕЫАОЭЯИЮ':
        break
    if number == len(word):
        print("Вы не указали ударение!")
        word = input("Введите слово, указав ударение большой буквой: ")
print(word[number])
