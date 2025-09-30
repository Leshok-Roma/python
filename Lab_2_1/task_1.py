str= input(" Input string ").lower()
words = str.split() 
words_dict = {}
for word in words:
     if word in words_dict: 
         words_dict[word] += 1
     else : 
         words_dict[word] = 1
   
length = len(words_dict)
for i , j  in words_dict.items():
    print(f" word {i} : {j} ")
print(f"amount of unique words : {length}")
