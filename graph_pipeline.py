from src.format_data import format_data
from src.plot import plot_graph

import argparse
import os

def setup_directories():
    paths = ["csv_data/", "plots/"]
    for path in paths:
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path')
    args = parser.parse_args()
    
    setup_directories()

    csv_file_name = format_data(args.file_path)
    plot_graph(csv_file_name)
    


