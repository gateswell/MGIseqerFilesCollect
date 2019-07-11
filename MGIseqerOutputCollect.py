#!/usr/bin/python
# -*- coding:utf-8 -*-

import re,os,sys
import time,datetime
from shutil import copyfile,copytree

def help_info():
	info='''
============================================================================
Usage:
	python MGIseqerOutputCollect.py <flowcell name> <ending date> <cycle:S001-S010,S101,S120|None> [outdir]
Examples:
	python MGIseqerOutputCollect.py V300018621 20190101 S001 D:\CopyData
	python MGIseqerOutputCollect.py V300018621 20190101 S001-S010 D:\CopyData
	python MGIseqerOutputCollect.py V300018621 20190101 S001-S010,S101,S120 D:\CopyData
	python MGIseqerOutputCollect.py V300018621 20190101 None D:\CopyData
Version:
	V1.0.1
Note:
	The Script can be run by python2 or python3 
	outdir will be created if outdir unexists, the default outdir is D:\CopyData
	write S001-S010,S101,S120 if wanna cycle 1 to 10 and cycle 101, 120 instead of writing None when no need copy any cycle
	contact caoshuhuan@yeah.net if any bug happened during runing.
Modify:
	1. add parameter: cycle 
	2. delete some redundant scripts
	3. fix some bugs
============================================================================
'''
	print(info.rstrip()) 
	exit(0)
	
if len(sys.argv)<4:	#outdir can be dismissed
	help_info()
	
def print_time():
	return time.strftime("[%Y-%m-%d %H:%M:%S] ",time.localtime())

def get_days(date,num=10):	#date format:20190101
	format_date=datetime.datetime(year=int(date[:4]),month=int(date[4:6]),day=int(date[6:]))	#2019-01-01
	#date=int(date)
	alldays=[]
	for i in range(num):
		be4day=format_date-datetime.timedelta(days=i)
		format_be4day=be4day.strftime("%Y%m%d")
		alldays.append(format_be4day)
		#print format_befday
	return alldays

def collect_cycles(cycle):	#S001-S003,S100,S152
	cycles=[]
	if cycle.upper() != 'NONE':
		if re.search(r',',cycle):
			for tmp in cycle.split(','):
				if re.search(r'-',tmp):	#S001-S003
					sta,end=tmp.split('-')	#S001 S003
					sta=int(sta.lstrip('S'))	#1
					end=int(end.lstrip('S'))	#3
					for i in range(sta,end+1):
						i="{:0>3d}".format(i)	#001 002 003
						cycles.append('S'+i)		#S001 S002 S003
				else:
					cycles.append(tmp)
		elif re.search(r'-',cycle):
			sta,end=cycle.split('-')
			sta=int(sta.lstrip('S'))
			end=int(end.lstrip('S'))
			for i in range(sta,end+1):
				i="{:0>3d}".format(i)
				cycles.append('S'+i)
		else:
			cycles.append(cycle)
	else:
		cycles=['None']
	return cycles
		
# copy chip png and tif files
def copy_DataThumbFOVFigs(dir,chipname,cycles,outdir):
	try :
		for lane in os.listdir(dir):
			#if lane != 'Metrics':
			if re.match(r'L',lane):
				if not os.path.exists(outdir+'\\'+chipname+'\\'+lane):
					os.makedirs(outdir+'\\'+chipname+'\\'+lane)
					
				if len(cycles) >= 1 and cycles[0].upper() != 'NONE': #&& cycle.upper() != 'NONE':
					for cycle in cycles:
						if not os.path.exists(outdir+'\\'+chipname+'\\'+lane+'\\'+cycle):	#add cycle directory
							os.makedirs(outdir+'\\'+chipname+'\\'+lane+'\\'+cycle)
						#for files in os.listdir(dir+'\\'+lane+'\\S001'):	v1.0.0
						for files in os.listdir(dir+'\\'+lane+'\\'+cycle):	#add cycle choose parameter
							#if files.startswith('Thumbnail'):	#copy thumbnail figures
							if re.search(r'C004R036|Thumbnail',files):
								#fullname=dir+'\\'+lane+'\\S001\\'+files
								fullname=dir+'\\'+lane+'\\'+cycle+'\\'+files
								outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+cycle+'\\'+files
								if not os.path.exists(outputname):
									copyfile(fullname,outputname)
									sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
							else:
								#sys.stdout.write('No such files: '+files+' \n')
								continue
				elif cycles[0].upper() == 'NONE':
					continue
				else:
					sys.stdout.write('wrong parameter been set! please check the cycle string, only None or format like: S001-S007,S100,S120 allowed!\n')
			else:
				continue
	except IOError as e:
		sys.stdout.write('No such dir: '+dir)
		raise e

def copy_Metrics(dir,chipname,outdir):	#copy Maps dir 
	try:
		if not os.path.exists(outdir+'\\'+chipname+'\\Metrics'):
			os.makedirs(outdir+'\\'+chipname+'\\Metrics')
		for Mfile in os.listdir(dir):
			if Mfile.startswith('Maps'):
				fullname=dir+'\\'+Mfile
				outputname=outdir+'\\'+chipname+'\\Metrics\\'+Mfile
				if not os.path.exists(outputname):
					copytree(fullname,outputname)
					sys.stdout.write(print_time()+'Copy dir: '+fullname+'\n')
			else:
				fullname=dir+'\\'+Mfile
				outputname=outdir+'\\'+chipname+'\\Metrics\\'+Mfile
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
	except IOError as e:
		sys.stdout.write('No such dir: '+dir)
		raise e

def copy_ResultStatHtml(dir,chipname,outdir):
	for lane in os.listdir(dir):
		if not os.path.exists(outdir+'\\'+chipname+'\\'+lane):
			os.makedirs(outdir+'\\'+chipname+'\\'+lane)
		for files in os.listdir(dir+'\\'+lane):
			if re.search('BarcodeStat|SequenceStat',files):
				fullname=dir+'\\'+lane+'\\'+files
				outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
				'''else:
					sys.stdout.write(outputname+'exists.\n')
					continue'''
			if re.search(r'allCycleHeatmap|bestFovReport|heatmapReport|summaryReport',files):
				fullname=dir+'\\'+lane+'\\'+files
				outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
				'''else:
					sys.stdout.write(outputname+'exists.\n')
					continue'''

def copy_BGI_logs(dir,date,chipname,outdir):
	alldays=get_days(date,10)
	if not os.path.exists(outdir+'\\'+chipname+'\\BGI_logs'):
		os.makedirs(outdir+'\\'+chipname+'\\BGI_logs')
	for logs in os.listdir(dir):
		if re.search(r'BGI.Zebra(.*)-(20\d+).',logs):
			logfiles=re.search(r'BGI.Zebra(.*)-(20\d+).',logs)
			outdate=logfiles.group(2)
			if outdate in alldays :	# keep 10 days logs before date
				fullname=dir+'\\'+logs
				outputname=outdir+'\\'+chipname+'\\BGI_logs\\'+logs
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')	
			else:
				#sys.stdout.write('file: '+logs+' unsupported\t'+outdate+'\n')
				continue

def copy_processor(dir,date,chipname,outdir):
	alldays=get_days(date,10)
	if not os.path.exists(outdir+'\\'+chipname+'\\processor'):
		os.makedirs(outdir+'\\'+chipname+'\\processor')
	for txt in os.listdir(dir):
		if re.search(r'processor_(20\d+)_(.*).',txt):	#processor_20190707_001625-HR.txt
			logfiles=re.search(r'processor_(20\d+)_(.*).',txt)
			outdate=logfiles.group(1)
			if outdate in alldays  :	# keep 10 days logs before date
				fullname=dir+'\\'+txt
				outputname=outdir+'\\'+chipname+'\\processor\\'+txt
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
		else:
			continue
			sys.stdout.write('No Such File or directory: '+txt+'\n')

def main():
	chipname=sys.argv[1].upper()
	dirD="D:\\Data\\"+chipname
	dirM="D:\\Data\\"+chipname+"\\Metrics"
	dirR="D:\\Result\\OutputFq\\"+chipname
	dirL="C:\\BGI\\Logs"
	dirZ='C:\\ZebraCallV2\\1.0.7.197'
	date=sys.argv[2]
	outdir=''
	cycles=collect_cycles(sys.argv[3])
	if len(sys.argv) ==5:
		outdir=sys.argv[4]
	elif len(sys.argv) ==4:
		outdir='D:\\CopyData'
	copy_DataThumbFOVFigs(dirD,chipname,cycles,outdir)
	copy_Metrics(dirM,chipname,outdir)
	copy_ResultStatHtml(dirR,chipname,outdir)
	copy_BGI_logs(dirL,date,chipname,outdir)
	copy_processor(dirZ,date,chipname,outdir)

if __name__ == '__main__':
	main()