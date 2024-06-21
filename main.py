import os
from imas_tools.story.gakuen_parser import parse_messages


def gakuen_txt_to_sc_csv(gakuen_txt: str, txt_name_without_ext: str) -> str:
    parsed = parse_messages(gakuen_txt)
    sc_csv = "id,name,text,trans\n"
    for line in parsed:
        if line["__tag__"] == "message" or line["__tag__"] == "narration":
            if line.get("text"):
                sc_csv += f"0000000000000,{line.get('name','__narration__')},{line['text']},\n"
        if line["__tag__"] == "title":
            if line.get("title"):
                sc_csv += f"0000000000000,__title__,{line['title']},\n"
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    sc_csv += f"select,,{choice['text']},\n"
            elif isinstance(line["choices"], dict):
                sc_csv += f"select,,{line['choices']['text']},\n"
            else:
                raise ValueError(f"Unknown choice type: {line['choices']}")
    sc_csv += f"info,{txt_name_without_ext}.txt,,\n"
    sc_csv += f"译者,,,\n"
    return sc_csv


if __name__ == "__main__":
    files = os.listdir("./raw")
    for file in files:
        
        if not file.endswith(".txt") or not file.startswith("adv_"):
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