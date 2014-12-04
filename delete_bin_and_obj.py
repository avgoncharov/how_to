import os
import shutil
# settings: src dir 
sSrc='.'   

def show_all(sSrc,iDirs=0,iFiles=0): 
    for file in os.listdir(sSrc): 
        # full pathname  
        file=os.path.join(sSrc,file)   
        if not os.path.isdir(file):
            continue
        iDirs += 1
        if '\\bin' in file or '\\obj' in file:
            #shutil.rmtree(file, ignore_errors=True)
            print ('['+file+']')
        else:
            iDirs,iFiles=show_all(file,iDirs,iFiles) 		  
        #else: 
             #else files 
         #    print (' '+file )
          #   iFiles+=1 
    return iDirs,iFiles

iDirs,iFiles=show_all(sSrc,0,0)   

print (""" total dirs: """,iDirs,""" total files: """,iFiles)
