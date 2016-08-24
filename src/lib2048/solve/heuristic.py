
def minimum_number_of_cell(grid):
    return sum([r.count(0) for r in grid])

def avg(l):
    return sum(l) / len(l)
