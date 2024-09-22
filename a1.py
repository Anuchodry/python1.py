print("hello world")
a = 15
b = 12
print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")
# Addition
add = a + b
print(f"(a + b):{a+b}")
#subtraction
sub = a - b
print(f"(a - b): {a-b}")
# Multiplication
mul = a * b
print(f" (a * b): {a*b}")
# Division
div = a / b
print(f"(a / b): {a/b}")

c = a/b
print(f"Value of c (integer division): {c}")
print(f"Type of c: {type(c)}")

# Convert c to float
c_float = float(c)
print(f"Value of c as float: {c_float}")
print(f"Type of c as float: {type(c_float)}")

# String message
message = "The result of a divided by b is:"
# Concatenate message with the value of c converted to string
message_with_result = f"{message} {c}"
print(message_with_result)
# Compare if a is greater than b
is_a_greater = a > b
print(f"a > b: {is_a_greater}")
# Check if a is equal to b
is_a_equal_b = a == b
print(f"a == b: {is_a_equal_b}")