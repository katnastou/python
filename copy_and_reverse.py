'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(fname,newfname):
    contents =''
    with open(fname, "r") as old_file:
        contents += old_file.read()[::-1]
    with open(newfname, "w") as new_file:
        new_file.write(contents)
        

copy_and_reverse('story.txt', 'story_reversed.txt')