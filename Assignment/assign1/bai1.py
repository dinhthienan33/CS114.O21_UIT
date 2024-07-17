def count_black_cells(grid, rows, cols):
    count = 0
    for i in rows:
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                count += 1
    return count


def count_ways(grid, rows, cols, target):
    if count_black_cells(grid, rows, cols) != target:
        return 0

    if len(rows) == len(grid) or len(cols) == len(grid[0]):
        return 1

    total_count = 0

    for i in range(len(grid)):
        if i not in rows:
            total_count += count_ways(grid, rows + [i], cols, target)

    for j in range(len(grid[0])):
        if j not in cols:
            total_count += count_ways(grid, rows, cols + [j], target)

    return total_count


def main():
    # Nhập số hàng, số cột và số tuổi của Bình
    h, w, k = map(int, input().split())

    # Nhập lưới ô màu
    grid = []
    for _ in range(h):
        row = input()
        grid.append(row)

    target = k  # Số tuổi của Bình

    # Gọi hàm count_ways để đếm số cách chọn hàng và cột thỏa mãn yêu cầu
    num_ways = count_ways(grid, [], [], target)

    # In ra số cách lựa chọn thỏa mãn yêu cầu
    print(num_ways)


if __name__ == "__main__":
    main()