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

def add_node(tree, value, location, return_new_location=False):
    expr1 = tree.var_name
    expr2 = ".".join([f"nodes[{idx}]" for idx in location])
    expr3 = f"add_node({value})"
    expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
    expression = ".".join(expr_list)
    eval(expression)

    if return_new_location:
        expr_list = [expr1, expr2, "nodes"] if expr2 else [expr1, "nodes"]
        expression = ".".join(expr_list)
        breadth = eval(f"len({expression})") # ここで，breadth < 1 となると困る
        new_location = deepcopy(location)
        new_location.append(breadth - 1)
        return new_location


def get_value(tree, location: list):
    expr1 = tree.var_name
    expr2 = ".".join([f"nodes[{el}]" for el in location])
    expr3 = "val"
    expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
    expression = ".".join(expr_list)
    return eval(expression)


def get_values(tree, location: list):
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
    ops = ['id'] # 空のリストだと下に行けないため，仮の値を設定．恒等写像．

    tree_main = NonBinTree(nums.pop(0), var_name="tree_main")
    tree_numbers = NonBinTree(nums, var_name="tree_numbers")
    tree_operators = NonBinTree(ops, var_name="tree_operators")
    tree_counter = NonBinTree(1, var_name="tree_counter")

    print(f'tree_main: {tree_main}')
    print(f'tree_numbers: {tree_numbers}')
    print(f'tree_operators: {tree_operators}')
    print(f'tree_counter: {tree_counter}')


    # 初期位置は空のリストで表現
    initial_location = []
    nums = deepcopy(tree_numbers.val)
    val = nums.pop(0) 
    next_location = add_node(tree_main, val, initial_location, return_new_location=True)
    add_node(tree_numbers, nums, initial_location)
    ops = deepcopy(operators)
    add_node(tree_operators, operators, next_location)
    values_tmp = get_values(tree_main, next_location)
    count = get_count(values_tmp)
    add_node(tree_counter, count, initial_location)


    print()
    print()
    print()
    print(f'tree_main: {tree_main}')
    print(f'tree_numbers: {tree_numbers}')
    print(f'tree_operators: {tree_operators}')
    print(f'tree_counter: {tree_counter}')

    

    # ルールにしたがって，深さ優先探索するように
    