import shutil

# Copying a file
'''shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.'''
shutil.copy("src.txt", "dst.txt")

# Copying a directory
'''shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.'''
shutil.copytree("src_dir", "dst_dir")

# Moving a file
'''shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.'''
shutil.move("src.txt", "dst.txt")

# Deleting a directory
'''shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.'''
shutil.rmtree("dir")