import os

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

file1 = input("Enter file names: ")
directory1 = input("Enter dirctory name: ")

print(find_files(file1,directory1))
