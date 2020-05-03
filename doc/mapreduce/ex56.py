from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')  
        yield idemp, sececon
       
    def reducer(self, key, values):
        quantity = 0
        for v in values:
            quantity+=1
        yield key, quantity

if __name__ == '__main__':
    MRWordFrequencyCount.run()