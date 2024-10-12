def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count(text)
    total_words = word_count(text)
    print(f"{total_words} is the amount of words found")
    
def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return  f.read()

def word_count(text):
    words = text.split()
    count = 0
    for i in words:
        count+=1
    return count
  #  return len(words)
def character_count(text):
    character_counted = {}
    for i in text:
        for j in i.lower():
            if j.isalpha():
                if j in character_counted:
                    character_counted[j]+=1
                else:
                    character_counted[j] = 1
 #   print(character_counted)
    for key,value in character_counted.items():  
        print(f"The {key} character was found {value} times")
   # print(f"The character_counted[j]}
main()

