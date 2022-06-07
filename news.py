with open('news.txt') as f: # Reads the txt file.
    lines = f.readlines()

for item in lines: # Analyzes every line of text.
    if item[0].isdigit() and item[len(item) - 2] == ".": # Analyzes the first and last character of every line.
        print(item)
