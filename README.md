# MGIseqerFilesCollect 
## Description 
The script is use to collect some important files such as `SummaryReport.html` for troubleshooting, contact our **FAS** colleagues with email.
Contact me by sending email to **caoshuhuan@yeah.net** when some bugs happen. 

## Version history 
The current version is V1.0.1  
You can also download the historic versions at [releases](https://github.com/gateswell/MGIseqerFilesCollect/releases "Lastest Version: v1.0.1")  

## Prerequisites
- make sure python has been added to Windows PATH (ref https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path)
- One **bat** file and **python script** are provided, download this repository to D:\ and uncompress it. make sure the uncompress address is **D:\\** before use!  

## Tutorial 
#### -step1: edit `run.bat` file
- Open the `run.bat` file with notepad++ or other text editors. 
- Change the **flowcell name** and **sequencing ending date**. 
- if you want to collect the whole files to a new address expcept `D:\CopyData`(default directory), please provide the **destination directory**.  
#### -step2: store the `run.bat` file 
#### -step3: Press `Win+R` firstly, then type in `cmd` and press `Enter`. 
#### -step4: drag the `run.bat` file to `cmd` and run it (recommended) 

## Python Script Usage
```
Usage:
	python MGIseqerOutputCollect.py <flowcell name> <ending date> <cycle:S001-S010,S101,S120|None> [outdir]
Example:
	python D:\MGIseqerFilesCollect-master\MGIseqerOutputCollect.py V300018621 20190101 S001 D:\CopyData
```