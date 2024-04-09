from copy import deepcopy


class NonBinTree:
    def __init__(self, val, var_name=""):
        self.var_name = var_name
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))
    
    def __repr__(self):
        return f"{self.val} -> {self.nodes}"


# class TreeManager:
#     def __init__(self, ):

def add_node(tree, value, location_list):
    expr1 = tree.var_name
    expr2 = ".".join([f"nodes[{idx}]" for idx in location_list])
    expr3 = f"add_node({value})"

    # expr_list = [expr for expr in [expr1, expr2, expr3] if expr]
    expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
    expression = ".".join(expr_list)

    print(expression)

    eval(expression)


def get_value(tree, location: list):
    expr1 = tree.var_name
    expr2 = ".".join([f"nodes[{el}]" for el in location])
    expr3 = "val"

    expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
    expression = ".".join(expr_list)

    print(expression)

    return eval(expression)


def get_values(tree, location: list):
    # values = []

    # for depth in range(len(location) + 1):
    #     value = get_value(tree, location[:depth])
    #     values.append(value)
    
    # return values

    return [get_value(tree, location[:depth]) for depth in range(len(location) + 1)]


def get_count(values: list):
    ops_length = sum(isinstance(val, str) for val in values)
    counter_value = len(values) - ops_length
    return counter_value









if __name__ == "__main__":
    operators = ['+', '-', '*', '/']
    numbers = [8, 7, 6, 5]

    print(f'operators: {operators}')
    print(f'numbers: {numbers}')
    print()

    nums = deepcopy(numbers)
    ops = []

    tree_main = NonBinTree(nums.pop(0), var_name="tree_main")
    tree_sub = NonBinTree((nums, ops), var_name="tree_sub")
    tree_counter = NonBinTree(1, var_name="tree_counter")

    print(f'tree_main: {tree_main}')
    print(f'tree_sub: {tree_sub}')
    print(f'tree_counter: {tree_counter}')


    # 初期位置は空のリストで表現
    print()
    print()
    print("tree_main")
    initial_location = []
    nums = deepcopy(tree_sub.val[0])
    val = nums.pop(0) # おそらく pop はインデックスを参照して要素をリストから取り出しているはず
    add_node(tree_main, val, initial_location)
    print(tree_main)
    
    print()
    print()
    print("tree_counter")
    next_location = [0]
    values_tmp = get_values(tree_main, next_location)
    print(values_tmp)
    print(get_count(values_tmp))
    count = get_count(values_tmp)
    add_node(tree_counter, count, initial_location)
    print(tree_counter)

    # tree_sub を更新
    print()
    print()
    print("tree_sub")
    add_node(tree_sub, nums, initial_location)
    print(tree_sub)

    # ルールにしたがって，深さ優先探索するように
    