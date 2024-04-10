from copy import deepcopy
from typing import Union


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

# def add_node(tree, value, location, return_new_location=False):
#     expr1 = tree.var_name
#     expr2 = ".".join([f"nodes[{idx}]" for idx in location])
#     expr3 = f"add_node({value})" if type(value) != str else f"add_node(r'{value}')"
#     expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
#     expression = ".".join(expr_list)
#     eval(expression)

#     if return_new_location:
#         expr_list = [expr1, expr2, "nodes"] if expr2 else [expr1, "nodes"]
#         expression = ".".join(expr_list)
#         breadth = eval(f"len({expression})") # ここで，breadth < 1 となると困る
#         new_location = deepcopy(location)
#         new_location.append(breadth - 1)
#         return new_location


# def get_value(tree, location: list):
#     expr1 = tree.var_name
#     expr2 = ".".join([f"nodes[{el}]" for el in location])
#     expr3 = "val"
#     expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
#     expression = ".".join(expr_list)
#     return eval(expression)


# def get_root_to_leaf_values(tree, location: list):
#     return [get_value(tree, location[:depth]) for depth in range(len(location) + 1)]


# def get_count(values: list):
#     return sum(1 if isinstance(val, int) else -1 for val in values)



# def move_to_bottom(tree_main, tree_counter, stack, location: list):
#     operators = ['+', '-', '*', '/']
    
#     while location


#     return final_location

# def move_one_step_deeper(tree_main, tree_counter, stack, operators, location):
#     '''
#     tree_main
#     '''
#     location_previous = deepcopy(location)
    
#     if len(location) == 1:
#         ops



class Solver:
    def __init__(
            self, 
            numbers: list[int], 
            target_number: int = 24
        ) -> None:

        self.numbers = numbers
        self.operators = ['+', '-', '*', '/']
        self.target_number = target_number

        # self.tree_main = NonBinTree(self.target_number, var_name="self.tree_main")
        # self.tree_counter = NonBinTree(1, var_name="self.tree_counter")
        self.tree_main = None
        self.tree_counter = None
        self.stack = []


    def add_node(
            self, 
            tree: NonBinTree, 
            value: Union[int, str], 
            location: list[int], 
            return_new_location: bool = False
        ) -> Union[None, list[int]]:

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


    def get_value(
            self, 
            tree: NonBinTree, 
            location: list[int]
        ) -> Union[int, str]:

        expr1 = tree.var_name
        expr2 = ".".join([f"nodes[{el}]" for el in location])
        expr3 = "val"
        expr_list = [expr1, expr2, expr3] if expr2 else [expr1, expr3]
        expression = ".".join(expr_list)
        return eval(expression)


    def get_root_to_leaf_values(
            self, 
            tree: NonBinTree, 
            location: list[int]
        ) -> list[Union[int, str]]:

        return [get_value(tree, location[:depth]) for depth in range(len(location) + 1)]


    def get_count(
            self, 
            values: list[Union[int, str]]
        ) -> int:

        return sum(1 if isinstance(val, int) else -1 for val in values)
    
    def solve(self):
        print(f'target number: {self.target_number}')
        print(f'operators: {self.operators}')
        print(f'numbers: {self.numbers}')
        print(f'stack:')
        for el in self.stack:
            print(el)
        print()

        self.tree_main = NonBinTree(target_number, "self.tree_main")
        self.tree_counter = NonBinTree(1, "self.tree_counter")

        nums = deepcopy(self.numbers)
        ops = []
        self.stack.append((nums, ops))
        print(f'main: {self.tree_main}')
        print(f'counter: {self.tree_counter}')
        print(f'stack:')
        for el in self.stack:
            print(el)
        print()

        location = [0]



if __name__ == "__main__":
    target_number = 24
    numbers = [5, 6, 7, 8]

    solver = Solver(numbers, target_number=target_number)
    solver.solve()







# if __name__ == "__main__":
#     target_number = 24

#     # operators = ['+', '-', '*', '/']
#     numbers = [8, 7, 6, 5]

#         print(f'target number: {target_number}')
#         print(f'operators: {operators}')
#         print(f'numbers: {numbers}')
#         print()



#     stack = []

#     tree_main = NonBinTree(target_number, var_name="tree_main")
#     tree_counter = NonBinTree(1, var_name="tree_counter")

#     nums = deepcopy(numbers)
#     ops = [] 
#     stack.append((nums, ops))

#     print(f'tree_main: {tree_main}')
#     print(f'tree_counter: {tree_counter}')
#     print(f'stack: {stack}')


    # move to the bottom
    # location = []
    # print()ｃｌ

    # while len(location) < 8:
    #     location_previous = deepcopy(location)

    #     if len(location) == 1:
    #         ops = deepcopy(operators)
    #     # elif len(location) == 7:
    #     #     ops = ['-']
    #     # elif len(location) == 8:
    #     #     ops = []

    #     nums = deepcopy(stack[len(location_previous)][0])
    #     if nums:
    #         val = nums.pop(0)
    #     else:
    #         ops = deepcopy(operators)
    #         val = ops.pop(0)
    #     location = add_node(tree_main, val, location_previous, return_new_location=True)

    #     rl_values = get_root_to_leaf_values(tree_main, location)
    #     count = get_count(rl_values)
    #     add_node(tree_counter, count, location_previous)

    #     if count > 1:
    #         ops = deepcopy(operators[1:]) # 仮
    #     elif len(location) == 7:
    #         ops = ['-']
    #     elif len(location) == 8:
    #         ops = []
        
    #     print(f'len stack: {len(stack)}')
    #     print((nums, ops))
    #     stack.append((nums, ops))

    #     print()
    #     for el in stack:
    #         print(el)
    #     print()

    #     # if len(location) == 8 or :
            



    # print()
    # print()
    # print(f'tree_main: {tree_main}')
    # print(f'tree_counter: {tree_counter}')
    # print(f'stack: ')
    # for el in stack:
    #     print(el)
    # print(f'len stack: {len(stack)}')
    # print()
    # print(len(location))









        
