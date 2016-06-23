# Generate a combination of phrases

import _config
import sys, os, fnmatch, datetime, subprocess, random
import numpy as np

from mylib import util


# Default params
DEFAULT_INP_DIR = _config.OUT_PLACE + 'a_worddb/'
NAME = util.get_fn(__file__)

# Functions

def read_words(inp_fn):
  with open(inp_fn) as f:
    lns = f.readlines()
  return [s.strip() for s in lns]

def generate(inp_dir, out_dir):
  nouns = read_words(inp_dir + 'nouns.txt')
  verbs = read_words(inp_dir + 'verbs.txt')

  for i in range(10):
    print '\t', random.choice(nouns), random.choice(verbs)
  return

@util.time_dec
def main(inp_dir, out_dir, run = True):
  print NAME  
  util.ensure_dir_exists(out_dir)
  if not run:
    print '\tskipped'
    return out_dir

  # Function calls
  generate(inp_dir, out_dir)
  return out_dir


if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1], sys.argv[2])
  else:
    main(DEFAULT_INP_DIR, _config.OUT_PLACE + NAME + '/')
