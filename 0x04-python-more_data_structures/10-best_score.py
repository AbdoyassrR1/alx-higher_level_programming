#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary or len(a_dictionary) == 0:
        return None
    else:
        nums = []
        for key in a_dictionary:
            nums.append(a_dictionary[key])

        for key, val in a_dictionary.items():
            if val == max(nums):
                best = key

    return best
