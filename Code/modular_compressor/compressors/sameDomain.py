from compressors.compressor import Compressor
from model import Block, Position


class SameDomain(Compressor):
    """
    A Compressor which replaces all the blocks within a parent block with a
    single block if all the domains of the blocks are the same.
    """

    def __init__(self, **parameters):
        """
        Creates a new compressor to compress the block data. Compressors take
        a set of parameters, which are unique to each compressor. This
        compressor doesn't take any parameters.
        """
        super(SameDomain, self).__init__()
        self.parameters = parameters

    def compress(self, parent_block):
        """
        Executes the compression algorithm on the specified parent block.
        
        This compressor sees if all the blocks in the parent block belong to
        the same domain. If they do, it replaces all the blocks with one
        new block the size of the parent block
        
        Returns the compressed parent block
        """
        domain = parent_block.get_block(0, 0, 0).domain
        for block in parent_block:
            if block.domain != domain:
                # not all the domains are the same, get out of here quick!
                return parent_block
        
        # if we get here, there is only one domain
        new_block = Block(
            size=parent_block.size,
            position=Position(0, 0, 0),
            domain=domain
        )
        
        parent_block.clear()
        parent_block.append(new_block)
        
        return parent_block
