import os
import sys
import csv
from bs4 import BeautifulSoup

claude_api_output = sys.argv[1]
claude_response_file = 'photos_claude_description.csv'

claude_response_list = []

for filename in os.listdir(claude_api_output):
    if filename.endswith('.md'):
        file_path = os.path.join(claude_api_output, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            # dictionary to store the tag and its corresponding text
            data_dict = {}
            data_dict['File'] = filename.replace('_claude_description.md', '')
            
            # find all the tags and their corresponding text
            for tag in soup.find_all():
                data_dict[tag.name] = tag.text
            
            claude_response_list.append(data_dict)

# write the data to the csv file
with open(claude_response_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=claude_response_list[0].keys())
    writer.writeheader()
    for data in claude_response_list:
        writer.writerow(data)




