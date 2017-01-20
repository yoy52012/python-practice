import os
import zipfile

def zip_files(dirname, zipfilename):

    full_zipfilename = os.path.abspath(zipfilename)
    full_dirname = os.path.abspath(dirname)
    print('Start to zip {} to {}...'.format(full_dirname, full_zipfilename))
    if not os.path.exists(full_dirname):
        print("Directory [{}] does not exist.".format(full_dirname))
        return

    if os.path.isdir(full_zipfilename):
        tempname = os.path.basename(full_zipfilename)
        full_zipfilename = os.path.join(full_zipfilename, tempname)
    if os.path.exists(full_zipfilename):
        print("[{}] has already exist, do you still want to zip the files? ".format(full_zipfilename))


    filelist = []

    for dirpath, dirnames, filenames in os.walk(full_dirname):
        if len(filenames) == 0:
            filelist.append(dirpath)
        else:
            for filename in filenames:
                filelist.append(os.path.join(dirpath, filename))

    mzip_file = zipfile.ZipFile(full_zipfilename, 'w', zipfile.ZIP_DEFLATED)
    for mfile in filelist:
        if os.path.isdir(mfile):
            temp = zipfile.ZipInfo(os.path.basename(mfile)+'\\')
            print(mfile)
            mzip_file.writestr(temp, "")
        else:
            mzip_file.write(mfile, mfile[len(dirname):])
    mzip_file.close()

def main():
    '''
    Call the main method
    '''
    zip_files(r'C:\Users\okieM\Desktop\image', r'C:\Users\okieM\Desktop\python\python.zip')

if __name__ == "__main__":
    main()


    
