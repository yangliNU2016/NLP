import nltk
import re
import numpy as np

# Map the word types to their indices generated by the order of occurance in file
file1 = nltk.data.path[0] + '/corpora/brown/brown_vocab_100.txt'
words = dict()
with open(file1) as f:
	for index, line in enumerate(f):
		words[line.rstrip()] = index
		
# Initialize a counter that counts how many each of the words 	
counts = np.zeros((len(words), len(words)))

file2 = nltk.data.path[0] + '/corpora/brown/brown_100.txt'
with open(file2) as g:
#	starting_word = '<s>'
	for line in g:
		wdsEachLine = line[:-1].lower().split()
#		wdsEachLine = [starting_word] + wdsEachLine
		wdsEachLine.append('</s>')
		for idx, wd in enumerate(wdsEachLine):
			if idx != 0:
				counts[words[wdsEachLine[idx]]][words[wdsEachLine[idx - 1]]] += 1

counts += 0.1
from sklearn.preprocessing import normalize
probs = normalize(counts, norm='l1', axis=0)
						
# Write them into a file
target = open('smooth_probs.txt', 'w')
target.write('p(the|all) = ' + str(probs[words['the']][words['all']]) + '\n')
target.write('p(jury|the) = ' + str(probs[words['jury']][words['the']]) + '\n')
target.write('p(campaign|the) = ' + str(probs[words['campaign']][words['the']]) + '\n')
target.write('p(calls|anonymous) = ' + str(probs[words['calls']][words['anonymous']]) + '\n')
target.close()

file3 = nltk.data.path[0] + '/corpora/brown/toy_corpus.txt'
target1 = open('smoothed_eval.txt', 'w')
with open(file3) as h:
	for line in h:
		wdsInSentence = line[:-1].lower().split()
#		wdsInSentence = ['<s>'] + wdsInSentence
		wdsInSentence.append('</s>')
		sentProb = 1
		for i, wd in enumerate(wdsInSentence):
#			if wd != '<s>':
			if i != 0:
				sentProb *= probs[words[wd]][words[wdsInSentence[i - 1]]]
		perplexity = 1 / (pow(sentProb, 1.0 / len(wdsInSentence)))
		target1.write(str(perplexity) + '\n')
	target1.close()	