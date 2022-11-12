import glob

# open all json files in folder
files = glob.glob("images/*.json")
print(files)
for file in files:
    with open(file) as f:
        data = f.read()
        result = "CanvasCycle.processImage(" + data + ");"
        name = file.replace(".json", ".js")
        with open(name, "w") as f:
            f.write(result)

        
