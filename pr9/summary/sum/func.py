import re


def summary(s):
    return re.sub(r'(\d+)%', lambda m: str(int(m.group(1)) / 100), s)
    # 'string 1,2,1.0,0.5'