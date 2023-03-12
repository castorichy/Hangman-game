
def read_file(line_no: int):
    """ Reads the file and return a word in a given line """
    data = []
    with open("words.txt", "r") as f:
        data = f.read().split("\n")
    return data[line_no]
