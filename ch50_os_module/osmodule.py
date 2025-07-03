import os

try :
    # change dir
    os.chdir('/Users/rahulkandula/Desktop')
    print(os.getcwd())
except FileNotFoundError:
    print('** WRONG PATH PROVIDED **')
else:
    # get all files in a dir
    print(os.listdir())

    #create a new folder
    # os.mkdir('sometest')
    os.makedirs('rahultest/innerfolder')

    # delete dirs
    # os.rmdir('sometest')
    os.removedirs('rahultest/innerfolder')


    #rename files
    # os.rename('actualname', 'newname')

    # get last mod times of a file
    file_stat = os.stat('test.txt')
    print(file_stat)
    print(file_stat.st_mtime)


    # environs
    print(os.environ.get('HOME'))


    # os.path
    new_file_path = os.path.join(os.environ.get('HOME'), 'test2.txt')
    print(os.path.dirname(new_file_path))
    print(os.path.basename(new_file_path))
    print(os.path.split(new_file_path))
    print(os.path.splitext(new_file_path))
    print(os.path.exists(new_file_path))

    print(os.path.isdir(new_file_path))
    print(os.path.isfile(new_file_path))


finally:
    print('All done!')