import re
import numpy as np

file = '/sscc/home/k/kob734/hw4materials/vocab.txt'
indices = dict()
words = dict()
with open(file) as f:
	for idx, word in enumerate(f):
		indices[word.rstrip()] = idx
		words[idx] = word.rstrip()

modelProb = np.zeros((len(words)))
noiseProb = np.zeros((len(words)))

file1 = '/sscc/home/k/kob734/hw4materials/lm.txt'
with open(file1) as f1:
	for line in f1:	 
		wd = re.split(r'\t', line[:-1])[0]
		prob = re.split(r'\t', line[:-1])[1]
		index = indices[wd]
		modelProb[index] = prob
file2 = '/sscc/home/k/kob734/hw4materials/noise.txt'
with open(file2) as f2:
	for line in f2:
		wd = re.split(r'\t', line[:-1])[0]
		noise = re.split(r'\t', line[:-1])[1]
		index = indices[wd]
		noiseProb[index] = noise

unnorm_posterior = modelProb * noiseProb
posterior = unnorm_posterior / np.sum(unnorm_posterior)

max_idx = np.argmax(posterior)
lst = np.where(posterior > 0.05)
for item in lst[0]:
	print words[item]
	print posterior[item]
