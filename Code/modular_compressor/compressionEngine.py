from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from compressors import sameDomain
from compressors import GreedyExpander

"""
The module which is responsible for compressing the model. Which compression
algorithms to run on which parent_blocks are decided by this module. The
function compress_parent_block() decides which algorithms to use to compress
a given parent block. The run() function is called to execute the compression
of the parent blocks across multiple processors.
"""


# Create all the different types of compressors
same_domain_compressor = sameDomain.SameDomain()
greedy_expander = GreedyExpander.GreedyExpander()

try:
    num_cpus = multiprocessing.cpu_count()
except NotImplementedError:
    num_cpus = 4


def compress_parent_block(parentblock):
    """
    Decides which compression algorithms to run on which parent blocks.
    The algorithms used can vary between parent blocks, so some heuristic should
    be put in place to decide which algorithms to use.
    
    Returns the newly compressed parent block
    """
    pb = same_domain_compressor.compress(parentblock)
    
    if len(pb) > 2:
        pb = greedy_expander.compress(pb)
    
    return pb


def run(model):
    """
    Run the appropriate compressors on the model using multiprocessing
    """
    chunk_size = (len(model) + 1) // num_cpus
    new_parents = []
    with ProcessPoolExecutor(max_workers=num_cpus) as executor:
        new_parents.extend(
            executor.map(
                compress_parent_block, model.parent_blocks, chunksize=chunk_size
            )
        )
        model.parent_blocks = new_parents
