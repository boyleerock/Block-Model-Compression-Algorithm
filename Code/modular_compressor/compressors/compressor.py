class Compressor:
    """
    A Basic Compressor that does nothing, but provides a base class for other
    compressors
    """

    def __init__(self, **parameters):
        """
        Creates a new compressor to compress the block data. Compressors take
        a set of parameters, which are unique to each compressor. This
        compressor doesn't take any parameters, because it does nothing.
        """
        super(Compressor, self).__init__()
        self.parameters = parameters

    def compress(self, parent_block):
        """
        Executes the compression algorithm on the specified parent block.
        Subclasses need to extend this function to do the compression. The
        function should take in a parent block, compress it and return the
        compressed parent block.
        
        This base class does not provide any compression.
        """
        pass
