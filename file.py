import os
for root,dirs,filse in os.walk("."):
    for file in filse:
        if file.endswith(".txt"):
            src=os.path.join(root,file)
            sht.copy(src,"text")

# This script scans the current working directory and all of its
   # subdirectories for text files (.txt). Every matching file is
    #copied to the "text" directory, allowing text documents to be
    #gathered into a single location for backup, analysis, or review.
