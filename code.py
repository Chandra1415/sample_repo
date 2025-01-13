num = int(input('Enter the number : ' ))
i = 1
while i<=num:
    print(i)
    i=i+1 # type: ignore

def real_fun(): 
    def inner_fun(s): 
        return s+" how are you?" 
    return inner_fun
@real_fun
def fun(s):
    return s
s="hii bro!"
res = fun(s)
print(res)