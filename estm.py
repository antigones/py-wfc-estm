from collections import defaultdict
import random as rd
import numpy as np
import math

from utils import get_neighbours

class ESTM:

    def __init__(self, size, rules, weights):
        self.size = size
        self.height = size
        self.width = size
        self.rules = rules
        self.weights = weights
        self.matrix = [[set(self.rules.keys()) for _ in range(self.size)] for _ in range(self.size)]
        self.entropies = {(x,y):self.shannon_entropy(self.matrix[x][y]) for x in range(self.size) for y in range(self.size)} 
        self.visited = set()
    

    def check_finished(self):
        return all(e == 0 for e in self.entropies.values())
    
    def shannon_entropy(self,tile):
        weight = [self.weights[x] for x in tile]
        return np.log(np.sum(weight)) - (np.sum(weight * np.log(weight)) / np.sum(weight))
    
    def propagate(self, x, y):
        # la union di tutte le scelte che ogni singola scelta può avere in una determinata direzione,
        # messa a confronto con quel che c'è già
        to_visit = set()
        to_visit.add((x,y))
        prop_visited = set()
        while len(to_visit) > 0:
            to_visit_x, to_visit_y = to_visit.pop()
            prop_visited.add((to_visit_x,to_visit_y))
            neighbours = get_neighbours(to_visit_x, to_visit_y, self.height, self.width)
            for neighbour in neighbours:
                nx,ny = neighbour
                if neighbour not in prop_visited and self.entropies[(nx,ny)] != 0:
                    ammissible_values_for_neighbours = set()
                    for elm in self.matrix[to_visit_x][to_visit_y]:
                        tile_rules = self.rules[elm]
                        rx,ry = nx-to_visit_x,ny-to_visit_y
                        mapp = tile_rules[(rx,ry)]
                        for e in mapp:
                            ammissible_values_for_neighbours.add(e)
                    if len(ammissible_values_for_neighbours) == 0:
                        raise Exception('Could not collapse!')
                    self.matrix[nx][ny] = self.matrix[nx][ny].intersection(ammissible_values_for_neighbours)
                    self.entropies[(nx,ny)] = self.shannon_entropy(self.matrix[nx][ny])
                    to_visit.add((nx,ny))


    def solve(self):
       
        while not self.check_finished():
            print('***ITERATION***')
            not_visited_entropies = {k:v for k,v in self.entropies.items() if k not in self.visited}
            possible_tiles = [k for k,v in not_visited_entropies.items() if v == min(not_visited_entropies.values())]
            rd_x, rd_y = rd.choices(possible_tiles)[0]
            self.visited.add((rd_x,rd_y))
            
            sorted_set = sorted(self.matrix[rd_x][rd_y])
            p = list()
            for v in sorted_set:
                p.append(self.weights[v])
            norm_p = [x+((1-sum(p))/len(p)) for x in p]
            chosen_elm = rd.choices(population=tuple(sorted_set),weights=norm_p,k=1)
            chosen_elm = chosen_elm[0]
            self.matrix[rd_x][rd_y] = {chosen_elm}
            self.entropies[(rd_x,rd_y)] = self.shannon_entropy(self.matrix[rd_x][rd_y])
            self.propagate(rd_x, rd_y)
        return self.matrix