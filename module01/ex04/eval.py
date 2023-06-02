class Evaluator :
    
    @staticmethod
    def zip_evaluate(coefs:list, words:list) :
        if (len(coefs) != len(words)) : return -1
        return sum(len(word) * coef for word, coef in zip(words, coefs))
        
    
    @staticmethod
    def enumerate_evaluate(coefs:list, words:list) :
        if (len(coefs) != len(words)) : return -1
        return sum(len(word) * coefs[index] for index, word in enumerate(words))
