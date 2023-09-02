import os 
import shutil
from_dir = "C:/Users/admin/Downloads/C102_assets-main"
to_dir = "C:/Users/admin/Desktop/Coding/Pro 102/assets"
list_files = os.listdir(from_dir)
print(list_files)

for file_name in list_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+file_name
        if os.path.exists(path2):
            print("moving"+file_name+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+".....")
            shutil.move (path1,path3)

