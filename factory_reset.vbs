x=msgbox ("Are you sure you want to reset DOS to factory settings?", 4+32,"Reset?")
dim Folder
Folder = "\\sys_files"
if x=6 then
   Set f_sys = CreateObject("Scripting.FileSystemObject")
   'f_sys.DeleteFile( ;var_Folder
   y=msgbox ("DOS successfully reset to factory settings!", 64,"Done!")
elseif x=7 then
   z=msgbox("Operation aborted!", 64,"Abort")
end if
