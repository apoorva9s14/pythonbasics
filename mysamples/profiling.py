'''to get profiling details for any function'''

import profile

from concurrent_futures import mytestfn
profile.run('print(mytestfn())')