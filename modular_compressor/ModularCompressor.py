#!/usr/bin/env python3

from model import Model
from csvparser import CSVParser
import compressionEngine


def main():
    # Create an empty Model
    model = Model()

    # create a CSV Parser
    parser = CSVParser(model)

    # Loop over all the slices of input data, compress, and write to the output
    while True:
        # Read the next slice of blocks
        num_blocks = parser.read()
        if num_blocks == 0:
            break
        
        # compress them
        compressionEngine.run(model)
        
        # write out this slice before moving on to the next slice
        parser.write()


if __name__ == '__main__':
    main()
