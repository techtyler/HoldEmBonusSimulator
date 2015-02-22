

class card_node(object):
    
    def new(id):
        _id = id
        count = 0
        ptrs = []
        
    def add_edge(card_node):
        ptrs.add(card_node)
        count += 1
        
    def rm_edge(card_node):
        ptrs.remove(card_node)
        count -= 1

    def get_highest_edge(self):
        edges_sorted = sorted([p._id for p in ptrs])
        return 14 if edges_sorted[0] == 1 else edges_sorted[-1]
