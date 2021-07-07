import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:    # here we are creating a directory and 
    if not os.path.isdir(dir_):
        os.makedirs(dir_)   # placing a empty directory
        with open(os.path.join(dir_,".gitkeep"),"w") as f:
            pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass