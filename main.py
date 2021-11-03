import os
import os.path
import re

directory = os.listdir()
for file in directory:
  if file.endswith('.testcafe.ts'):
    with open(file, 'r') as openedFile:
      print('### FIXTURE: ', file)
      data = openedFile.readlines()
      joined = ''.join(data)
      searchPattern = r"((\`).*?(\`))"
      output = re.findall(searchPattern, joined, re.DOTALL)
      for item in output:
        str = ''.join(item)
        print(str)