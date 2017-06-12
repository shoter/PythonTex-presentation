def importPeople():
    with open("table.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    result = []
    for line in content:
        split = line.split("\t")
        result.append(split)

    return result
