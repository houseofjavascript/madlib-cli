from textwrap import dedent

greeting = dedent(
    """
    ***************************************************
    **             Welcome to Madlib!                **
    **    Please see the game instructions below.    **
    **        This will be a word prompt game.       **
    **    I will prompt you for a word and you 
                  will give  me a reply
    **        To quit at any time, type "quit"       **
    ***************************************************
    """
)

def read_template():
    with open("game.txt", "r") as file:
        file_contents = file.read().strip()
        return file_contents


def parse_template():
    pass


adjectives = []
txt = "It was a {Adjective} and {Adjective} {Noun} {Plural Noun}."
txt_split = txt.split()
print("This the string split", txt_split)
for word in txt_split:
    if word.startswith("{") and word.endswith("}"):
        print(word)
        adjectives.append(word)
        # results = results.replace(word, "{}")

    print(adjectives)

# This section invokes functions
# print(greeting)
contents = read_template()
# print(contents)


# create a variable called adjectives =[]

# create a variable called visited_characters = ""
visited_character = ""
# create a variable called temp_word_to_capture = ""
temp_word_to_capture = ""
# create a variable called capturing = false
capturing = false
# for loop through each letter in the text
# for ea character in txt


# if the character is not an "{", add the character to the visited_characters
if not char == "{"
    visited_character += char

# if the character is an "{" ,
# add the character to visited_characters
if char == "{"
    visited_character += char
    capturing = true
else:
    temp_word_to_capture += char
if char == "}"
    adjectives.append(temp_word_to_capture)
    capturing = false
    visited_character += char
return visited_character

# change capturing = true
# if capturing = true, add character to temp_word_to_capture
# if character is a "}", add the character to visited_characters
# append temp word to adjectives
# turn capturing = false
# return visited_characters
