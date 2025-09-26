import os, glob


def main():
    contextfile = "xx.osb"

    tagsline = ""

    with open(contextfile, "r") as f:
        for line in f:
            if line[0] == "T" and line[1] == "a" and line[2] == "g":
                tagsline = line
                break

    # print(tagsline)

    for filename in glob.glob("*.osu"):
        lines = []
        line_to_insert = -1
        deleteFirst = False

        with open(os.path.join(os.getcwd(), filename), "r") as f:
            lines = f.readlines()

            for index in range(len(lines)):
                if len(lines[index]) < 4:
                    continue
                if (
                    lines[index][0] == "T"
                    and lines[index][1] == "a"
                    and lines[index][2] == "g"
                ):
                    deleteFirst = True
                    line_to_insert = index
                    break

            if line_to_insert == -1:
                for index in range(len(lines)):
                    if len(lines[index]) < 4:
                        continue
                    if (
                        lines[index][0] == "V"
                        and lines[index][1] == "e"
                        and lines[index][2] == "r"
                    ):
                        line_to_insert = index + 1
                        break

        if deleteFirst:
            lines.pop(line_to_insert)

        lines.insert(line_to_insert, tagsline)

        with open(os.path.join(os.getcwd(), filename), "w") as f:
            lines = "".join(lines)
            f.write(lines)


if __name__ == "__main__":
    main()
