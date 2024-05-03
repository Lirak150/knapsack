import itertools


def gs(all_items: dict[int, tuple[int, int]], current_knapsack: tuple[int], current_knapsack_capacity: int,
       all_capacity: int) -> tuple[int, int, set[int]]:
    new_profit = 0
    new_weight = 0
    new_items = set()
    available_capacity = all_capacity - current_knapsack_capacity
    for item in (set(all_items.keys()) - set(current_knapsack)):
        item_profit, item_weight = all_items[item]
        if item_weight <= available_capacity:
            available_capacity -= item_weight
            new_profit += item_profit
            new_weight += item_weight
            new_items.add(item)
        if available_capacity == 0:
            break
    return new_profit, new_weight, new_items


def solve(weights: tuple[int], profits: tuple[int], capacity: int, *, k: int) -> tuple[int, int, list[int], int]:
    result_profit = 0
    result_weight = 0
    num_of_intermediate_solutions = 0
    ans_items = [0] * len(weights)
    all_items = {ind: (profit, weight) for ind, (profit, weight) in enumerate(zip(profits, weights))}
    all_items_keys = list(all_items.keys())
    for current_cardinality in range(1, k + 1):
        for current_items in itertools.combinations(all_items_keys, current_cardinality):
            current_profit = sum((all_items[item][0]) for item in current_items)
            current_weight = sum((all_items[item][1]) for item in current_items)
            num_of_intermediate_solutions += 1
            if current_weight > capacity:
                continue
            new_profit, new_weight, new_items = gs(all_items, current_items, current_weight, capacity)
            if new_profit + current_profit > result_profit:
                result_profit = new_profit + current_profit
                result_weight = new_weight + current_weight
                ans_items = [0] * len(weights)
                for item in current_items:
                    ans_items[item] = 1
                for item in new_items:
                    ans_items[item] = 1
    return result_profit, result_weight, ans_items, num_of_intermediate_solutions
