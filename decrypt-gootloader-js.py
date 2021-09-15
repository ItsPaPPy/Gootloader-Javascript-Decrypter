# %%
import re
import sys

with open(sys.argv[1],"r", encoding='utf-16-le') as f:
    lines = f.readlines()
 
obfuscated = lines[0][lines[0].index("= '")+3:lines[0].index("';")]
stringBuilder = ""

for index in range(len(obfuscated)):
    if index & 1:
        stringBuilder += obfuscated[index]
    else: 
        stringBuilder = obfuscated[index] + stringBuilder

pipe_split = stringBuilder.split("|");
pipe_split = list(map(lambda x: x[::-1],pipe_split))

if len(pipe_split[0]) < 200:
    pipe_split.reverse()
# %%


def find_url():
    for mal_doc in pipe_split:
#   if "Â" in pipe_split[index]:
#       first_split = pipe_split[index].split("Â")
#       second_split = first_split[1].split("©")
#       mal_doc = first_split[index]+second_split[0][::-1]+second_split[1]
#   else:
#       mal_doc = pipe_split[index][::-1]
        matches = re.search('href=\"(https?:\/\/[^\"]*)', mal_doc)
        reverse_matches = re.search('([^\"]*\/\/:s?ptth)\"=ferh', mal_doc)
        if matches or reverse_matches:
            if matches:
                url = matches.group(1)
            else:
                url = reverse_matches.group(1)[::-1]
            return url

    return "No Matches Found"

print(find_url())

# %%