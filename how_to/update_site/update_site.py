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
# This script creates backup and updates site(or service) by simply copying of files and directories.
import os
import sys
import time

SOURCE_DIR = sys.argv[1]
SITE_DIR = sys.argv[2]
BACKUP_DIR = sys.argv[3]
ZIP_NAME = time.strftime("%Y_%m_%dT%H_%M_%S")


def stop_iis():
	res = os.system("iisreset /STOP")
	if res != 0:
		print("Can't strop IIS.")
		sys.exit(2)


def start_iis():
	res = os.system("iisreset /START")
	if res != 0:
		print("Can't start IIS.")
		sys.exit(3)


def on_remove_tree_error_handler(funciton, path, error_inf):
	print(error_inf)
	os.system("7z x -y -o{0}\ {1}\\{2}.7z".format(SITE_DIR, BACKUP_DIR, ZIP_NAME))
	start_iis()
	sys.exit(5)


def backup_site(backup_dir, zip_name, site_dir):
	if not os.path.exists(backup_dir):
		os.mkdir(backup_dir)
	res = os.system("7z a {0}\\{1}.7z {2}\\*".format(backup_dir, zip_name, site_dir))
	if res != 0:
		print("Can't create backup.")
		start_iis()
		sys.exit(4)

	import shutil
	shutil.rmtree("{0}".format(site_dir), False, on_remove_tree_error_handler)
	os.mkdir(site_dir)


def update(source_dir, backup_dir, zip_name, site_dir):
	res = os.system("xcopy /Y /E {0}\\* {1}".format(source_dir, site_dir))
	if res != 0:
		os.system("7z x -y -o{0}\ {1}\\{2}.7z".format(site_dir, backup_dir, zip_name))
	return res

#-------------------------------------------------------------------------------------------------------------
#main function
def update_site():
	stop_iis()
	backup_site(BACKUP_DIR, ZIP_NAME, SITE_DIR)
	result = update(SOURCE_DIR, BACKUP_DIR, ZIP_NAME, SITE_DIR)
	start_iis()
	sys.exit(result)
#-------------------------------------------------------------------------------------------------------------

update_site()