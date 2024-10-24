import os

def rename_min_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('-min.png'):
            new_filename = filename.replace('-min.png', '.png')
        elif filename.endswith('-min.jpg'):
            new_filename = filename.replace('-min.jpg', '.jpg')
        elif filename.endswith('-min.jpeg'):
            new_filename = filename.replace('-min.jpeg', '.jpeg')
        else:
            continue
        
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} to {new_filename}')

# Usage
directory_path = 'C://Users//mahnoor//Documents//compressed_static//projects'
rename_min_files(directory_path)
