import re
import nltk

target = open("browncaps.txt", 'w')
brown_filename = nltk.data.path[0] + "/corpora/brown/brown_all.txt"
with open(brown_filename) as f:
	for line in f:
		match = re.search(r'\b[A-Z][a-z]* [a-z]* [A-Z][a-z]* [a-z]* [A-Z][a-z]*\b', line)
		if match is not None:
			target.write(match.group() + '\n')
target.close()
			
