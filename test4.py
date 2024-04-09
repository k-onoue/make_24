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
    expr3 = f"add_node({value})" if type(value) != str else f"add_node(r'{value}')"
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


def get_root_to_leaf_values(tree, location: list):
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
    # previous_location
    # location
    # next_location
    # len(location) == 6 で式を評価

    location = []
    nums = deepcopy(get_value(tree_sub, location))[0]
    # val = nums.pop(0) if nums else ops.pop(0)
    val = nums.pop(0)
    next_location = add_node(tree_main, val, location, return_new_location=True)
    ops = deepcopy(operators)
    add_node(tree_sub, (nums, ops), location)
    rl_values = get_root_to_leaf_values(tree_main, next_location)
    count = get_count(rl_values)
    add_node(tree_counter, count, location)


    print()
    print()
    print()
    print(f'tree_main: {tree_main}')
    print(f'tree_sub: {tree_sub}')
    print(f'tree_counter: {tree_counter}')

    # ルールにしたがって，深さ優先探索するように
    while len(location) < 3:
        previous_location = deepcopy(location)
        location = deepcopy(next_location)

        nums = deepcopy(get_value(tree_sub, location))[0]
        val = nums.pop(0) if nums else ops.pop(0)
        next_location = add_node(tree_main, val, location, return_new_location=True)

        ops = deepcopy(ops)
        add_node(tree_sub, (nums, ops), location)
        rl_values = get_root_to_leaf_values(tree_main, next_location)
        count = get_count(rl_values)
        add_node(tree_counter, count, location)

        print()
        print()
        print(f'tree_main: {tree_main}')
        print(len(location))
        






        
