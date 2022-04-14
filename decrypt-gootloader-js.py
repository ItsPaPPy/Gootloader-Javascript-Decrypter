# %%
import re
import math
import sys
# %%


def alternating_unzip(zipped):
    ## Imagine a reverse card shuffle. It takes every other char
    ## and adds it to the beginning. Then takes the others and 
    ## adds them to the end.
    unzipped = ""
    for index in range(len(zipped)):
        if index & 1:
            unzipped += zipped[index]
        else: 
            unzipped = zipped[index] + unzipped
    return unzipped

def find_url(mal_doc):
    matches = re.search('href=\"(https?:\/\/[^\"]*)', mal_doc)
    if matches:
        return matches.group(1)
    return "No Matches Found"

# %%
with open(sys.argv[1],"r", encoding='latin1') as f:
    obfuscated_js = f.readlines()

# %%
def method_one(obfuscated_js):
    internal_payload = obfuscated_js[0][obfuscated_js[0].index("= '")+3:obfuscated_js[0].index("';")]
    unzipped_payload = alternating_unzip(internal_payload)
    if "pots|" in unzipped_payload:
        print("Reversed String")
        unzipped_payload=unzipped_payload[::-1]
    else: 
        pass
    html_body = unzipped_payload.split("|")[0]
    #next they encode things using "" and +
    html_array = re.split("''|\+",html_body)

    ## next every other index is reversed
    for x in range(len(html_array)):
        if x % 2:
            html_array[x]=html_array[x][::-1]


    ## last they reverse every other index
    html_array_length = len(html_array)
    for x in range(math.floor(html_array_length/2)):
        if x % 2:
            temp_holder = html_array[x]
            html_array[x] = html_array[html_array_length-x-1]
            html_array[html_array_length-x-1] = temp_holder
    return "".join(html_array)

url = find_url(method_one(obfuscated_js))
print(url)
# %%
# %%
