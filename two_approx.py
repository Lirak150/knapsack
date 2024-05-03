def solve(weights: tuple[int], profits: tuple[int], capacity: int) -> tuple[int, int, list[int], int]:
    items_sorted_by_values = sorted([(profit, weight) for profit, weight in zip(profits, weights)],
                                    key=lambda item: item[0] / item[1], reverse=True)

    # max greed
    knapsack_max_greed_profit = 0
    knapsack_max_greed_weight = 0
    items_max_greed = [0] * len(items_sorted_by_values)
    for ind, (profit, weight) in enumerate(items_sorted_by_values):
        if weight <= capacity:
            knapsack_max_greed_profit = profit
            knapsack_max_greed_weight = weight
            items_max_greed[ind] = 1
            break

    # greedy
    available_weight = capacity
    knapsack_greedy_profit = 0
    knapsack_greedy_weight = 0
    items_greedy = [0] * len(items_sorted_by_values)
    for ind, (profit, weight) in enumerate(items_sorted_by_values):

        if weight <= available_weight:
            knapsack_greedy_profit += profit
            knapsack_greedy_weight += weight
            available_weight -= weight
            items_greedy[ind] = 1

        if available_weight == 0:
            break

    if knapsack_max_greed_profit > knapsack_greedy_profit:
        return knapsack_max_greed_profit, knapsack_max_greed_weight, items_max_greed, 2
    else:
        return knapsack_greedy_profit, knapsack_greedy_weight, items_greedy, 2
