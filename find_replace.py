'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

# def find_and_replace(fname, word_bef, word_after):
#     text =""
#     with open(fname, "r") as file:
#          lines = file.readlines()
#          for line in lines:
#             words = line.split(" ")
#             for word in words:
#                 if word == word_bef:
#                     text += word_after
#                 else:
#                     text += word
#                 text += " "
#             text += "\n"
#     with open(fname, "w") as file:
#         file.write(text)
 
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()