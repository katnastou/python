import re

url_regex = re.compile(r'https?://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})[-a-zA-Z0-9@:%_\+.~#?&//=]*')
match = url_regex.search("http://www.youtube.com/videos")
print(match.group(0)) #print entire string
print(match.group(1)) #print first match