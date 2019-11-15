#importing baseClass and required other thing from baseClass.py
from baseClass import FIFOCache, LRUCache, RandomCache, OracleModel, LFUCache, approxiLRU
# library for plotting graph in python
import matplotlib.pyplot as plt

#list for plotting graphs

fifoHits_loop = list()


lruHits_loop = list()


lfuHits_loop = list()

randomHits_loop = list()


OracleModelHits_loop = list()


#for cache size 1 to 100 we will see behaviour
for cachesize in range(1,101):
    cache = FIFOCache(cachesize)
    fifoHits_loop.append(cache.loopingSeq())

    cache = LRUCache(cachesize)
    lruHits_loop.append(cache.loopingSeq())

    cache = LFUCache(cachesize)
    lfuHits_loop.append(cache.loopingSeq())

    cache = RandomCache(cachesize)
    randomHits_loop.append(cache.loopingSeq())


    cache = OracleModel(cachesize)
    OracleModelHits_loop.append(cache.loopingSeq())

cachesizes = [i for i in range(1,101)]




# fraph plot for looping sequencial workload
plt.scatter(cachesizes, lruHits_loop, marker='.', color='brown', label='LRU')
plt.scatter(cachesizes, fifoHits_loop, marker ='o', color='green', label='FIFO')
plt.plot(cachesizes, lfuHits_loop, color='pink', label='LFU')
plt.plot(cachesizes, randomHits_loop, color='purple', label='Random')
plt.plot(cachesizes, OracleModelHits_loop, color='red', label='OracleModel')

plt.xlabel("Cache Size (Blocks)")
plt.ylabel("Hit Rate (%)")
plt.legend(loc='lower right')
plt.title("The Looping-sequencial Workload")

plt.show()