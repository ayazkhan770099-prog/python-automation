import os
for root,dirs,filse in os.walk("."):
    for file in filse:
        if file.endswith(".txt"):
            src=os.path.join(root,file)
            sht.copy(src,"text")
