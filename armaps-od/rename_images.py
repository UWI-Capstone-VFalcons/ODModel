import os

root_directory = "raw-images"

# Get list of directories in  
directories = [x[0] for x in os.walk(root_directory)] 

for directory in directories[1:]:
    print(directory.replace(root_directory+"/" , ""))
    d_files = os.listdir(directory)
    for num in range(len(d_files)):
        os.rename(directory+"/"+d_files[num],directory+"/"+directory.replace(root_directory+"/" , "")+"_"+str(num+1)+".jpg") 
