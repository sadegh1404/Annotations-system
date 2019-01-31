from collections import Counter
from collections import defaultdict
class Naive_bayes:


	def __init__(self):

		self.prob = defaultdict()

	def fit(self,data):

		c = Counter([x[-1] for x in data])

		self.prob['PB'] = float(c[1])/sum(c.values())



		for a in range(len(data[0])-1):
			var = set([i[a] for i in data])
			d = Counter([x[a] for x in data])
			for i in d:
				self.prob[i] = float(d[i])/sum(d.values())
			for name in var:
				c = Counter([(x[a],x[-1]) for x in data])
				self.prob[name+'|B'] = float(sum([c[i] for i in c if i[0] == name and i[1] == 1])) / sum(c[i] for i in c if i[1] == 1)
				self.prob[name+'|Bnot'] = float(sum([c[i] for i in c if i[0] == name and i[1] == 0])) / sum(c[i] for i in c if i[1] == 0)

				d = Counter([x[a] for x in data])


	def predict(self,color,car_type,luxury):


		yeh = self.prob[color+'|B'] * self.prob[car_type+'|B'] * self.prob[luxury+'|B'] * self.prob['PB']

		nop = self.prob[color+'|Bnot'] * self.prob[car_type+'|Bnot'] * self.prob[luxury+'|Bnot'] * (1-self.prob['PB'])

		px = self.prob[color] * self.prob[car_type] * self.prob[luxury]


		if float(yeh)/px > float(nop)/px:

			return 'YES'
		else:
			return 'NO'



