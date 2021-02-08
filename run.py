import re

command = open("command.txt", 'r')
command_split = command.read().split('\n')
command.close()
for x in command_split:
    y = re.match(r'(.*?)="(.*)"', x)
    if y.group(1) == 'skin':
        skinpath = y.group(2)
    if y.group(1) == 'format':
        skinformat = y.group(2)
    if y.group(1) == 'target':
        skintarget = y.group(2)

target_list = ["Alex",
               "Annika",
               "Archeologist",
               "Baako",
               "Bediako",
               "Darian",
               "Elaine",
               "Eshe",
               "Esperanza",
               "Explorer",
               "Frosty",
               "Fuego",
               "Greta",
               "Hal",
               "Hedwig",
               "Hex",
               "Igor",
               "Jade",
               "Mayeso",
               "Morris",
               "Neo",
               "Nuru",
               "Pake",
               "Qamar",
               'Sam',
               "Sergey",
               "Shikoba",
               'Steve',
               'Sven',
               "Valorie",
               'Violet',
               'Wargen',
               'Winter_Warrior',
               'Zola']

if skintarget in target_list:
    from convert_skin import convert_mcd_skin_format
    convert_img = convert_mcd_skin_format(skinpath, skinformat)
    if convert_img:
        import os
        import uuid
        import shutil
        import json
        dirname = os.path.abspath('./' + str(uuid.uuid4()))
        shutil.copytree(os.path.abspath('./files/'), dirname)
        skinfile = dirname + f'/T_{skintarget}_Skin.png'
        shutil.copyfile(convert_img, skinfile)
        import_json = {
    "ImportGroups": [
        {
            "GroupName": "World",
            "Filenames": [
                skinfile
            ],
            "DestinationPath": f"/Game/Actors/Characters/Player/Master/Skins/{skintarget}/",
            "FactoryName": "TextureFactory",
            "bReplaceExisting": 1,
            "bSkipReadOnly": 0,
            "bShouldAttemptToSave": 1,
            "ImportSettings": {
                "Format": "B8G8R8A8",
                "CompressionSettings": "TC_BC7",
                "Filter": "TF_Nearest"
            }
        }
    ]
}
        jsonfile = open(dirname + '/import.json', 'w')
        jsonfile.write(json.dumps(import_json))
        jsonfile.close()
        os.chdir(dirname)
        a = os.system(dirname + '/add_assets.bat')
        b = os.system(dirname + '/cook_assets.bat')
        os.chdir(dirname + '/Tools/')
        c = os.system(dirname + '/Tools/pack_compressed.bat')
        os.chdir("../../")
        shutil.copy(dirname + '/Tools/compressed_pack.pak', f"./")
        shutil.rmtree(dirname)
        os.remove(convert_img)
    else:
        print('The skin size is incorrect, should be 64*64.')
print('The skin target name is incorrect, it can be found in run.py.')
