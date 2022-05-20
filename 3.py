letter = input("Введите строчную латинскую букву: ")
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("Гласная.")
elif letter == 'y':
    print("Может быть как гласной, так и согласной.")
else:
    print("Согласная.")