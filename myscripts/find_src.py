import yaml
import os
for subdir, dirs, files in os.walk('kinetic/'):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".yaml"):  
            if 'source' in file:
                print(file)