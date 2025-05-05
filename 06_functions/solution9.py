
# Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit

'''
A generator function in Python allows you to generate a sequence of values one at a time, instead of returning them all at once like a list.
It uses the yield keyword instead of return.

📌 yield vs return:
return exits the function completely.

yield pauses the function, saving its state, and resumes from there the next time it's called.
'''
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)
