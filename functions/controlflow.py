# 1.Range.Used to generate a sequence of numbers that we can use in iteration.

def even_numbers():
    x = range(10)
    for i in x:
        if i%2==0:
            print(i)
    
 

        
# 2.If statement.Checks whether expression is true or false.Its used mostly in combination with comparison operators.
 
def odd_numbers():
    y=range(10)
    for i in y:
      if i%2 != 0:
            print(i)
           

# 3.Else statement.The if statement can optimally be combined with an else statement.The code inside else will be executed if the preceding if statement returns false

def divisible_by_five():
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
             print(f"{i} is not divisible by 5")


       

# Elif- Combining if statement with logical operators. And,Not or

def odd_or_even():
    x = range(50)
    for i in x:
        if i%2==0 and i%3 ==0:
            print(f"{i} is divisible by both 2 and 3")
        elif i%2==0 or i%3 ==0:
            print(f"{i} is divisible by 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3")


# While loop .It continues running as long as the set condition remains true.

def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1

# 6.Break statement exists the while loop even if the condition set is true.Its like a return .It doesn’t consider whether the condition is true or false.

def break_statement():
    y=1
    while y<10:
        print("Hello")
        y+=1
        if y==5:
            break

# 6.Continue statement.It skips the remainder of the current iteration and goes to the next iteration.It doesn’t terminate the iteration.
def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x)


