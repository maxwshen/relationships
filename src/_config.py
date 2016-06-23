PRJ_DIR = '/cluster/mshen/self/relationships/'  
SRC_DIR = PRJ_DIR + 'src/'

# toy = True
toy = False
if toy:
  PRJ_DIR += 'toy/'
#######################################################
# Note: Directories should end in / always
#######################################################
DATA_DIR = PRJ_DIR + 'data/'
OUT_PLACE = PRJ_DIR + 'out/'
RESULTS_PLACE = PRJ_DIR + 'results/'
#######################################################
#######################################################

CLEAN = False       # Values = 'ask', True, False

#######################################################
# Project-specific parameters
#######################################################

NOUN_FN = DATA_DIR + 'quintans/noun4k.txt'
VERB_FN = DATA_DIR + 'wordnet3.1/unique.conv.data.verb'