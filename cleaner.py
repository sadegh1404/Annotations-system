
import nltk 
class Preproccess:


	def __inint__(sef):
		print('hi')
		stop_words = ''


	def get_stop_words(self):

		with open('/home/sadegh/Annotations-system/stop_words.txt','r') as f:
			content = f.read()


		stop_words = list(unicode(content,'utf-8').split('\n'))
  		return stop_words



