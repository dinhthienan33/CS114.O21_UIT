def count_coloring_options(H, W, K, paper):
    # Initialize a list to store all possible bitmasks
    masks = []
    for i in range(2**W):
        masks.append(bin(i)[2:].zfill(W))

    # Initialize the count of valid options
    valid_options = 0

    # Iterate through all bitmasks
    for mask in masks:
        black_count = 0
        for i in range(H):
            for j in range(W):
                if mask[j] == '1' or paper[i][j] == '#':
                    black_count += 1
        if black_count == K:
            valid_options += 1

    return valid_options
def main():

    # Read input
    H, W, K = map(int, input().split())
    paper = [input() for _ in range(H)]

    # Calculate and print the result
    print(count_coloring_options(H, W, K, paper))
    print(paper)
if __name__ == '__main__':
    main()