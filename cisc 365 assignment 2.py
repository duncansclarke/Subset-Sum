# Duncan Clarke
# 20056561
# I certify that this submission contains my own work, except as noted.

class Set:
    """ A  set of positive integers (duplicates possible)
    Attributes
    ---------------
    elements (list):
        A list containing the positive integers of the set
    sum (int):
        The sum of all integers in the set
    """
    def __init__(self, elements, sum):
        self.elements = elements
        self.sum = sum

# Instantiate empty set object
empty_set = Set([],0)

# Sample set
S = [3,5,3,9,18,4,5,6]

def BFI_Subset_Sum(S,k):
    """
    Finds a subset of integers from the set S that sums exactly to some integer k (if such a subset exists).
    The function does this by generating all subsets of S and computing each corresponding sum.
    Parameters
    ---------------
    S (list):
        The set of integers
    k (int):
        The target sum
    """
    # Handles case where target value is the sum of the entire set
    if k == sum(S):
        return S
    # Create list subsets containing the empty set
    subsets = [empty_set]
    for i in range(1, len(S)):
        new_subsets = [] # list to contain set objects
        for old_u in subsets:
            # Create new set object with old_u's elements and the current element of S
            new_set_elements = [S[i]] +(old_u.elements)
            new_u = Set(new_set_elements, old_u.sum + S[i])
            # Check if this new subset is the target sum... if so, done
            if new_u.sum == k:
                return new_u.elements
            else:
                new_subsets.append(old_u)
                new_subsets.append(new_u)
        subsets = new_subsets
    # No solution is found
    return "no subsets sum to target value"

def modified_BFI_Subset_Sum(S):
    """
    Modified version of the BFI_Subset_Sum algorithm which generates a list of all subsets and their corresponding sums from set S
    Parameters
    ---------------
    S (list):
        The set of integers
    """
    # Create list subsets containing the empty set
    subsets = [empty_set]
    all_subsets = []
    for i in range(1, len(S)):
        new_subsets = [] # list to contain set objects
        for old_u in subsets:
            # Create new set object with old_u's elements and the current element of S
            new_set_elements = [S[i]] +(old_u.elements)
            new_u = Set(new_set_elements, old_u.sum + S[i])
            new_subsets.append(old_u)
            new_subsets.append(new_u)
            all_subsets.append(old_u)
            all_subsets.append(new_u)
        subsets = new_subsets
    return all_subsets


def HS_Subset_Sum(S,k):
    """
    Finds a subset of integers from the set S that sums exactly to some integer k (if such a subset exists).
    The function does this by using a divide and conquer approach.
    Checks subsets and sums in each half of S and then checks subset sums from combining subsets from each half.
    Parameters
    ---------------
    S (list):
        The set of integers
    k (int):
        The target sum
    """
    # Handles case where target value is the sum of the entire set
    if k == sum(S):
        return S

    # split list S in half, with S_left containing the first half and S_right containing the second half
    half = len(S)//2
    S_left = S[:half]
    S_right = S[half:]

    # Get list of all subsets and their sums in left half
    left_sets = modified_BFI_Subset_Sum(S_left)

    # Get list of all subsets and their sums
    right_sets = modified_BFI_Subset_Sum(S_right)

    # If k is one of the subset sums on the left list, print the subset and finish
    for i in range(0, len(left_sets)):
        if k == left_sets[i].sum:
            print(left_sets[i].elements)
            return
    # If k is one of the subset sums on the right list, print the subset and finish
    for i in range(0, len(right_sets)):
        if k == right_sets[i].sum:
            print(left_sets[i].elements)
            return

    # Sort each list of subsets in ascending order by the set's corresponding sum
    left_sets.sort(key=lambda x: x.sum)
    right_sets.sort(key=lambda x: x.sum)

    # Use pair sum algorithm to find 2 sums from the left and right half that add up to k
    subset_pair = Pair_Sum(left_sets, right_sets, k)
    # If such an x and y don't exist, print failure statement
    if subset_pair == (-1,-1):
        print("No subset sums to the target value")
    else:
        left_set = subset_pair[0]
        right_set = subset_pair[1]
        subset = left_set.elements + right_set.elements
        print(subset)

def Pair_Sum(lis1, lis2, k):
    """
    Finds integer x from one (sorted) set and integer y from another (sorted) set such that x + y = k (for some integer k).
    Does this by checking the sum of the first value of list 1, and the final value of list 2, and eliminating one of those values depending whether it is > or < k
    Parameters
    ---------------
    lis1 (list):
        The first set of integers
    lis2 (list):
        The second set of integers
    k (int):
        The target sum
    """
    p1 = 0 # index being checked on lis1, starting at the first index
    p2 = len(lis2)-1 # index being checked on lis2, starting at the final index
    # iterates over lis1 ascending and lis2 descending
    while (p1 < len(lis1)) and (p2 >= 0):
        # computes sum of lis1's element at p1 and lis2's element at p2
        t = lis1[p1].sum + lis2[p2].sum
        # finish if this sum is the target value
        if t == k:
            return (lis1[p1],lis2[p2])
        # increment the index for lis1 if the computed sum is too small
        elif t < k:
            p1 = p1+1
        # decrement the index value for lis2 if the computed sum is too large
        else:
            p2 = p2-1
    return (-1,-1)
