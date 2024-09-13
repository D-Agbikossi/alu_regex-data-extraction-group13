#!/usr/bin/python3

# Import python regular expression library
import re

# Open and read the data file
with open('data.txt', 'r') as file:
    file_content = file.read()

# Pattern for email address and find matches
pattern1 = r'[A-Za-z0-9-_.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}'
email = re.findall(pattern1, file_content)

# Print result
print("Emails found:", email)

# Repeat procces for URLs
pattern2 = r'https?:\/\/[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})(?:\/[^\s]*)?'
url = re.findall(pattern2, file_content)
print("URLs found:", url)
