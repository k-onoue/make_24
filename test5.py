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
    return sum(1 if isinstance(val, int) else -1 for val in values)



# def move_to_bottom(tree_main, tree_counter, stack, location: list):
#     operators = ['+', '-', '*', '/']
    
#     while location


#     return final_location






if __name__ == "__main__":
    target_number = 24

    operators = ['+', '-', '*', '/']
    numbers = [8, 7, 6, 5]

    print(f'target number: {target_number}')
    print(f'operators: {operators}')
    print(f'numbers: {numbers}')
    print()



    stack = []

    tree_main = NonBinTree(target_number, var_name="tree_main")
    tree_counter = NonBinTree(1, var_name="tree_counter")

    nums = deepcopy(numbers)
    ops = [] 
    stack.append((nums, ops))

    print(f'tree_main: {tree_main}')
    print(f'tree_counter: {tree_counter}')
    print(f'stack: {stack}')


    # move to the bottom
    location = []
    while len(location) < 7:
        location_previous = deepcopy(location)

        nums = deepcopy(stack[len(location_previous)])[0]
        val = nums.pop(0) if nums else ops.pop(0)
        location = add_node(tree_main, val, location_previous, return_new_location=True)

        rl_values = get_root_to_leaf_values(tree_main, location)
        count = get_count(rl_values)
        add_node(tree_counter, count, location_previous)

        if count > 1:
            ops = deepcopy(operators)

        stack.append((nums, ops))


    print()
    print()
    print(f'tree_main: {tree_main}')
    print(f'tree_counter: {tree_counter}')
    print(f'stack: {stack}')
    print()
    print(len(location))









        
