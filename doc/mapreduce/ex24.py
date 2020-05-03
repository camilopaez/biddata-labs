from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')  
        yield idemp, int(salary)
       
    def reducer(self, key, values):
        salary = 0
        quantity = 0
        for v in values:
            salary+=v
            quantity+=1
        yield key, salary/quantity

if __name__ == '__main__':
    MRWordFrequencyCount.run()