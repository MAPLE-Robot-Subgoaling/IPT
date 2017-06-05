from kanren import Relation, facts, run, var, conde
from itertools import combinations

# TODO: what about empty lines?
# probably skip them


def dependent(line1, line2, name):
    """
    two lines a,b are dependent on a name if they both use that name
    this is not necessarily true in practice, consider this:
    w = 3
    x = 4 * w
    y = 9 * x
    z = x + 9
    print(z)
    
    the goal is print z, y is extraneous, but z and y share x and would therefore be considered dependent
    in essence, I either don't want to capture every dependency or I need to be more specific with the rule
    
    """

    # both lines have the same name AND line1 comes before line 2
    return conde([hasID(line1, name),
                  hasID(line2, name),
                  isBefore(line1, line2)])


def dependent2(line1, line2):
    """
    Attempt to find all pairs of lines that are dependent on a name
    """
    name = var()

    return conde([hasID(line1, name),
                  hasID(line2, name),
                  isBefore(line1, line2)])


def transdepend(a, b, c):
    n = var()
    return conde([dependent(a,b,n), dependent(b,c,n)])


def depends(a,b):
    '''there is a dependency between two lines {A, B} if:
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target'''
    shared_id = var()
    return conde([
                  isBefore(a, b),
                  assigns(a, shared_id),
                  uses(b, shared_id)
                  ])

n = var()
l1 = var()
l2 = var()
l3 = var()

hasID = Relation()
isBefore = Relation()
assigns = Relation()
uses = Relation()

num_lines = 5

# quick bootstrap of knowledge base
# [1] x = 5
# [2] y = 5
# [3] z = 7
# [4] val = x + y
# [5] print(val)


# line # has id
facts(hasID, (1, "x"), (2, "y"), (3, "z"), (4, "val"), (4, "x"), (4, "y"), (5, "val"))

# this is a quick add of all combinations of line numbers from 1-5 by pairs of two
# such that for pair (a, b), a < b holds true
# since you can't do logical x < logical y, using this statement works
facts(isBefore, *combinations(range(1, num_lines + 1), 2))

# ID name is assigned on line no #
facts(assigns, (1, "x"), (2, "y"), (3, "z"), (4, "val"))

facts(uses, (4, "x"), (4, "y"), (5, "val"))

# (1,1), (3,3) are not useful
# (1,3), (3,1) are the same


result1 = run(0, (l1, l2), hasID(l1, "x"), hasID(l2, "x"))
result2 = run(0, (l1, l2), dependent(l1, l2, "val"))
result3 = run(0, (l1, l2), dependent2(l1, l2))
result4 = run(0, (l1, l2, l3), transdepend(l1, l2, l3))

'''
# this is how you remove duplicates in the results
s = set([tuple(sorted(l)) for l in result1])
print("Result1: ", result1)
print("Result1 no dups: ", s)
print()

# remove duplicates in results after filtering out (a,a), (b,b), etc.
s = set([tuple(sorted(l)) for l in filter(lambda x: x[0] != x[1], result1)])
print("Result1: ", result1)
print("Result1 no dups or same: ", s)
print()

print("Pairs of lines that have name 'x': ")
for a, b in s:
    print(a, b)

'''
print()

print("Pairs of lines that are dependent1 on each other: ")
for a, b in filter(lambda x: x[0] != x[1], result2):
    print(a, b)
print()

print("Pairs of lines that are dependent2 on each other: ")
for a, b in filter(lambda x: x[0] != x[1], result3):
    print(a, b)


print()
print("New depends function:")
result5 = run(0, (l1, l2), depends(l1, l2))
print(result5)
