import os
from typing import List
file_struct={
    "src/":{
        "models/": None,
        "routes/": None,
        "services/": None,
        "app.py": None
    },
    ".gitignore": None,
    "dockerfile": None,
    "main.py": None,
    "readme.md": None,
    "requirements.txt": None
    
}
def create_file(path,filename):
    with open(f'{path}/{filename}','w') as file:
        file.write("")    
        
def create_folder(path,foldername):
    os.mkdir(f'{path}/{foldername}')
    
def folder_struct(path:str,struct_dict:dict):
        
            
        
        
if __name__ in "__main__":
   #create_file('.','test.py')
 create_folder('.','test')