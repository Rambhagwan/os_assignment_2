
import random
# Base Simulator for every cache policy
class baseClass():
    # availableInCache is list for available things in cache 
    # SizeOfCache is total size a cache can have
    def __init__(self, cachesize):
        self.size = cachesize
        self.cacheList = list()
        super().__init__()
    
    # find_page_in_cache is called whenever a page is accessed in cache
    def find_page_in_cache(self):
        pass
    
    # page is not in cache then take it from memory
    def find_page_from_memory(self):
        pass

    #for calculating hit rate
    def find_hit_rate(self, sequence):
        numberOfHits = 0
        length_sequence = len(sequence)
        t = 0  # t is used for iterating over the sequence
        while t!=length_sequence:
            var = sequence[t]
            numberOfHits += self.find_page_in_cache(var)
            t+=1
        length_sequence = len(sequence)
        return (numberOfHits*100) / length_sequence

    # pure random no locality is there
    def no_locality(self):
        sequence = [random.randint(0,99) for i in range(10000)]
        return self.find_hit_rate(sequence)
    
    # looping sequence after ever 50 terms of sequence
    def loopingSeq(self):
        sequence = list()
        for i in range(10000):
            sequence.append(i%50)
        return self.find_hit_rate(sequence)
    
    # most of the time os deals with same amount of data 80% of the time
    def workload_80_20(self):
        sequence = [random.randint(0,19) for i in range(8000)] #80% of time
        sequence_20 = [random.randint(20,99) for i in range(2000)] #20% of time
        sequence.extend(sequence_20)  #full sequence
        random.shuffle(sequence)  #shuffling it more randomization
        return self.find_hit_rate(sequence)


# Inheriting baseClass in FIFOCache
class FIFOCache(baseClass):  #baseclass in the brackets shows inheritence
    def __init__(self, cachesize):
        super(FIFOCache, self).__init__(cachesize)
    
    def find_page_from_memory(self, page_number):
        if(len(self.cacheList)>=self.size):
            self.cacheList.pop(0)
            self.cacheList.append(page_number)
        else:  #untill cache is not full
            self.cacheList.append(page_number)
    
    def find_page_in_cache(self, page_number):
        if(page_number in self.cacheList):
            return 1
        
        self.find_page_from_memory(page_number) #put page in cache according to policy
        return 0


# Inherit the baseClass for LRU policy
class LRUCache(baseClass):
    def __init__(self, cachesize):
        super(LRUCache, self).__init__(cachesize)
    
    # 0th index is least recently used and size-1 is most recently used
    def find_page_from_memory(self, page_number):
        if(len(self.cacheList)>=self.size): #exceeding the maximum cache size
            self.cacheList.pop(0)      #removing least used page
            self.cacheList.append(page_number)   #appending the page to most recent used page
        else:
            self.cacheList.append(page_number)    ##appending the page to most recent used page
    
    def find_page_in_cache(self, page_number):
        if(page_number in self.cacheList):
            self.cacheList.pop(self.cacheList.index(page_number))
            self.cacheList.append(page_number)
            return 1
        
        self.find_page_from_memory(page_number) #put page in cache according to policy
        return 0


# Inheriting baseClass in LFUCache
class LFUCache(baseClass):
    def __init__(self, cachesize):
        self.frequenct_table = {i:0 for i in range(100)}
        super(LFUCache, self).__init__(cachesize)

    def find_page_from_memory(self, page_number):
        if(len(self.cacheList)>=self.size):
            lfupageaddress = 0
            lfupagefreq = self.frequenct_table[self.cacheList[0]]
            for i in range(1,self.size):
                if(self.frequenct_table[self.cacheList[i]]<lfupagefreq):
                    lfupageaddress = i
                    lfupagefreq = self.frequenct_table[self.cacheList[i]]
            self.cacheList.pop(lfupageaddress)
            self.cacheList.append(page_number)
            self.frequenct_table[page_number]+=1
        else:
            self.cacheList.append(page_number)
            self.frequenct_table[page_number]+=1
    
    def find_page_in_cache(self, page_number):
        if(page_number in self.cacheList):
            self.frequenct_table[page_number]+=1
            return 1
        
        self.find_page_from_memory(page_number)  #put page in cache according to policy
        return 0


# Inheriting baseClass in RandaomCache
class RandomCache(baseClass):
    def __init__(self, cachesize):
        super(RandomCache, self).__init__(cachesize)
    
    def find_page_from_memory(self, page_number):
        if(len(self.cacheList)>=self.size):
            page_to_remove = random.randint(0,self.size-1)  #randomly removing the page
            self.cacheList.pop(page_to_remove)
            self.cacheList.append(page_number)
        else:
            self.cacheList.append(page_number)
    
    def find_page_in_cache(self, page_number):
        if(page_number in self.cacheList):
            return 1
        
        self.find_page_from_memory(page_number)   #put page in cache according to policy
        return 0


class approxiLRU(baseClass):
    def __init__(self, cachesize):
        super(approxiLRU,self).__init__(cachesize)
        self.usebits = {i:0 for i in range(100)}
        self.clockhand = 0
    
    def find_page_from_memory(self, page_number):
        if((len(self.cacheList))>=self.size):
            while(self.usebits[self.cacheList[self.clockhand]]==1):
                self.usebits[self.cacheList[self.clockhand]] = 0
                self.clockhand = (self.clockhand+1)%self.size
            self.cacheList.pop(self.clockhand)
            self.cacheList.append(page_number)
            self.usebits[page_number] = 1
        else:
            self.cacheList.append(page_number)
            self.usebits[page_number] = 1
    
    def find_page_in_cache(self, page_number):
        if(page_number in self.cacheList):
            self.usebits[page_number] = 1
            return 1

        self.find_page_from_memory(page_number)  #put page in cache according to policy
        return 0        



# Inheriting baseClass in OracleModel
class OracleModel(baseClass):
    def __init__(self, cachesize):
        super(OracleModel,self).__init__(cachesize)
        self.sequence = list()
    
    def find_page_from_memory(self, page_number, currentaccessindex):
        if(len(self.cacheList)>=self.size):
            farthestpageaddress = -1
            farthestpagedistance = 0
            for i in range(self.size):
                try:
                    k = self.sequence.index(self.cacheList[i], currentaccessindex)
                    if((k-currentaccessindex) > farthestpagedistance):
                        farthestpageaddress = i
                        farthestpagedistance = k-currentaccessindex
                except ValueError:
                    farthestpageaddress = i
                    break
            self.cacheList.pop(farthestpageaddress)
            self.cacheList.append(page_number)
        else:
            self.cacheList.append(page_number)
    
    def find_page_in_cache(self, page_number, currentaccessindex):
        if(page_number in self.cacheList):
            return 1
        
        self.find_page_from_memory(page_number, currentaccessindex)
        return 0
    
    def find_hit_rate(self, sequence):
        self.sequence = sequence
        numberOfHits = 0
        length_sequence = len(sequence)
        for i in range(len(self.sequence)):
            numberOfHits += self.find_page_in_cache(self.sequence[i], i)
        return (numberOfHits*100)/length_sequence
