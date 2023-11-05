import shutil
import os
import datetime

source_dir = '/path/to/source_directory'
backup_dir = '/path/to/backup_directory'
backup_folder_name = datetime.datetime.now().strftime('%Y-%m-%d') #folder with current date
backup_path = os.path.join(backup_dir, backup_folder_name)

if not os.path.exists(backup_path):
    os.makedirs(backup_path)

for root, dirs, files in os.walk(source_dir):
    for file in files:
        source_file = os.path.join(root, file)
        destination_file = os.path.join(backup_path, os.path.relpath(source_file, source_dir))
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        shutil.copy2(source_file, destination_file)
        print(f'Copied: {source_file} to {destination_file}')

print('Backup completed.')
