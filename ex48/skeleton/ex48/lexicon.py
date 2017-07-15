directions = ('north', 'south', 'east', 'west', 'down','up', 'left', 'right',
             'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    result = []
    words = stuff.split()
    for i in words:
        if i in directions:
            result.append(('direction', i))
        elif i in verbs:
            result.append(('verb', i))
        elif i in stops:
            result.append(('stop', i))
        elif i in nouns:
            result.append(('noun', i))
        elif convert_number(i):
            result.append(('number', convert_number(i)))
        else:
            result.append(('error', i))

    return result