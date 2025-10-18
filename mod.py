# import mod
# mybar = mod.Bar()


User1 =  ["hi", "bye", "hello", "leetcode", "start", "end"]
User2 = ["hi", "stop", "leetcode", "start", "end", "bye"]
def find(u1, u2):
    commonstr =   [(str1) for str2 in u2 for str1 in u1 if str1== str2]
    print(max(commonstr, key= len))

find(User1, User2)



vec = [[1,2,3], [4,5,6], [7,8,9]]
a = [num1 for elem2 in vec  for num1 in elem2]
print (a)


print(''.join(str(vec)))
 

def reverse(User1):
    if len(User1) == 0:
        return ''
    else:
        len1 = len(User1)
        sr = User1[-1]
        sr = sr + reverse(User1[0:len1-1])
    return sr

print(reverse(User1))


def feb(n):
    if n==0 :
        return
    if n==1:
        return n
    else:
        return n + feb(n-1)
    
print (feb(2))

def power(b, n):
    if abs(n) == 0:
        return 1
    elif (n<0):
        return (1/b)* power(b,-(abs(n)-1))
    else:
        return b*power(b,n-1)
   



print(power(2,-3))

def strtoint(str1):
    revstr = reverse(str1)
    print(revstr)
    ind = 0
    val = 0
    while(revstr[ind] != ' '):
        val = val + int(revstr[ind])*pow(10,ind)
        ++ind

    return val


print(str(strtoint('1546')) )
