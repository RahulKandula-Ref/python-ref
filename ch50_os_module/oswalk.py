import os

for dirpath, dirs, files in os.walk('/Users/rahulkandula/Desktop/nand2tetris'):
    print('Directory : ', dirpath)
    print('Dirs      : ', dirs)
    print('Files     : ', files)

    # walk is useful for searching or just iterating through all the files!