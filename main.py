import os
from imas_tools.story.story_csv import StoryCsv
from imas_tools.story.gakuen_parser import parse_messages


def gakuen_txt_to_sc_csv(gakuen_txt: str, txt_name_without_ext: str) -> str:
    parsed = parse_messages(gakuen_txt)
    sc_csv = StoryCsv.new_empty_csv(f"{txt_name_without_ext}.txt")
    for line in parsed:
        if line["__tag__"] == "message" or line["__tag__"] == "narration":
            if line.get("text"):
                sc_csv.append_line(
                    {
                        "id": "0000000000000",
                        "name": line.get("name", "__narration__"),
                        "text": line["text"],
                        "trans": "",
                    }
                )
        if line["__tag__"] == "title":
            if line.get("title"):
                sc_csv.append_line({"id": "0000000000000", "name": "__title__", "text": line["title"], "trans": ""})
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    sc_csv.append_line({"id": "select", "name": "", "text": choice["text"], "trans": ""})
            elif isinstance(line["choices"], dict):
                sc_csv.append_line({"id": "select", "name": "", "text": line["choices"]["text"], "trans": ""})
            else:
                raise ValueError(f"Unknown choice type: {line['choices']}")
    return str(sc_csv)


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
