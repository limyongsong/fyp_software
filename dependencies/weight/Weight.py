import re

def main(str_val):

    textlist = re.split('=',str_val)
    textlist = list(filter(None, textlist))
    textlist = list(map(float, textlist))
    text = max(textlist)
    text = str(text)
    return text
