kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
    for key, value in kata.items() :
        print(f"{key} was created by {value}")