def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    print (k)
    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]
    return(nums)


# print(rotate([1,2,3,4,5,6,7],3))
def feb(n) :
    if n == 0:
        return 0
    if n==1 :
        print(n)
        return 1
    
    else:
        return n + int(feb(n-1))
    

# feb(5)


def pow1(b,e)  :
    if e == 0:
        return 1
    elif e < 0:
        return 1/b * pow1(b, e+1)
    else:
        return b*pow1(b,e-1)

# print (pow1(2,-4))


def reverse(User1):
    if len(User1) == 0:
        return ''
    else:
        len1 = len(User1)
        sr = User1[-1]
        sr = sr + reverse(User1[0:len1-1])
    return sr

print(reverse('abcdefgh'))