import sys, os, datetime

import _config, _clean

from mylib import util

# Import all your steps
import a_worddb, b_generate

##############################################################
##############################################################
util.cp(_config.SRC_DIR + '_config.py', _config.RESULTS_PLACE)

start = datetime.datetime.now()
print start
##############################################################
##############################################################

a_res_dir = a_worddb.main([_config.NOUN_FN, _config.VERB_FN], 
  _config.OUT_PLACE + 'a_worddb/', 
  run = True)

b_res_dir = b_generate.main(a_res_dir, 
  _config.OUT_PLACE + 'b_generate/',
  run = True)


##############################################################
##############################################################


print '\n\nDone.\n'
end = datetime.datetime.now()
print end, '\nTotal Time:', end - start

# _clean.main()