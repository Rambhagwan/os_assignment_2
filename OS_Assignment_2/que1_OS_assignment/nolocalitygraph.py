#importing baseClass and required other thing from baseClass.py
from baseClass import FIFOCache, LRUCache, RandomCache, OracleModel, LFUCache, approxiLRU
# library for plotting graph in python
import matplotlib.pyplot as plt



fifoHits_NL = list()
lruHits_NL = list()
lfuHits_NL = list()
randomHits_NL = list()
OracleModelHits_NL = list()


#for cache size 1 to 100 we will see behaviour
for cachesize in range(1,101):
    cache = FIFOCache(cachesize)
    fifoHits_NL.append(cache.no_locality())

    cache = LRUCache(cachesize)
    lruHits_NL.append(cache.no_locality())

    cache = LFUCache(cachesize)
    lfuHits_NL.append(cache.no_locality())

    cache = RandomCache(cachesize)
    randomHits_NL.append(cache.no_locality())

    cache = OracleModel(cachesize)
    OracleModelHits_NL.append(cache.no_locality())

cachesizes = [i for i in range(1,101)]


# graph plot for no locality workload
plt.scatter(cachesizes, lruHits_NL, marker='x', color='brown', label='LRU')
plt.scatter(cachesizes, fifoHits_NL, marker ='o', color='purple', label='FIFO')
plt.plot(cachesizes, lfuHits_NL, color='blue', label='LFU')
plt.plot(cachesizes, randomHits_NL, color='red', label='Random')
plt.plot(cachesizes, OracleModelHits_NL, color='orange', label='OracleModel')

plt.xlabel("Cache Size (in Blocks)")
plt.ylabel("hit rate (in %)")
plt.legend(loc='lower right')
plt.title("No_Locality Workload")

plt.show()