
import os
import stat

def get_file_info(file_path):
    '''
    Get and Print file's infomation
    '''
    try:
        file_path = os.stat(file_path)
        file_info = {
            
        }
    except OSError:
        print('\nNameError : [%s] No such file or directory\n', file_path)



