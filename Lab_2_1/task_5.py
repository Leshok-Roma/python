print("Введите два слова")
word1 = input().lower()
word2 = input().lower()

letters1 = [a for a in word1]
letters2 = [a for a in word2]
letters1.sort()
letters2.sort()
print("True") if letters1 == letters2 else print("False")

