file_name = "test.txt"
word_length = int(input("Enter desired word length: "))

file = open(file_name, 'r')
content = file.read()
file.close()

words = content.split()

print(f"Words with length {word_length}:")
for word in words:
    cleaned_word = ""
    for char in word:
        if char.isalpha():
            cleaned_word += char
    
    if len(cleaned_word) == word_length:
        print(cleaned_word)