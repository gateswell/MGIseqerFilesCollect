# MGIseqerOutputCollect 
## Description 
The script is use to collect some important files such as `SummaryReport.html` for troubleshooting, contact with our **FAS** colleagues with email.
Contact with me by send email to `caoshuhuan@yeah.net` when some bugs happen. 

## Prerequisites
- make sure python has been added to PATH (ref https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path)
- One bat file and python script are provided, download this repository to D:\ and uncompress it. make sure the address is **D:\** before use. 

## Tutorial 
#### -step1: edit `run.bat` file
- Open the `.bat` file with notepad++ or other text editors. 
- Change the **chip name** and **date**. 
- if you want collect the whole files to a new address expcept `D:\CopyData`, please provide the **destination directory**. 
#### -step2: store the `run.bat` file 
#### -step3: double dial `run.bat` file to run it or run it by `cmd`(recommand) 

## Python Script Usage
```
Usage:
	python MGIseqerOutputCollect.py <chip name> <date> [outdir]
Example:
	python D:\Scripts\MGIseqerOutputCollect.py V300018621 20190101 D:\tmp
```