def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"The text word count is: {word_count(text)}" )
    characters = count_occurence_of_characters(text)
    list_of_characters = break_up_characters(characters)
    list_of_characters.sort(reverse=True, key=sort_on)
    report_character_occurrence(list_of_characters)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

def count_occurence_of_characters(text):
    lowered_text = text.lower()
    #create dictionary of string (key) -> Integer (value)
    characters = {}
    #Loop through text each character (split by character if necessary)
    #for character in text: / 
    for i in range(0, len(lowered_text)):
        #checks that character is a letter
        if lowered_text[i].isalpha():
            if lowered_text[i] in characters:
                new_value = characters.get(lowered_text[i])
                new_value = new_value + 1
                characters.update({lowered_text[i]: new_value})
        #else add character to dictionary w/ value 1
            else:
                characters.update({lowered_text[i]: 1})
    return characters

def break_up_characters(characters):
    letters = []
    for character, count in characters.items():
        temp_dictionary = {'character': character, 'count': count}
        letters.append(temp_dictionary)
    return letters

def sort_on(dictionary):
    return dictionary["count"]

def report_character_occurrence(list):
 for item in list:
    print("The %(character)s character was found %(count)s times." % item)

main()
