def q1(source,target):
    count = 0
    i = 0
    while i < len(target):
        flag = True
        for j in range(len(source)):
            if target[i] == source[j]:
                flag = False
                i += 1
        if(flag):
            return -1
        count += 1
    return count

print(q1('abc','abcbc'))
print(q1('abc','acdbc'))
print(q1('xyz','xzyxz'))

def q2(input):
    k = len(input)
    li = []
    stack = []
    for i in range(2*k):
        li.append(' ')
    for i in range(k):
        c = input[i]
        if c != '(' and c != ')':
            continue
        else:
            if c == '(':
                li[i+k] = 'x'
                stack.append(i+k)
            else: # cases for )
                if len(stack) == 0:
                    li[i+k] = '?'
                else:
                    index = int(stack.pop())
                    li[index] = ' '
    ans = input + '\n'
    for i in range(k):
        ans = ans+li[i+k]
    return ans

print(q2('bge)))))))))'))
print(q2('((IIII))))))'))
print(q2('()()()()(uuu'))
print(q2('))))UUUU((()'))

'''
定义一个多重集合 S 的权值 val(S)为 Mean(S)-Median(S)。给定一个长度为 n 的非负整数序列a[0],a[1],..,a[n- 1]，对于所有 2^n 个子序列, 求出最大权值的子序列的权值。
要求时间复杂度为O(n^2) 及以下。Sample input: n=4 a =[1,3,5,9]; Sample output: 1.333...。
'''
#我的思路：
#对于一个已知的array (4个参数:1. length 2. Median 3. Mean 4. Median左右的数),当一个新的数 x 被加入时，这个数会导致权值 (1) 上升  或 (2) 下降
#找出对应权值上升的情况时，这个新的数需要满足的条件：
#对于权值上升的情况的x的值域，在数学上，这个条件应该是个一个或多个包含4个参数中的n(>0)个所组成的多项式 

# for i in range(len(li)): # N
#     arr  = [li[i]]
#     for j in range(i+1,len(li)): # N
#         if (li[j] in 对应的权值上升值域): 
#             maxVal = max(maxVal,新权值)
#             arr.append(li[j])
# return maxVal # O(N^2)
