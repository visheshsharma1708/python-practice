size = 5  # Size of the + pattern (odd number)

for i in range(size):
    for j in range(size):
        if i == size // 2 or j == size // 2:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()
