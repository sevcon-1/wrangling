import pyperclip as pc
import re

tl_parts = re.compile(r'^\[(.*)\](.*)')

t = pc.paste()

text_list = t.split("\n")

time_dict = {}

''' Create a list of key value pairs '''
for s in text_list:
    m = re.match(tl_parts, s)
    time_dict[m.group(1)] = m.group(2)
    
with open('timeline.csv', 'w') as f:
    for k,v in time_dict.items():
        f.write(f"{k},{v}\n")

#print(text_list[5])