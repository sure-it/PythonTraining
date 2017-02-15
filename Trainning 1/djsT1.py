import pprint
import collections

with open('randlist.txt','r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)

    print(value)
