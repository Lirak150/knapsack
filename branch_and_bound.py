from queue import PriorityQueue


class Item:
    def __init__(self, idx, weight, profit):
        self.idx = idx
        self.weight = weight
        self.profit = profit


class Node:
    def __init__(self, level, parent, item, cum_profit, cum_weight):
        self.level = level
        self.parent = parent
        self.item = item
        self.cum_profit = cum_profit
        self.cum_weight = cum_weight

    def __lt__(self, other):
        return other.cum_weight - self.cum_weight


def upper_bound(node: Node, capacity: int, items: list[Item]):
    if node.cum_weight >= capacity:
        return 0

    cum_profit_bound = node.cum_profit
    cum_weight = node.cum_weight
    next_level = node.level

    while cum_weight + items[next_level].weight <= capacity:
        next_level += 1
        if next_level == len(items):
            break
        cum_weight += items[next_level].weight
        cum_profit_bound += items[next_level].profit

    if next_level < len(items):
        cum_profit_bound += (capacity - cum_weight) * (items[next_level].profit / items[next_level].weight)

    return cum_profit_bound


def solve(weights: tuple[int], profits: tuple[int], capacity: int) -> tuple[int, int, list[int], int]:
    items = sorted(
        [Item(weight=weight, profit=profit, idx=idx) for idx, (weight, profit) in enumerate(zip(weights, profits))],
        key=lambda item: item.profit / item.weight, reverse=True)
    max_profit = 0
    num_of_intermediate_solutions = 0
    max_profit_node = None
    queue = PriorityQueue()
    node = Node(-1, None, None, 0, 0)
    queue.put(node)

    while not queue.empty():
        node = queue.get()

        if node.level == len(items) - 1:
            continue
        else:
            left_node = Node(node.level + 1, node, items[node.level + 1],
                             node.cum_profit + items[node.level + 1].profit,
                             node.cum_weight + items[node.level + 1].weight)

        if left_node.cum_weight <= capacity and left_node.cum_profit > max_profit:
            max_profit = left_node.cum_profit
            max_profit_node = left_node

        left_node_bound = upper_bound(left_node, capacity, items)
        if left_node_bound > max_profit:
            queue.put(left_node)

        right_node = Node(node.level + 1, node, None, node.cum_profit, node.cum_weight)
        right_node_bound = upper_bound(right_node, capacity, items)
        if right_node_bound > max_profit:
            queue.put(right_node)
        num_of_intermediate_solutions += 2

    ans_items = [0] * len(items)
    current_node = max_profit_node
    while current_node is not None:
        if current_node.item is not None:
            ans_items[current_node.item.idx] = 1
        current_node = current_node.parent

    return max_profit, max_profit_node.cum_weight, ans_items, num_of_intermediate_solutions
