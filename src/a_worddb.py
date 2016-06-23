# From a corpus of words, extract relevant sections

import _config
import sys, os, fnmatch, datetime, subprocess
import nltk, pattern.en

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
from pattern.en import conjugate

from mylib import util


# Default params
# DEFAULT_INP_DIR = _config.DATA_DIR + 'google10k/google-10000-english-usa.txt'
DEFAULT_INP_DIR = [_config.NOUN_FN, _config.VERB_FN] 
NAME = util.get_fn(__file__)

# Functions

def pluralize(word):
  lemma = wnl.lemmatize(word, 'n')
  plural = True if word is not lemma else False
  if not plural:
    out = pattern.en.pluralize(word)
  else:
    out = word
  return out

def make_nouns(inp_fn, out_dir):
  nouns = set()
  with open(inp_fn) as f:
    for i, line in enumerate(f):
      nouns.add(pluralize(line.strip()))
  print '\tFound', len(nouns), 'nouns'

  out_fn = out_dir + '/nouns.txt'
  with open(out_fn, 'w') as f:
    for n in nouns:
      f.write(n + '\n')
  return

def make_verbs(inp_fn, out_dir):
  verbs = set()
  with open(inp_fn) as f:
    for i, line in enumerate(f):
      verbs.add(conjugate(line.strip(), 'p'))
  print '\tFound', len(verbs), 'verbs'

  out_fn = out_dir + '/verbs.txt'
  with open(out_fn, 'w') as f:
    for n in verbs:
      f.write(n + '\n')
  return


def make_db(inp_fn, out_dir):
  noun_fn, verb_fn = inp_fn[0], inp_fn[1]
  
  make_nouns(noun_fn, out_dir)
  make_verbs(verb_fn, out_dir)
  return


@util.time_dec
def main(inp_dir, out_dir, run = True):
  print NAME  
  util.ensure_dir_exists(out_dir)
  if not run:
    print '\tskipped'
    return out_dir

  # Function calls

  inp_fn = DEFAULT_INP_DIR
  make_db(inp_fn, out_dir)

  return out_dir


if __name__ == '__main__':
  main(DEFAULT_INP_DIR, _config.OUT_PLACE + NAME + '/')