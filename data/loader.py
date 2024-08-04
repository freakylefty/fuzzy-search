# Basic utility to convert the the sample data I used into the format I import
# (https://docs.python.org/3/tutorial/index.html)
# Raw data is in data.txt (after stripping out the section numbers and replacing some unicode characters)
# Processed data for testing is in sections.txt

with open('data.txt') as file:
    lines = file.readlines()
output = []
headings = ['', '', '', '']
for line in lines:
    currLine = line.replace('\n', '')
    tabCount = currLine.count('\t')
    headings[tabCount] = currLine.replace('\t', '')
    index = 0
    currTitle = ''
    while index <= tabCount:
        if (index > 0):
            currTitle += ' / '
        currTitle += headings[index]
        index += 1
    output.append(currTitle)

with open('sections.txt', 'w') as outfile:
    outfile.write('\n'.join(line for line in output))