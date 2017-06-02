from kanren import Relation, facts, run, var, conde
from itertools import combinations

# TODO: what about empty lines?

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

n = var()
l1 = var()
l2 = var()
l3 = var()

hasID = Relation()
isBefore = Relation()
isAssigned = Relation()

# quick bootstrap of knowledge base
# line # has name
facts(hasID, (1, "x"),
             (2, "y"),
             (3, "x"),
             (4, "y"),
             (5, "x"),
             (6, "x"))

# this is a quick add of all combinations of line numbers from 1-6 by pairs of two
# such that for pair (a, b), a < b holds true
# since you can't do logical x < logical y, using this statement works
facts(isBefore, *combinations(range(1, 7), 2))


# (1,1), (3,3) are not useful
# (1,3), (3,1) are the same
result1 = run(0, (l1, l2), hasID(l1, "x"), hasID(l2, "x"))
result2 = run(0, (l1, l2), dependent(l1, l2, "y"))
result3 = run(0, (l1, l2), dependent2(l1, l2))
result4 = run(0, (l1, l2, l3), transdepend(l1, l2, l3))
print(result4)

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

print()

print("Pairs of lines that are dependent on each other: ")
for a, b in filter(lambda x: x[0] != x[1], result3):
    print(a, b)
