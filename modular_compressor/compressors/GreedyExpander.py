from compressors.compressor import Compressor
from model import Direction


class GreedyExpander(Compressor):
    """
    The compressor looks at the neighbouring blocks in the x, y, z directions.
    For each set of neighbours, it is determined if all the neighbours in the
    set share the domain with the origin block. The set with the most
    neighbours, which shares the domain with the origin block are merged into a
    new block. This continues until no more blocks can be merged. The origin
    block is then moved to the next block in the ParentBlock
    """

    def __init__(self, **parameters):
        super(GreedyExpander, self).__init__()
        self.parameters = parameters
        
    def _suck_in_the_blocks(self, parent_block, block):
        """
        Merges the largest neighbouring set that also matches the domain of the
        block.
        
        Returns True if a merge occurred, otherwise False
        """
        neighbours = [
            parent_block.get_neighbours(block, Direction.POS_X),
            parent_block.get_neighbours(block, Direction.POS_Y),
            parent_block.get_neighbours(block, Direction.POS_Z)
        ]
        
        for i in range(3):
            neighbour = list(neighbours[i])
            for n in neighbour:
                # all the domains don't match
                if n.domain != block.domain:
                    neighbours[i].clear()
                    break
                else:
                    for j in range(3):
                        if i == j:
                            continue
                        if n.position[j] < block.position[j] \
                            or (n.position[j] + n.size[j]) > (block.position[j] + block.size[j]):   # noqa
                            # a neighbour starts of ends past the edge of this
                            # block
                            neighbours[i].clear()
                            break
                            
        # find the direction with the most neighbours
        max_neighbours = ()
        for n in neighbours:
            if len(n) > len(max_neighbours):
                max_neighbours = n
        
        if len(max_neighbours) == 0:
            return False
        else:
            max_neighbours.add(block)
            parent_block.combine_blocks(list(max_neighbours))
            return True
    
    def compress(self, parent_block):
        """
        Executes the compression algorithm on the specified parent block.
        See the class description for information on how the compressor operates
        
        Returns the compressed parent block
        """
        for block in parent_block:
            while True:
                if not self._suck_in_the_blocks(
                    parent_block,
                    parent_block.get_block(*block.position)
                ):
                    break
        return parent_block
