from kanren import conde, Relation, var

# declaration of the relations
has_id = Relation()
is_before = Relation()
assigns = Relation()
uses = Relation()
hasOutput = Relation()  # line L has output of value V

# define the data dependency relationship
def depends(a, b):
    '''there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target'''
    shared_id = var()
    return conde([is_before(a, b), assigns(a, shared_id), uses(b, shared_id)])