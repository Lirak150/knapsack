def solve(weights: tuple[int], profits: tuple[int], capacity: int) -> tuple[int, int, list[int], int]:
    matrix = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    for i in range(len(weights) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif weights[i - 1] <= j:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weights[i - 1]] + profits[i - 1])
            else:
                matrix[i][j] = matrix[i - 1][j]
    ans = matrix[len(weights)][capacity]
    ans_items = [0] * len(profits)
    backward_path = len(weights)
    backward_capacity = capacity
    while backward_path != 0:
        if not matrix[backward_path][backward_capacity] == matrix[backward_path - 1][backward_capacity]:
            ans_items[backward_path - 1] = 1
            backward_capacity -= weights[backward_path - 1]
        backward_path -= 1
    return ans, sum((weight * item) for weight, item in zip(weights, ans_items)), ans_items, (len(weights) + 1) * (
                capacity + 1)
