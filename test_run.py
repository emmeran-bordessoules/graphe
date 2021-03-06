import math


MAP_ROW = 37
MAP_COL = 43

map = [[ 20, 20, 20, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 70, 20, 20, 20, 20, 20, 20, 20, 20, 70, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 70, 20, 70, 70, 70, 70, 70, 70, 20, 70, 20, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 5, 5, 5, -1, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 70, 20, 70, 20, 20, 20, 20, 70, 20, 70, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 5, 5, 5, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 70, 20, 70, 20, 70, 70, 20, 70, 20, 70, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 5, 5, 5, -1, -1, -1, 20, 20, 70, 70, 70, 70, 20, 20, 20, 20 ],
[ 20, 20, 20, 70, 20, 70, 20, 70, 20, 20, 70, 20, 70, 20, -1, -1, -1, -1, -1, -1, 5, 5, 5, -1, -1, -1, 5, 5, 5, 5, -1, -1, -1, -1, 20, 20, 70, 70, 20, 20, 70, 70, 70 ],
[ 20, 70, 20, 70, 20, 70, 20, 70, 70, 70, 70, 20, 70, 20, -1, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, -1, -1, -1, -1, 20, 20, 70, 70, 70, 70, 70, 70, 20 ],
[ 20, 70, 20, 70, 20, 70, 20, 20, 20, 20, 20, 20, 70, 20, 20, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20, 70, 70, 70, 20, 20 ],
[ 70, 70, 20, 70, 20, 70, 70, 70, 70, 70, 70, 70, 70, 20, 20, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20, 20, 70, 70, 70, 70, 20 ],
[ 70, 20, 20, 20, 20, 70, 20, 70, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 70, 20, 70, 70, 70, 70, 20, 70, 70, 70, 20, 70, 70, 70, 20, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 20, 70, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, 5, 5, 5, 5, 5, 5, 5, -1, -1, -1, 20, 20, 20, 20, 20, -1, -1, 70, 70, 70, 70, 70, 70, 70, 20 ],
[ 20, 20, 20, 20, 20, 70, 70, 70, 20, 20, 20, 20, 20, 20, -1, -1, -1, -1, 5, 5, -1, 5, -1, 5, 5, -1, -1, -1, -1, 20, 20, 20, 20, -1, -1, -1, -1, 70, 70, 70, 70, 70, 20 ],
[ 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 5, 70, 70, 20, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20, 20, -1, -1, -1, 70, 70, 70, 70, 20, 20 ],
[ 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 5, 70, 70, 20, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 70, 70, 70, -1, 70, 70, 70, 70, 20, 20, 20 ],
[ 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 5, 70, 70, 70, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, 20, 20, 70, 70, 70, 70, -1, -1, 70, 70, 70, 70, 20, 20 ],
[ 20, 20, 20, 20, 20, 70, 70, 70, 70, 70, 5, 70, 70, 70, 70, -1, -1, -1, -1, 20, 20, 5, 20, 20, -1, -1, -1, -1, 20, 20, 20, 20, 70, 70, -1, -1, -1, -1, 70, 70, 70, 70, 70 ],
[ 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 5, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 20, 70, 70, 70, 70 ],
[ 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 20, 20, 20, 20, 20, 20 ],
[ 20, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 70, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 70, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 70, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 70, 70, 20, -1, -1, -1, 20, -1, -1, 20 ],
[ -1, 70, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 5, 70, 70, 20, 20, -1, -1, -1, -1, -1, 20 ],
[ -1, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 5, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 5, 70, 70, 70, 20, 20, -1, -1, -1, 20, 20 ],
[ 20, -1, -1, -1, -1, -1, -1, 20, 20, 5, 5, 5, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 20, 70, 70, 70, 70, 70, 5, 5, 70, 70, 70, 20, 20, -1, -1, 20, 20 ],
[ 20, 20, 20, 20, -1, -1, -1, -1, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 5, 5, 70, 70, 70, 70, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 20, 20, -1, -1, -1, 5, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 70, 70, 70, 70, 70, 20, 20, 5, 20, 20, 70, 70, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 20, 20, 20, 20, -1, 5, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 5, 5, 70, 70, 70, 70, 70, 70, 70, 70, 20, 20, 20, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 20, 20, 20, 20, 20, 5, 20, -1, -1, -1, 20, 20, 20, 20, 20, 5, 5, 5, 5, 70, 70, 70, 70, 70, 70, 70, 20, 20, 70, 70, 5, 5, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 20, 20, 5, 5, 5, 5, 20, 20, -1, -1, -1, -1, 20, 20, 20, 20, 5, 5, 5, 5, 5, 70, 70, 70, 70, 70, 20, 20, 70, 70, 70, 5, 5, 5, 5, 5, 20, 20, 20 ],
[ 20, 20, 20, 70, 70, 5, 5, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, -1, 20, 20, 20, 20, 5, 5, 5, 70, 70, 70, 70, 70, 20, 20, 70, 70, 70, 70, 20, 20, 20, 5, 5, 20, 20 ],
[ 20, 70, 70, 70, 70, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -1, -1, -1, 20, 20, 20, 20, 70, 70, 70, 70, 70, 20, 20, 20, 20, -1, -1, -1, -1, -1, -1, 20, 20, 5, 5, 5 ],
[ 20, 70, 70, 70, 70, 5, 20, 20, 20, 70, 70, 70, 20, 20, 20, 20, 20, -1, -1, -1, 20, 20, 20, 20, 70, 70, 70, 20, 20, 20, 20, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 20, 20 ],
[ 70, 70, 70, 70, 70, 5, 20, 20, 70, 70, 70, 70, 70, 70, 20, 20, 20, 20, -1, -1, 20, 20, 20, 20, 70, 70, 70, 70, 20, 20, -1, -1, -1, 20, 20, 20, -1, -1, -1, 20, 20, 20, 20 ],
[ 70, 70, 70, 20, 5, 5, 20, 20, 20, 70, 70, 70, 70, 70, 70, 70, 20, 20, -1, -1, -1, 20, 20, 20, 20, 70, 70, 70, 70, 20, 20, -1, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 20, 20, -1, -1, -1, -1, 20, 20, 20, 70, 70, 70, 70, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ],
[ 20, 20, 20, 20, 5, 20, 20, 20, 20, 20, 20, 20, 20, 70, 70, 70, 70, 20, 20, 20, 20, -1, -1, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20 ]]

def exterieur_map(x, y):
    if x < 0 or x > MAP_COL-1 or y < 0 or y > MAP_ROW-1:
        return True
    return False

def bloquer(x, y):
    if map[y][x] == -1:
        return True
    return False

def peut_se_deplacer(p):
    x, y = p
    if exterieur_map(x, y):
        return False
    if bloquer(x, y):
        return False
    return True

def voisins_proches(p):
    x, y = p
    voisins = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return filter(peut_se_deplacer, voisins)


def distance_heuristique(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def distance_case(p1, p2):
    return map[p2[1]][p2[0]]

def astar(debut, cible, voisins_proches, distance_case, distance_heuristique):
    closedset = []
    openset   = [debut]
    came_from = {}
    g_score   = {}
    f_score   = {}
    g_score[debut] = 0
    f_score[debut] = g_score[debut] + distance_heuristique(debut, cible)
    while openset:
        current = min((f_score[node], node) for node in openset)[1]
        if current == cible:
            return reconstruire_chemin(came_from, cible)
        openset.remove(current)
        closedset.append(current)
        for voisin in voisins_proches(current):
            tentative_g_score = g_score[current] + distance_case(current, voisin)
            tentative_f_score = tentative_g_score + distance_heuristique(voisin, cible)
            if voisin in closedset and tentative_f_score >= f_score[voisin]:
                continue
            if voisin not in openset or tentative_f_score < f_score[voisin]:
                came_from[voisin] = current
                g_score[voisin] = tentative_g_score
                f_score[voisin] = tentative_f_score
                if voisin not in openset:
                    openset.append(voisin)
    return None

def reconstruire_chemin(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    return path


if __name__ == '__main__':
    agent = [(29, 2),(2,0),(4,7),(9,31),(22,31),(30,18),(31,27),(41,7),(40,10),(42,18),(40,20),(42,22),(35,34)]
    cible  = (21, 5)
    for i in agent:
        path  = astar(i, cible, voisins_proches, distance_case, distance_heuristique)
        if path:
            print("<=================>")
            string = " Chemin De l'agent " + str(i) + " à la cible  " + str(cible)
            print(string)
            for position in reversed(path):
                x,y = position
                
                print(x,y)
<<<<<<< HEAD
=======
               
				

>>>>>>> origin/master
