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
def add_build_failed(out_file):
    out_file.write("<div class='bg-danger'><h2>")
    out_file.write("Build FAILED.")
    out_file.write("</h2></div>")
    return

def add_build_success(out_file):
    out_file.write("<div class='bg-success'><h2>")
    out_file.write("Build success.")
    out_file.write("</h2></div>")
    return

def add_div(out_file, text, div_begin, div_end):
  out_file.write(div_begin)
  out_file.write(text)
  out_file.write(div_end)
  return

def add_buidl_result(out_file, content):
    build_err = "Build FAILED."
    
    for str in content:
        if build_err in str:
            add_build_failed(out_file)
            return

    add_build_success(out_file)            
    return

def add_started_at(out_file, content):
    for str in content:
        if "Build started " in str:
            add_div(out_file, str, "<div><h4>", "</h4></div>")
            return    

#-------------------------------------------------------------------------------------------
import time
import os

new_dir = "report_dir\\out\\{0}\\".format(time.strftime("%Y_%m_%dT%H_%M_%S"))

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

#-----------------------------------------------------------------------------------
html_begin = "<html><head><link rel='stylesheet' type='text/css' href='../../bootstrap-3.2.0-dist/css/bootstrap.css'></head><doby><div style='padding:20px'>\n"
html_end = "</div></body></html>"
w_begin = "<div class='bg-warning'>"
e_begin = "<div class='bg-danger'>"
build_er_begin = "<div class='bg-danger'><h4>"
build_s_begin = "<div><h4>"
build_s_end = "</h4></div>"
build_s = "Build succeeded."
build_err = "Build FAILED."
buidl_started_flag = False
#-----------------------------------------------------------------------------------

with open("report_dir\\result.txt") as in_file:
    content = in_file.readlines()

with open("{0}output_result.html".format(new_dir),"w") as out_file:
    out_file.write(html_begin);
    add_started_at(out_file, content)
    add_buidl_result(out_file, content)
        
    for str in content:
        if ": warning" in str and str[6] != '>':
            add_div(out_file, str, w_begin, "</div>")
            continue
        
        if "Warning(s)" in str:
            if str[4] != '0':
                add_div(out_file, str, w_begin, "</div>")
            else:
                add_div(out_file, str, "<div>", "</div>")
            continue
            
        if ": error" in str and str[6] != '>':
            add_div(out_file, str, e_begin, "</div>")
            continue
        
        if "Error(s)" in str:
            if str[4] != '0':
                add_div(out_file, str, e_begin, "</div>")
            else:
                add_div(out_file, str, "<div>", "</div>")
            continue

        if build_s in str:
            add_div(out_file, str, build_s_begin, build_s_end)
            buidl_started_flag = False
            continue

        if build_err in str:
            add_div(out_file, str, build_er_begin, build_s_end)
            buidl_started_flag = False
            continue

        if "Project " in str and "Done Building Project " not in str:
            if not buidl_started_flag:
                add_div(out_file, str, "<div>-----------------------------------------</div><div>", "</div>")
            else:
                add_div(out_file, str, "<div>", "</div>")
            buidl_started_flag = True
            continue

    out_file.write(html_end)

with open ("{0}Index.html".format("report_dir\\"), "w") as main_index:
    main_index.write(html_begin);
    for dirname, dirnames, filenames in os.walk('report_dir\\out\\'):
        if len(dirname[len("report_dir\\out\\"):]) > 0:            
            main_index.write("<div><a href='out/{0}/output_result.html'>Build at: {0}</a></div>".format(dirname[len("report_dir\\out\\"):]))

    main_index.write(html_end)
