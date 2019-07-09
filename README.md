# MGIseqerOutputCollect 
## Description 
The script is use to collect some important files such as `SummaryReport.html` for troubleshooting, contact our **FAS** colleagues with email.
Contact me by sending email to `caoshuhuan@yeah.net` when some bugs happen. 

## Prerequisites
- make sure python has been added to Windows PATH (ref https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path)
- One **bat** file and **python script** are provided, download this repository to D:\ and uncompress it. make sure the address is **D:\\** before use. 

## Tutorial 
#### -step1: edit `run.bat` file
- Open the `run.bat` file with notepad++ or other text editors. 
- Change the **flowcell name** and **sequencing ending date**. 
- if you want to collect the whole files to a new address expcept `D:\CopyData`(default directory), please provide the **destination directory**.  
#### -step2: store the `run.bat` file 
#### -step3: open `cmd` by input `win+R` 
#### -step4: drag the `run.bat` file to `cmd` and run it (recommended) 

## Python Script Usage
```
Usage:
	python MGIseqerOutputCollect.py <chip name> <date> [outdir]
Example:
	python D:\Scripts\MGIseqerOutputCollect.py V300018621 20190101 D:\CopyData
```