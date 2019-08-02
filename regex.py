import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None
    
def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)
    #if there is nothing it returns an empty list

# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False


def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False
    
#(extract_phone("my number is 432 567-8976"))
#print(extract_phone("my number is 432 567-897622"))

#print(extract_all_phones("my number is 432 567-8976 or call me at 678 890-9037"))



print(is_valid_phone("432 567-8976"))
print(is_valid_phone("432 567-8976 asd"))
print(is_valid_phone("asd 432 567-8976"))

