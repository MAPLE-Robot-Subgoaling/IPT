from kanren import conde, Relation, var

class ResetableRelation(Relation):
    def reset(self):
        self.facts = set()
        self.index = dict()

# declaration of the relations
has_id = ResetableRelation("has_id")
is_before = ResetableRelation("is_before")
assigns = ResetableRelation("assigns")
uses = ResetableRelation("uses")
has_output = ResetableRelation("has_output")  # line L has output of value V
relations = [has_id, is_before, assigns, uses, has_output]

def reset_all_relations():
    for relation in relations:
        relation.reset()

def depends(a, b):
    '''there is a dependency between two lines {A, B} if:
    they share an ID X AND
    A comes before B AND
    X is a target for the assignment on line A AND
    B uses X (not just an assignment where X is a target'''
    shared_id = var()
    return conde([is_before(a, b), assigns(a, shared_id), uses(b, shared_id)])