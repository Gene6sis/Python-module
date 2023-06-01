class Evaluator :
    
	@staticmethod
	def zip_evaluate(coefs:list, words:list) :
		if (len(coefs) != len(words)) : return -1
		return sum(len(word) * coef for word, coef in zip(words, coefs))
		
	
	@staticmethod
	def enumerate_evaluate() :
		pass

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))