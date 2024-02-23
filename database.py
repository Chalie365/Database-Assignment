class MinitermGenerator:
    def __init__(self, relations):
        self.relations = relations

    def generate_miniterm_fragments(self, predicates):
        miniterms = []
        for predicate in predicates:
            miniterm = []
            for relation in self.relations:
                if relation in predicate:
                    miniterm.append(predicate)
                else:
                    miniterm.append('NOT ' + predicate)
            miniterms.append(miniterm)
        return miniterms