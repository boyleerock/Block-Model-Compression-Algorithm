# Modular Compressor

This compression system uses a modular architecture and uses some layers of
abstraction to simplify the development or compression algorithms.

## The Parser
This module is responsible for reading and writing the data in CSV format.
It will read 1 parent block high slice at a time. It then creates Block objects
for each line on the input. These Blocks are then collected in to ParentBlocks.
The position of the Blocks is relative to the start of the ParentBlock. This
allows the same code to handle the blocks no matter where in the model they are
actually located. These Parent Blocks are then added to the Model, which holds
the collection of ParentBlocks.

## Model
This module contains all the classes that represent the types of data in the
model. The Model and ParentBlock can be viewed as container classes, and
several Python protocol are implemented on them to allow for easy iteration over
their data, as well as adding and removing data.

### Block
This represents a single block in the model. It has a Size, Position, and
domain. Block, Size, and Position are all types of `namedtuple`, which means
they are lightweight objects without instance dictionaries taking up no more
space than simple `tuples`.

## Compression Engine
This module is responsible for deciding which algorithm gets applied to which
ParentBlocks. It applies these algorithms to the ParentBlocks in parallel using
multiprocessing.

### compressors
The compressors package (directory) holds all the different compressors, which
implement different compression algorithms. Each one should be a subclass
of `Compressor`. The Compressors need only implement a single method, `compress`
which is passed the ParentBlock to compress. The Compressors are also able
to be created with a set of parameters, which can be used to modify the
behaviour of the system.

To add a new compression algorithm:
- Create a new module (file) in the compressors package (folder)
- Implement the subclass of Compressor in that file
- In the compressionEngine module:
  - import the new compressor
  - instantiate it, optionally with any parameters it needs
  - call its `compress` method at the appropriate place in the 
    compress_parent_block() function.