#!/usr/local/bin/python3
from subprocess import call
from subprocess import check_output
import os
import shutil
os.chdir('./hitcon-ctf')
while "zip" or "bz2" in os.listdir():
	try:
		fn=(check_output(["ls | grep 'zip\|bz2\|gz'"],shell=True)).strip().decode()
		if "zip" in fn.split()[-1]:
			call(['unzip',fn])
		elif "bz2" in fn.split()[-1]:
			call(['tar','-xvf',fn])
		elif "gz" in fn.split()[-1]:
			call(['tar','-xvf',fn])
	except:
		for each in os.listdir():
			if "zip2" or "gz" in check_output(['file',each]):
				print(check_output(['file',each]))
				os.rename(each,each+".bz2")
				continue
			elif "zip" in check_output(['file',each]).decode().strip():
				os.rename(each,each+".zip")
				continue
	try:
		new_dir=(check_output(["ls -l | grep 'drw'"],shell=True).decode()).split(' ')[-1].strip()
		new_f=(os.listdir(new_dir)[0])
	except:
		continue
	try:
		src_dir=new_dir+"/"+new_f
		shutil.move(src_dir,".")
	except shutil.Error:
		rename=src_dir+".bz2"
		os.rename(src_dir,rename)
		shutil.move(rename,".")
		os.rmdir(rename)
		os.remove(fn+".bz2")
		continue
	os.rmdir(new_dir)
	os.remove(fn)
