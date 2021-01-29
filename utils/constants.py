"""
    Contains constants shared across the project.

"""

import os
import enum
from torch.utils.tensorboard import SummaryWriter


# Supported datasets - currently only Cora
class DatasetType(enum.Enum):
    CORA = 0


# Networkx is not precisely made with drawing as it's main feature but I experimented with it a bit
class GraphVisualizationTool(enum.Enum):
    NETWORKX = 0,
    IGRAPH = 1


# Support for 3 different GAT implementations - we'll profile each one of these in playground.py
class LayerType(enum.Enum):
    IMP1 = 0,
    IMP2 = 1,
    IMP3 = 2


# 3 different model training/eval phases used in train.py
class LoopPhase(enum.Enum):
    TRAIN = 0,
    VAL = 1,
    TEST = 2


writer = SummaryWriter()  # (tensorboard) writer will output to ./runs/ directory by default


# Global vars used for early stopping. After some number of epochs (as defined by the patience_period var) without any
# improvement on the validation dataset (measured via accuracy metric), we'll break out from the training loop.
BEST_VAL_ACC = 0
PATIENCE_CNT = 0


BINARIES_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'binaries')
CHECKPOINTS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'checkpoints')
DATA_DIR_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
CORA_PATH = os.path.join(DATA_DIR_PATH, 'cora')  # this is checked-in no need to make a directory

# Make sure these exist as the rest of the code assumes it
os.makedirs(BINARIES_PATH, exist_ok=True)
os.makedirs(CHECKPOINTS_PATH, exist_ok=True)

#
# Cora specific information
#

# Thomas Kipf et al. first used this split in GCN paper and later Petar Veličković et al. in GAT paper
CORA_TRAIN_RANGE = [0, 140]
CORA_VAL_RANGE = [140, 140+500]
CORA_TEST_RANGE = [1708, 1708+1000]
CORA_NUM_INPUT_FEATURES = 1433
CORA_NUM_CLASSES = 7

network_repository_cora_url = r'http://networkrepository.com/graphvis.php?d=./data/gsm50/labeled/cora.edges'

# Used whenever we need to plot points from different class (like t-SNE in playground.py and CORA visualization)
cora_label_to_color_map = {0: "red", 1: "blue", 2: "green", 3: "orange", 4: "yellow", 5: "pink", 6: "gray"}



