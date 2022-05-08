:: don't worry it's not a virus
@echo off
::mode 800
::color f0 ;light mode
cd sys_files
python kernel_start.py %*
cmd /k
