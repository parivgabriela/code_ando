"""
Task

You are given a text of

lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or

Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer,
.
The next

lines each contain a line of the text.

Constraints

Neither && nor || occur in the start or end of each line.

Output Format

Output the modified text.

Sample Input

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    

"""
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

