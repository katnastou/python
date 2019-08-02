'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(fname,newfname):
    with open(fname, "r") as old_file:
        contents = old_file.read()
    with open(newfname, "w") as new_file:
        new_file.write(contents)

        