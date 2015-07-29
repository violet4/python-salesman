#!/usr/bin/env python3

from argparser  import parser
from tspparse   import read_tsp_file
from algorithms import ( calc_nearest_neighbor_tour
                       , calc_in_order_tour
                       , calc_furthest_neighbor_tour)


from glob    import iglob
from os.path import isfile, isdir, join, exists

def glean_tsp_files(path_arg_list):
    for path_arg in path_arg_list:

        if isdir(path_arg):
            for filepath in iglob(join(path_arg,"*.tsp")):
                yield filepath

        elif isfile(path_arg) & str(path_arg).endswith(".tsp"):
            yield path_arg

        elif isfile(path_arg) & (not path_arg.endswith(".tsp")):
            print("Can't open file ``{0}'': not a .tsp file".format(path_arg))

        elif exists(path_arg):
            print("Path {0} is neither a file nor a directory".format(path_arg))

        else:
            print("Path {0} does not exist".format(path_arg))

def print_results_from_tsp_path(call_args, tsp_path):
    tsp = read_tsp_file(tsp_path)
    print("TSP Problem:              {}".format(tsp["NAME"]))
    print("PATH:                     {}".format(tsp_path))

    if call_args.need_in_order:
        print("IN-ORDER TOUR LENGTH:     {}"
             . format(calc_in_order_tour(tsp)))

    if call_args.need_nearest_neighbor:
        print("NEAREST NEIGHBOR LENGTH:  {}"
             . format(calc_nearest_neighbor_tour(tsp)))

    if call_args.need_furthest_neighbor:
        print("FURTHEST NEIGHBOR LENGTH: {}"
             . format(calc_furthest_neighbor_tour(tsp)))

    print("")
    del(tsp)

def main():
    call_args = parser.parse_args()
    for tsp_path in glean_tsp_files(call_args.tsp_queue):
        print_results_from_tsp_path(call_args,tsp_path)

if __name__ == "__main__":
    main()
