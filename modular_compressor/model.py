from collections import namedtuple
from enum import IntEnum, unique
import math

Size = namedtuple('Size', ['x', 'y', 'z'])
Position = namedtuple('Position', ['x', 'y', 'z'])


@unique
class Direction(IntEnum):
    POS_X = 1
    NEG_X = 2
    POS_Y = 3
    NEG_Y = 4
    POS_Z = 5
    NEG_Z = 6


class Model:
    """
    The Model is the internal representation of the block data model. The Model
    holds the current set of ParentBlocks which constitute the current slice of
    the model. The model also holds the mappings between domains and domain
    tags, which the Blocks use.
    """

    def __init__(self):
        super(Model, self).__init__()
        self.parent_blocks = []
        self.domains = []
        self.size = None
        self.parent_block_size = None
            
    def get_domain_tag(self, domain_name):
        """Gets the integer tag that corresponds to the domain"""
        try:
            return self.domains.index(domain_name)
        except ValueError:
            # the domain is not in the list, add it
            self.domains.append(domain_name)
            return len(self.domains) - 1
        
    def get_domain_name(self, tag):
        """Gets the domain for the integer tag"""
        try:
            return self.domains[tag]
        except IndexError:
            return ""
        
    def append(self, parent_block):
        """Adds a parent block to the model"""
        self.parent_blocks.append(parent_block)
        
    def pop(self):
        """Removes and returns a parent block from the model"""
        return self.parent_blocks.pop()
    
    def __len__(self):
        """Gets the number of parent blocks remaining in the model"""
        return len(self.parent_blocks)
        
    def __bool__(self):
        """Gets the truthiness of the list of parent blocks"""
        return bool(self.parent_blocks)
        
    def __iter__(self):
        """
        Returns an iterator over the list of parent blocks.
        
        Therefore the model can be used in a for loop, e.g.
            for parent_block in model:
                # do something
        """
        return iter(self.parent_blocks)


class ParentBlock:
    """
    The ParentBlocks subdivide the model exactly with no remainder. Each Parent
    Block contains a collection of Blocks. Each Parent Block has a size and
    position. All of the Blocks that the Parent Block contain are positoned
    relative to the ParentBlock position.
    
    The ParentBlock implements the iterator protocol, so can be iterated over
    natively in for loops, e.g.
        for block in parentBlock:
            # block is of the Block type
    """
    
    def __init__(self, size, position):
        super(ParentBlock, self).__init__()
        self.size = size
        self.position = position
        self.blocks = []
    
    def append(self, block):
        """Adds a block to this parent block"""
        self.blocks.append(block)
        
    # def pop(self):
    #     return self.blocks.pop()
        
    def clear(self):
        """Clears (removes) all blocks from this parent block"""
        self.blocks.clear()
    
    # iterator protocol methods, so the ParentBlock can be used in for loops
    def __iter__(self):
        """
        Returns an iterator over the list of blocks.
        
        Therefore the model can be used in a for loop, e.g.
            for block in parent_block:
                # do something
        """
        return ParentBlockIter(self)
    
    def __len__(self):
        """
        Gets the number of blocks in the parent_block. This is not actually
        always accurate. It is only accurate after the parent block has been
        cleared and a new block added. To be truly useful this function needs
        to be updated to be more general.
        
        TODO: FIx this.
        """
        return len(self.blocks)
    
    # not sure how useful this is right now
    def __getitem__(self, coordinate):
        return self.get_block(*coordinate)
        
    def get_block(self, x, y, z):
        """
        Get the block that occupies the specified coordinates. The block may
        not start at the specified location, but it will extend to occupy the
        specified coordinate. If the coordinate is out of range of the parent-
        block None is returned.
        """
        b = self.get_block_or_position(x, y, z)
        if isinstance(b, Position):
            b = self.get_block_or_position(*b)
        return b
            
    def get_block_or_position(self, x, y, z):
        """
        Get the block that starts at the specified location or the Position of
        the block that occupies the specified location, in the event that a
        block does not start at that location. None is returned if the
        coordinate is outside of the parent-block
        """
        if x < 0 or x >= self.size.x or \
            y < 0 or y >= self.size.y or \
                z < 0 or z >= self.size.z:
            return None
                
        if len(self.blocks) == 1:
            # special case for when all the blocks are the same domain
            # all the blocks are replaced with a single block
            return self.blocks[0]
            
        return self.blocks[
            z * (self.size.x * self.size.y) + y * (self.size.x) + x]
            
    def combine_blocks(self, blocks):
        """
        Combines blocks to create a larger block. The new block will be the
        bounding box of all the blocks supplied and have the domain of the
        first block supplied. It is the user's resposibility to ensure that
        combining the blocks is valid and makes sense.
        """
        combined_block = Block.combine(blocks)
        
        for b in blocks:
            # mark all blocks with the position of the combined block
            index = b.position.z * (self.size.x * self.size.y) \
                + b.position.y * (self.size.x) \
                + b.position.x
            self.blocks[index] = combined_block.position
        
        # place the combined block at its origin
        index = combined_block.position.z * (self.size.x * self.size.y) \
            + combined_block.position.y * (self.size.x) \
            + combined_block.position.x
        
        self.blocks[index] = combined_block
            
    def get_neighbours(self, block, direction):
        """
        Get a list of all the neighbours of the block in the given Direction.
        Neighbours of a block are any blocks that touch the face of the block
        on the specified side. Only part of a block needs to touch the face
        to be counted as a neighbour.
        
        Returns a set of neighbouring blocks
        """
        # set the start and end indexes to search for blocks
        start_x = block.position.x
        end_x = block.position.x + block.size.x
        
        start_y = block.position.y
        end_y = block.position.y + block.size.y
        
        start_z = block.position.z
        end_z = block.position.z + block.size.z
        
        if direction == Direction.POS_X:
            start_x = end_x
            end_x = end_x + 1
            
        elif direction == Direction.POS_Y:
            start_y = end_y
            end_y = end_y + 1
            
        elif direction == Direction.POS_Z:
            start_z = end_z
            end_z = end_z + 1
            
        elif direction == Direction.NEG_X:
            end_x = start_x
            start_x = start_x - 1
            
        elif direction == Direction.NEG_Y:
            end_y = start_y
            start_y = start_y - 1
            
        elif direction == Direction.NEG_Z:
            end_z = start_z
            start_z = start_z - 1
        
        # iterate through the list to find the blocks
        neighbours = set()
        for z in range(start_z, end_z):
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    b = self.get_block(x, y, z)
                    if b:
                        neighbours.add(b)
        return neighbours


class ParentBlockIter:
    """
    An iterator over a ParentBlock. Objects of this class will be created
    from the __iter__() method of the ParentBlock, and do not need to be
    created explicitly.
    """
    
    def __init__(self, parentblock):
        super(ParentBlockIter, self).__init__()
        self.iter = iter(parentblock.blocks)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        # skip over everything, which isn't a block
        while (True):
            b = next(self.iter)
            if isinstance(b, Block):
                return b


class Block(namedtuple('Block', ['size', 'position', 'domain'])):
    """
    Lightweight representation of a block in the data model.
    
    A block has a size, a position relative to the start of its ParentBlock and
    a domain tag.
    
    The size is a namedtuple and the fields are labelled x, y and z. So the
    size of the block in the x direction can be accessed as `block.size.x`.
    
    The Position is similarly, a namedtuple also with the the fields x, y, z.
    These positions are relative to the start of the ParentBlock. The x
    position can be accessed as `block.poistion.x`
    
    The domain is an integer tag that represents the domain. The model contains
    a mapping between these tags and the actual domain names. This conversion
    is done to increase the speed of comparing the domains of different blocks.
    The domain tag can be accessed as `block.domain`
    """
    
    __slots__ = ()      # remove the instance dictionary
    
    @classmethod
    def combine(cls, blocks):
        """
        Returns a new block that is the combination of all of the blocks passed
        to the function. No checks are performed to ensure that this operation
        is posible. The new block will be the bounding block that has the
        smallest starting position and the largest ending position. The domain
        of the block will be the domain of the first block.
        """
        start = Position(0, 0, 0)
        end = Position(0, 0, 0)
        
        start_squared = math.inf
        end_squared = 0
        
        for block in blocks:
            s = block.position.x**2 + block.position.y**2 + block.position.z**2
            if s < start_squared:
                start_squared = s
                start = block.position
            
            e = (block.position.x + block.size.x)**2 \
                + (block.position.y + block.size.y)**2 \
                + (block.position.z + block.size.z)**2
            if e > end_squared:
                end_squared = e
                end = Position(
                    (block.position.x + block.size.x),
                    (block.position.y + block.size.y),
                    (block.position.z + block.size.z)
                )
        new_size = Size(end.x - start.x, end.y - start.y, end.z - start.z)
        return Block(size=new_size, position=start, domain=blocks[0].domain)
    
    def __add__(self, other_block):
        return Block.combine(self, other_block)
