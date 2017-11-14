import nltk
import re
import numpy as np

file1 = nltk.data.path[0] + '/corpora/brown/brown_words_hw3.txt'
words = dict()
with open(file1) as f1:
	for index, line in enumerate(f1):
		words[line.rstrip()] = index

file2 = nltk.data.path[0] + '/corpora/brown/brown_tags_hw3.txt'
tags = dict()
with open(file2) as f2:
	for index, line in enumerate(f2):
		tags[line.rstrip()] = index

trans = np.zeros((len(tags), len(tags)))
emiss = np.zeros((len(tags), len(words)))

file3 = nltk.data.path[0] + '/corpora/brown/brown_100_pos.txt'
with open(file3) as f3:
	for line in f3:
		wdsEachLine = line[:-1].lower().split()
		wdsEachLine.append('<end>')
		for idx, wd in enumerate(wdsEachLine):
			wdsEachLine[idx] = wd.split('/')
		for idx, wd in enumerate(wdsEachLine):
			if idx != len(wdsEachLine) - 1:
				emiss[tags[wd[1]]][words[wd[0]]] += 1
			if idx != 0:
				prevIdx = idx - 1
				if idx != len(wdsEachLine) - 1:
					trans[tags[wdsEachLine[prevIdx][1]]][tags[wd[1]]] += 1
				else:
					trans[tags[wdsEachLine[prevIdx][1]]][tags[wd[0]]] += 1
from sklearn.preprocessing import normalize
emissN = normalize(emiss, norm='l1', axis=1)
transN = normalize(trans, norm='l1', axis=1)

target1 = open('emission.txt', 'w')
target1.write('p(weekend|nn) = ' + str(emissN[tags['nn']][words['weekend']]) + '\n')
target1.write('p(texas|np) = ' + str(emissN[tags['np']][words['texas']]) + '\n') 
target1.write('p(to|to) = ' + str(emissN[tags['to']][words['to']]) + '\n') 
target1.write('p(old|jj) = ' + str(emissN[tags['jj']][words['old']]) + '\n')  
target1.close()

target2 = open('transition.txt', 'w')
target2.write('p(nn|nn) = ' + str(transN[tags['nn']][tags['nn']]) + '\n')
target2.write('p(.|nn) = ' + str(transN[tags['nn']][tags['.']]) + '\n') 
target2.write('p(<end>|.) = ' + str(transN[tags['.']][tags['<end>']]) + '\n') 
target2.write('p(vb|to) = ' + str(transN[tags['to']][tags['vb']]) + '\n') 
target2.close()

file4 = nltk.data.path[0] + '/corpora/brown/toy_pos_corpus.txt'
target3 = open('pos_eval.txt', 'w')
with open(file4) as f4:
	for line in f4:
		wdsInSentence = line[:-1].lower().split()
		wdsInSentence.append('<end>')
		for idx, wd in enumerate(wdsInSentence):
			wdsInSentence[idx] = wd.split('/')
		sentProb = 1
		for i, wd in enumerate(wdsInSentence):
			if i != len(wdsInSentence) - 1:
				sentProb *= emissN[tags[wd[1]]][words[wd[0]]]
			if i != 0:
				prevIdx = i - 1
				if i != len(wdsInSentence) - 1:
					sentProb *= transN[tags[wdsInSentence[prevIdx][1]]][tags[wd[1]]] 
				else:
					sentProb *= transN[tags[wdsInSentence[prevIdx][1]]][tags[wd[0]]] 
		target3.write(str(sentProb) + '\n')
target3.close()		
	