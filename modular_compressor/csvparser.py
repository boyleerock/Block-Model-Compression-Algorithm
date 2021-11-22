"""
A module that contains the parsing to and from the CSV data format to the
internal representation. It should only read 1 ParentBlock slice in the z
direction. This requires that the CSV data is in sorted in the z direction.
"""

from model import Size, Position, Block, ParentBlock
import csv
import sys


class CSVParser:
    """
    A Parser that will read CSV data and add the blocks to a model, and write
    blocks from the model in CSV format.
    
    Parameters:
        model       The model to place the parsed ParentBlocks
        in_file     The file to read the data from. It defaults to STDIN
        out_file    The file to write to to. It defaults to STDOUT
    """

    def __init__(self, model, in_file=sys.stdin, out_file=sys.stdout):
        super(CSVParser, self).__init__()
        
        self.model = model
        
        # open the in file
        if in_file == sys.stdin:
            self.in_file = sys.stdin
        else:
            self.in_file = open(out_file, newline='')
            
        # open the out file
        if out_file == sys.stdout:
            self.out_file = sys.stdout
        else:
            self.out_file = open(out_file, newline='')
            
        # create the csv reader/writer
        self.reader = csv.reader(self.in_file)
        self.writer = csv.writer(self.out_file)
        
        # read the parent block line
        header = next(self.reader)
        if header[0][0] != '#':
            sys.exit(1)     # perhaps throw an error instead
            
        self.writer.writerow((header[0], header[1], header[2], header[3], header[4], header[5]))  # noqa
        
        header[0] = header[0].split()[1]    # remove the starting '#'
        self.model.size = Size(x=int(header[0]), y=int(header[1]), z=int(header[2]))    # noqa
        self.model.parent_block_size = Size(
            x=int(header[3]),
            y=int(header[4]),
            z=int(header[5])
        )
        
        self.slices = 0
        
    def read(self):
        """
        Adds parent blocks to the model. It will read a parent block slice of
        data (provided the data is sorted in the z direction). Once the last
        block has been read, according to the input file header, the parser
        will not read any more data.
                
        Returns:
            The number of blocks parsed
        """
        # calculate the number of parent blocks in the slice in each dimension
        num_pbs_x = self.model.size.x // self.model.parent_block_size.x
        num_pbs_y = self.model.size.y // self.model.parent_block_size.y
        
        # create an array of all the parent blocks
        pbs = [ParentBlock(
                size=self.model.parent_block_size,
                position=Position(x * self.model.parent_block_size.x, y * self.model.parent_block_size.y, self.slices * self.model.parent_block_size.z)    # noqa
               ) for y in range(num_pbs_y) for x in range(num_pbs_x)
               ]
        
        self.slices += 1
        
        num_blocks = self.model.parent_block_size.x \
            * self.model.parent_block_size.y \
            * self.model.parent_block_size.z \
            * len(pbs)
                     
        num_rows = 0
        
        while num_rows < num_blocks:
            # try to read the next row
            try:
                row = next(self.reader)
            except StopIteration:
                break
            
            if row[0][0] == '#':
                continue        # skip comment lines
                
            if len(row) < 7:    # skip over lines that are the wrong length
                continue        # TODO: Change this to an appropriate error
            
            # Work out which parent block it belongs to
            x = int(row[0])
            y = int(row[1])
            z = int(row[2])
            pb_x = x // self.model.parent_block_size.x
            pb_y = y // self.model.parent_block_size.y
            index = pb_y * num_pbs_x + pb_x
            
            try:
                parent_block = pbs[index]
            except IndexError:
                sys.exit(-1)
            
            # the position of a block is relative to the parent block
            x -= parent_block.position.x
            y -= parent_block.position.y
            z -= parent_block.position.z
            
            # create the block and add it to the parent_block
            p = Position(x, y, z)
            s = Size(int(row[3]), int(row[4]), int(row[5]))
            t = self.model.get_domain_tag(row[6])
            
            block = Block(size=s, position=p, domain=t)
            
            # need to add it to the appropriate parent block
            parent_block.append(block)
            
            num_rows += 1
        
        # add all the parent blocks to the model
        for pb in pbs:
            self.model.append(pb)
        
        # return the number of rows read
        return num_rows
                    
    def write(self):
        """
        Removes parent blocks from the model and writes them as CSV values
        to the output file. The ParentBlocks are removed from the model, so
        when the method completes the model will be empty of blocks. The order
        the blocks are written to the output will be different from the order
        they were read. However all the blocks from 1 parent block will be
        written before blocks from another parent block.
        """
        while self.model:
            pb = self.model.pop()
            for block in pb:
                # get the domain name from the tag
                domain = self.model.get_domain_name(block.domain)
            
                self.writer.writerow(
                    (block.position.x + pb.position.x,
                        block.position.y + pb.position.y,
                        block.position.z + pb.position.z,
                        block.size.x,
                        block.size.y,
                        block.size.z,
                        domain
                     ))
