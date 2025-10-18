import sys

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    e = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        print('key error')
    except ValueError as e:
        print('value error')
    print(e)

#bad()

def good():
    exception = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        exception = e
        print('key error')
    except ValueError as e:
        exception = e
        print('value error')
    print(exception)

#good()

def strtoint(s) :
    l = []
    for e in s:
        l.append(e)
    return l
#print(strtoint('1546'))  

#
#printnletter("Print  Letter Every Word String",4)
def pl(s,n) :
    print( [w[n] for w in s.split(' ') if len(w) > n ])
            #if(len(w) > n) for l in  w])

pl("Print nth Letter of Every Word in String",3)  