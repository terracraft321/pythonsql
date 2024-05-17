def create_set():
    my_set = {1, 2, 3, 4, 5}
    print(my_set)
#{1, 2, 3, 4, 5}

def add_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    print(my_set)
    #1,2,3,4,5,6


def remove_element():
    my_set = {1, 2, 3, 4, 5}
    my_set.remove(3)
    print(my_set)
    #1,2,4,5


def clear_set():
    my_set = {1, 2, 3, 4, 5}
    my_set.clear()
    print(my_set)
    #empty set


def set_union():
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    my_set = set1.union(set2) ###1,2,3,4,5,6
    print(my_set)


def set_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8} ### 4,5
    my_set = set1.intersection(set2)
    print(my_set)


def set_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    my_set = set1.difference(set2) ## / drop
    ## 1,2,3
    print(my_set)


def set_symmetric_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    ## 1,2,3,6,7,8
    my_set = set1.symmetric_difference(set2)
    print(my_set)


def set_subset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    subset = set2.issubset(set1)
    print(subset)
    ##yes


def set_superset():
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    superset = set1.issuperset(set2)
    print(superset)
    #yeah


if __name__ == '__main__':
    create_set()
    add_element()
    remove_element()
    clear_set()
    set_union()
    set_intersection()
    set_difference()
    set_symmetric_difference()
    set_subset()
    set_superset()
