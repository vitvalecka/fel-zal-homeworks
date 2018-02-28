def permutations(array):
    if len(array) <= 1:
        return [array]

    list_of_permutations = []

    for item in array:
        remaining_items = []

        for other_items in array:
            if other_items != item:
                remaining_items.append(other_items)

        recursion_permutations = permutations(remaining_items)

        for perms in recursion_permutations:
            list_of_permutations.append([item] + perms)

    return list_of_permutations
