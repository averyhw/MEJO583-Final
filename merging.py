import glob
import json

glob_data = []
for file in glob.glob('../final/*-summary.json'):
    with open(file) as json_file:
        data = json.load(json_file)

        i = 0
        while i < len(data):
            glob_data.append(data)
            i += 1

with open('finalFile.json', 'w') as f:
    json.dump(glob_data, f, indent=4)



# https://stackoverflow.com/questions/23520542/issue-with-merging-multiple-json-files-in-python
