"""
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLLLLLL
LLLLLCLLCC
LLLLCSCCSS
LLLCSSSSSS
LLCSSSSSSS
LCSSSSSSSS
CSSSSSSSSS
"""

from collections import Counter, defaultdict
from utils import get_neighbours


class ESTMRuleParser():

    def __init__(self, matrix_str_repr: str):
        self.height = len(matrix_str_repr)
        self.width = len(matrix_str_repr[0])
        self.matrix = [list(matrix_str_repr[i]) for i in range(len(matrix_str_repr))]
    
    def calc_rules(self):
        rule_dict = defaultdict(lambda:dict())
        for i in range(self.height):
            for j in range(self.width):
                neighbours = get_neighbours(i,j,self.height,self.width)
                for neighbour in neighbours:
                    cur_elm = self.matrix[i][j]
                    nx,ny=neighbour
                    rx,ry=nx-i,ny-j
                    if (rx,ry) not in rule_dict[cur_elm].keys():
                        rule_dict[cur_elm][(rx,ry)] = set(self.matrix[nx][ny])
                    else:
                        rule_dict[cur_elm][(rx,ry)].add(self.matrix[nx][ny])
        flattened_matrix = "".join("".join(line) for line in self.matrix)
        counts = Counter(flattened_matrix)
        c_min = min(counts.values())
        c_max = max(counts.values())
        for k in counts:
            counts[k] = (counts[k]-c_min)/(c_max-c_min)
        weights = counts
        print(weights)
        return rule_dict, weights