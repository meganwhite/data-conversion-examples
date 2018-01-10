with open('name.txt') as f:
    my_name = f.read()

    hello_my_name = "Hello, my name is " + my_name

with open('hello.txt', 'w') as f:
    f.write(hello_my_name)

print hello_my_name