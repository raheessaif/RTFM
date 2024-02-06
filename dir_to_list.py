import os

def save_folder_contents_to_file(folder_path, output_file):
    try:
        with open(output_file, 'w') as file:
            for root, dirs, files in os.walk(folder_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    file.write(file_path + '\n')
        print(f"Paths of contents saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# Replace 'your_folder_path' and 'output_file.list' with your actual folder path and desired output file name
folder_path = 'G:\\DATASETS\\UCF_CRIME\\UCF_CRIME_I3D\\UCF_Test_ten_crop_i3d'
output_file = 'list/ucf-i3d-test.list'

save_folder_contents_to_file(folder_path, output_file)
