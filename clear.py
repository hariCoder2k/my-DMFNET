import os

def delete_files_except_pkl(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            # Check if the file is a .pkl file, if not, delete it
            if not file.endswith('.pkl'):
                print(f"Deleting: {file_path}")
                os.remove(file_path)

# Replace 'path_to_your_data2_directory' with the actual path to your 'data2' directory
data2_path = './Train/'

# Delete files in 'HGG' directory
delete_files_except_pkl(os.path.join(data2_path, './HGG'))

# Delete files in 'LGG' directory
delete_files_except_pkl(os.path.join(data2_path, './LGG'))

