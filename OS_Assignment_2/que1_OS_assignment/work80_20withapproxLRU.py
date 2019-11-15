#importing baseClass and required other thing from baseClass.py
from baseClass import FIFOCache, LRUCache, RandomCache, OracleModel, LFUCache, approxiLRU
# library for plotting graph in python
import matplotlib.pyplot as plt

fifoHits_8020 = list()

lruHits_8020 = list()

lfuHits_8020 = list()

randomHits_8020 = list()

OracleModelHits_8020 = list()

approxlruHits_8020 = list()


#for cache size 1 to 100 we will see behaviour
for cachesize in range(1,101):
    cache = FIFOCache(cachesize)
    fifoHits_8020.append(cache.workload_80_20())
    
    cache = LRUCache(cachesize)
    lruHits_8020.append(cache.workload_80_20())
    

    
    cache = LFUCache(cachesize)
    lfuHits_8020.append(cache.workload_80_20())
    

    
    cache = RandomCache(cachesize)
    randomHits_8020.append(cache.workload_80_20())

    cache = approxiLRU(cachesize)
    approxlruHits_8020.append(cache.workload_80_20())


    cache = OracleModel(cachesize)
    OracleModelHits_8020.append(cache.workload_80_20())
    

cachesizes = [i for i in range(1,101)]

# plot 80-20 workload including approx LRU
plt.scatter(cachesizes, lruHits_8020, marker='x', color='aqua', label='LRU')
plt.scatter(cachesizes, approxlruHits_8020, marker='.', color='black', label='Approx LRU')
plt.scatter(cachesizes, fifoHits_8020, marker ='.', color='black', label='FIFO')
plt.plot(cachesizes, lfuHits_8020, color='yellow', label='LFU')
plt.plot(cachesizes, randomHits_8020, color='purple', label='Random')
plt.plot(cachesizes, OracleModelHits_8020, color='orange', label='OracleModel')

plt.xlabel("Cache Size (Blocks)")
plt.ylabel("Hit Rate (%)")
plt.legend(loc='lower right')
plt.title("The 80-20 Workload with approx LRU")

plt.show()