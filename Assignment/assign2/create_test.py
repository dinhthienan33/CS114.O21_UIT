import random
in_range='500 500 \n'
matrix = [[random.randint(-10000,10000) for _ in range(500)] for _ in range(500)]
with open('test_cases.txt', 'w') as f:
    f.write(str(in_range))  # Write the value of in_range followed by a newline character
    for row in matrix:
        f.write(' '.join(str(num) for num in row) + '\n')  # Write each element in the row separated by spaces, followed by a newline 
    f.close()