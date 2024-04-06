import sys
import os
import exiftool
import csv

# python location_history.py photos
photos_folder_path = sys.argv[1]

# location history output file
location_history_file = 'location_history.csv'

# Extract the 'Create Date' and 'GPS Position'
metadata_list = []

for filename in os.listdir(photos_folder_path):
    if filename.endswith('.jpeg'): # or HEIC
        file_path = os.path.join(photos_folder_path, filename)
        print(f"Processing {file_path}")
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(file_path)
            #print(f"{file_path}: {metadata}")
            create_date = metadata[0]['EXIF:DateTimeOriginal'] # 2023:11:11 16:55:35
            gps_position = metadata[0]['Composite:GPSPosition'] # 37.7600027777778 -122.426941666667
            # print(f"{file_path}: {create_date}, {gps_position}")
            metadata_list.append([filename, create_date, gps_position])

with open(location_history_file, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File', 'Create Date', 'GPS Position'])
    for md in metadata_list:
        writer.writerow(md)
