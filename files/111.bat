SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"


SET /p editorPath= < Tools\user_settings\editor_directory.txt

"%editorPath%\UE4Editor-Cmd.exe" "%ddp%\UE4Project\Dungeons.uproject" -run=ImportAssets -importsettings="C:\Users\25963\Desktop\Dungeons-Mod-Kit-master\111.json" -ImportAndSave