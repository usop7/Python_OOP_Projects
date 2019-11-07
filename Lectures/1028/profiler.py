import cProfile
import re
import pstats

cProfile.run('re.compile("foo|bar")', 'restats', sort=pstats.SortKey.CALLS)
p = pstats.Stats('restats')
p.strip_dirs().print_stats()