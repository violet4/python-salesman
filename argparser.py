import argparse

parser = argparse.ArgumentParser(
      description = "Parse TSP files and calculate paths using simple "
                    "algorithms.")

parser.add_argument (
      "-n"
    , "--nearest"
    , action  = "store_true"
    , dest    = "need_nearest_neighbor"
    , default = False
    , help    = "calculate distance traveled by nearest neighbor heuristic"
    )

parser.add_argument (
      "-f"
    , "--furthest"
    , action  = "store_true"
    , dest    = "need_furthest_neighbor"
    , default = False
    , help    = "calculate distance traveled by furthest insertion heuristic"
    )

parser.add_argument (
      "-i"
    , "--in-order"
    , action  = "store_true"
    , dest    = "need_in_order"
    , default = False
    , help    = "calculate the distance traveled by the in-order-tour [1..n,1]"
    )

parser.add_argument (
      "-p"
    , "--print-tours"
    , action  = "store_true"
    , dest    = "need_tours_printed"
    , default = False
    , help    = "print explicit tours"
    )

parser.add_argument (
      "tsp_queue"
    , nargs   = "+"
    , metavar = "PATH"
    , help    = "Path to directory or .tsp file. If PATH is a directory, run "
                "on all .tsp files in the directory."
    )
