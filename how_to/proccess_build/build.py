"""
The MIT License (MIT)

Copyright (c) 2014 Goncharov Andrey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
def do_build():    
    import os
    res = os.system("cd repo_dir&&git pull origin branch")    
    
	curr_dir = "report_dir"
	
    if res != 0:
        with open("{0}log.txt".format(curr_dir), "w") as log:
            log.write("Git update failed.")        
        return    
    
    res = os.system("del /F {0}result.txt".format(curr_dir))
    if res != 0:
        with open("{0}log.txt".format(curr_dir), "w") as log:
            log.write("Can't remove result.txt.")        
        return

    res = os.system("{0}clear.cmd".format(curr_dir))
    if res != 0:
        with open("{0}log.txt".format(curr_dir), "w") as log:
            log.write("Cleaning failed.")        
        return    

    res = os.system("{0}exec_build.cmd>{0}result.txt".format(curr_dir))
    if res != 0:
        with open("{0}log.txt".format(curr_dir), "w") as log:
            log.write("Build failed.")            

    res = os.system("python {0}convert_to_html.py".format(curr_dir))
    if res != 0:
        with open("{0}log.txt".format(curr_dir), "w") as log:
            log.write("Converting to html failed.")            
        return

    print("Ok")        
    return

do_build()
    
    

        
    



