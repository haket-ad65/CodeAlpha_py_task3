import os
import shutil

old_directory="c:/Users/dell/downloads"

file_type={
    "Documents" :['.docx', '.pdf', '.txt','.pptx', '.xlsx','.csv'],
    "Images" :['.jpeg','.jpg','.png','.gif'],
    "Videos" :['.mp4','.mov','.avi'],
    "Music" :['.mp3','.wav'],
    "Archives":['.zip','.tar','.gz'],
    "Scripts" :['.py', '.sh', '.cpp','.c','.html','.css' ],
    "Application":['.exe','.rdp','.msi'],
    }
def Oraganize_Myfiles(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exists...")
        return
    
    for filename in os.listdir(directory):
        paths =os.path.join(directory,filename)

        if os.path.isdir(paths):
            continue

        _, file_extension =os.path.splitext(filename)

        destination_dir =None
        for dir_name, extensions in file_type.items():
            if file_extension.lower() in extensions:
                destination_dir = os.path.join(directory, dir_name)
                break

        if destination_dir:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            shutil.move(paths,  destination_dir)
            print(f"Moved {filename} to {destination_dir}")
        else:
            print(f"No category found for {filename}. Skipping")
if __name__== "__main__":
    Oraganize_Myfiles(old_directory)