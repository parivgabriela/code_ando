
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern_and_symbol = '\ && '
pattern_or_symbol = '\ \|\|\ '
n_lines = int(input())
if n_lines > 100 or n_lines < 0: n_lines = 0
list_text = []

for i in range(n_lines):
    line = input()
    list_text.append(line)

text = '\n'.join(list_text)

pattern_and = re.compile(pattern_and_symbol)
pattern_or = re.compile(pattern_or_symbol)

match_and = pattern_and.search(text)
match_or = pattern_or.search(text)
while match_and or match_or:
    text = re.sub(r'\ && ', ' and ', text)
    text = re.sub(r'\ \|\|\ ', ' or ', text)
    match_and = pattern_and.search(text)
    match_or = pattern_or.search(text)

print(text)

