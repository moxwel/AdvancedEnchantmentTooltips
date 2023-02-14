import os
import json
print("Advance")



# Setup paths
langs_path = "./langs/"
icons_path = "./icons.json"
out_path = "./out/"



# Read icons file
print("Reading icons...")
icons_file = open(icons_path, "r", encoding="UTF8")
icons_data = json.load(icons_file)
icons_keys = list(icons_data.keys())
icons_file.close()
print("Readed "+str(len(icons_keys))+" icons...")



# Read langs directory
print("Reading langs...")
langs_dir = os.listdir(langs_path)
print("Readed "+str(len(langs_dir))+" files.")



# Build process
if not os.path.exists(out_path):
    print("Out folder not found. Creating one...")
    os.mkdir(out_path)

for file in langs_dir:
    print("Building "+file+" ...")
    lang_file = open(langs_path+file, "r", encoding="UTF8")
    lang_data = json.load(lang_file)

    new_data = dict()
    
    for lang_key in icons_keys:
        try:
            new_data[lang_key]= str(icons_data[lang_key]+lang_data[lang_key])
        except KeyError:
            print("    Key '"+lang_key+"' not found in '"+file+"'. Skipping...")

    out_file = open(out_path+file, "w", encoding="UTF8")
    json.dump(new_data, out_file, indent=4)
    out_file.close()

    lang_file.close()

print("Done.")
