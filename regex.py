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

# Pattern for Time stamps in 12-hour or 24-hour format
pattern5 = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
timeStamps = re.findall(pattern5, file_content)
print("Time Stamps found:", timeStamps)

# Pattern for HTML tags matches
pattern6 = r'<\/?[a-zA-Z][a-zA-Z0-9\s"\'=.-]*>'
html_tags = re.findall(pattern6, file_content)
print("HTML Tags found:", html_tags)