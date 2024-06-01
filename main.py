import os
from imas_tools.story.adapter import gakuen_txt_to_sc_csv

if __name__ == "__main__":
    files = os.listdir("./raw")
    for file in files:
        
        if not file.endswith(".txt"):
            continue
        with open("./raw/" + file, "r", encoding="utf-8") as f:
            dest = f'./tmp/{file.replace(".txt", ".csv")}'
            with open(dest, "w", encoding="utf-8") as f2:
                txts = f.read()
                try:
                    f2.write(gakuen_txt_to_sc_csv(txts, file.replace(".txt", "")))
                    print("Successfully converted " + file + " to " + dest)
                except Exception as e:
                    # print(txts)
                    print(file)
                    raise e
                    # pass