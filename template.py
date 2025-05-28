import os 
from pathlib import Path

file_dir = 'src'

 
file_list = [
    f'{file_dir}/__init__.py'
]

for filepath in file_list:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir.strip() != " ":
        os.makedirs(filedir,exist_ok='True')
    if ( not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
    else:
        logging.debug("Unable to create the files")
