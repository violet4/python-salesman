from collections import deque
from city        import distance, GeoCity, Euc_2D, GeoCoord
from tspparse    import read_tsp_file
from numpy       import array

def calc_distance(tsp, city1_index, city2_index):
    """Calculate distance between cities by their (one-based) indices"""
    cities = tsp["CITIES"]
    return distance(cities[city1_index - 1], cities[city2_index - 1])

def path_length(tsp,path):
    """Find the length of a path of cities given as a list"""
    if len(path) == 1:
        return 0
    else:
        start_node = path.pop()
        next_node  = path[-1]
        return calc_distance(tsp,start_node,next_node) + path_length(tsp,path)

def tour_from_path(path):
    """Append the first city in a path to the end in order to obtain a tour"""
    path.append(path[0])
    return path

def in_order_path(tsp):
    """Return the tour [1,2,...,n,1] where n is the dimension of the TSP"""
    dim = tsp["DIMENSION"]
    return list(range(1,dim+1))

def in_order_tour(tsp):
    """Return the tour obtained by traveling to each city in order and
circling around back to the first city"""
    return tour_from_path(in_order_path(tsp))

def calc_in_order_tour(tsp):
    """Calculate the distance of the in-order-tour for a tsp"""
    return path_length(tsp,in_order_tour(tsp))

def nearest_neighbor(tsp,untraveled_cities,current_city):
    """Given a set of city keys, find the key corresponding to the
closest city"""
    distance_to_current_city = lambda city: calc_distance(tsp,current_city,city)
    return min(untraveled_cities, key = distance_to_current_city)

def furthest_neighbor(tsp,untraveled_cities,current_city):
    """Given a set of city keys, find the key corresponding to the
closest city"""
    distance_to_current_city = lambda city: calc_distance(tsp,current_city,city)
    return max(untraveled_cities, key = distance_to_current_city)

def nearest_neighbor_tour(tsp):
    """Construct a tour through all cities in a TSP by following the nearest
neighbor heuristic"""
    nearest_neighbor_path = [1]
    current_city          = 1
    cities_to_travel      = set(range(2, tsp["DIMENSION"] + 1))

    while cities_to_travel:
        current_city = nearest_neighbor(tsp,cities_to_travel,current_city)
        nearest_neighbor_path.append(current_city)
        cities_to_travel.remove(current_city)

    return tour_from_path(nearest_neighbor_path)

def furthest_neighbor_tour(tsp):
    """Construct a tour through all cities in a TSP by following the furthest
neighbor heuristic"""
    nearest_neighbor_path = [1]
    current_city          = 1
    cities_to_travel      = set(range(2, tsp["DIMENSION"] + 1))

    while cities_to_travel:
        current_city = furthest_neighbor(tsp,cities_to_travel,current_city)
        nearest_neighbor_path.append(current_city)
        cities_to_travel.remove(current_city)

    return tour_from_path(nearest_neighbor_path)

def calc_nearest_neighbor_tour(tsp):
    return path_length(tsp,nearest_neighbor_tour(tsp))

def calc_furthest_neighbor_tour(tsp):
    return path_length(tsp,furthest_neighbor_tour(tsp))
