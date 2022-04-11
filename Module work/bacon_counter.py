from mrjob.job import MRJob

class Bacon_count(MRJob):
	def mapper(self, _, line):
		for word in line.split():
			if word.lower()=="bacon":
				yield "bacon", 1

	def reducer(self, key, values):
		yield key, sum(values)
if __name__=="__main__":
	Bacon_count.run

# task1=Bacon_count(args=[2])
# with open ('input.txt', 'r') as fi:
# # 	# row = [(i,line.strip()) for i,line in enumerate(fi)]	
# output= list(task1)
