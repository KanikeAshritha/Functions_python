#easy1
def calculate_average(nums):
    avg=0
    if len(nums)==0:
        return 0
    else:
        avg=sum(nums)/len(nums)
        return avg
print(calculate_average([5, 10, 15, 20]))  
print(calculate_average([]))




#easy2
def greet_user(name,*args):
    if(args):
        for a in args:
            return f"{a}, {name}!"
    else:
        return f"Hello, {name}!"

print(greet_user("Alice")) 
print(greet_user("Bob", "Hi"))  




#medium1
def calculate_total(*args,discount=0):
    total_cost=0
    for a in args:
        total_cost += a
    if(discount!=0):
        total_cost -= (total_cost*discount)/100
    return int(total_cost)

print(calculate_total(10, 20, 30)) 
print(calculate_total(10, 20, 30, discount=10)) 




#medium2
def create_multiplier(n):
    def func(x):
        return x*n
    return func
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  
print(triple(5))



#hard1
def power(x,n):
    if n == 0:
        return 1
    if n < 0 :
        x = 1 / x
        n = -n
    if n%2 == 0:
        pow1 = power(x , n // 2)
        return pow1*pow1
    else:
        return x* x**(n-1)
print(power(2, 10)) 
print(power(3, 4))





#hard2
def compose(*args):
    def composed(x):
        for func in reversed(args):
            x= func(x)
        return x
    return composed

def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x ** 2

f = compose(square, double, add_one)
print(f(3)) 