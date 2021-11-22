from compressors.compressor import Compressor
from model import Block, Position, Dimension


# WARNING: THIS COMPRESSOR IS INCOMPLETE, DO NOT USE YET


class RunLength(Compressor):
    """
    A Compressor which works along a single dimension and to combine all the
    blocks of the same domain into 1 block. It will only work in a single
    dimension.
    """

    def __init__(self, **parameters):
        """
        Creates a new compressor to compress the block data. Compressors take
        a set of parameters, which are unique to each compressor. This
        compressor takes the parameter "dimension", which has one of the values:
        "x", "y", "z"
        """
        super(SameDomain, self).__init__()
        self.parameters = parameters
        if 'dimension' not in self.parementers:
            self.parameters['dimension'] = 'x'

    def _run_length_compress(self, parent_block, block):
        if self.parameters['dimension'] is 'y':
            neighbours = parent_block.get_neighbours(block, Direction.POS_Y)
            skip_i = 1
        elif self.parameters['dimension'] is 'z':
            neighbours = parent_block.get_neighbours(block, Direction.POS_Z)
            skip_i = 2
        else:
            neighbours = parent_block.get_neighbours(block, Direction.POS_X)
            skip_i = 3
        
        # check if we can merge all the neighbours
        for n in neighbours:
            if n.domain != block.domain:
                # all the domains don't match
                neighbours.clear()
                break
            else:
                for i in range(3):
                    if i == skip_i:
                        continue
                    if n.position[i] < block.position[i]
                        or (n.position[i] + n.size[i]) > (block.position[i] + block.size[i]):  # noqa
                            # a neighbour starts of ends past the edge of this
                            # block
                            neighbours.clear()
                            
        if len(neighbours) > 0:
            parent_block.combine_blocks(block, *neighbours)
            return True
        else:
            return False
                        
    def compress(self, parent_block):
        """
        Executes the compression algorithm on the specified parent block.
        
        Returns the compressed parent block
        """
        for block in parent_block:
            while True:
                if not self._run_length_compress(block):
                    break
        return parent_block
