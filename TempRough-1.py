import random

# Helper functions to generate random data types
def random_int():
    return random.randint(0, 100)

def random_float():
    return round(random.uniform(0.1, 100.0), 2)

def random_bool():
    return random.choice([True, False])

def random_str():
    return "'" + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) + "'"

def random_set():
    x= "{" + random_str() + ", " + random_str() + "}"
    x = eval(x)
    return x

def random_dict():
    return "{" + random_str() + ": " + random_str() + "}"

def random_tuple():
    return "(" + str(random_int()) + ", " + str(random_float()) + ")"

def random_list():
    return "[" + random_str() + ", " + str(random_bool()) + "]"

# Generating a list of 100 random inputs of different types
user_Inputs = []
for _ in range(12):
    user_Inputs.extend([
        random_int(), random_float(), random_bool(),
        random_str(), random_set(), random_dict(),
        random_tuple(), random_list()
    ])

# Limiting to 100 items only
user_Inputs = user_Inputs[:100]

# Formatting the final output to show in the correct format
formatted_inputs = ', '.join(map(str, user_Inputs))


print(formatted_inputs)
