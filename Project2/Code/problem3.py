#This is just a comment!
import numpy as np
trans = np.array([(0.0, 0.8, 0.2, 0.0, 0.0),
				  (0.0, 0.3, 0.0, 0.5, 0.2),
				  (0.0, 0.8, 0.2, 0.0, 0.0),
				  (0.0, 0.6, 0.2, 0.0, 0.2), 
				  (0.0, 0.0, 0.0, 0.0, 0.0)])

emiss = np.array([(0.2, 0.4, 0.4),
				  (1.0, 0.0, 0.0),
				  (0.0, 0.5, 0.5)])

tagsTrans = ['<s>', 'N', 'A', 'V', '</s>']
words =['young', 'man', 'wall']
tagsEmiss = ['N', 'A', 'V']

nodeStructure = ['<s>', ['N1', 'A1', 'V1'], ['N2', 'A2', 'V2'], ['N3', 'A3', 'V3'], '</s>']
for idx, node in enumerate(nodeStructure):
	if node != '<s>':
		if node != '</s>':
			for i, nd in enumerate(node):
				print emiss[words[idx]][tagsEmiss.index(nd[:-1])] * trans[tagsTrans.index(nd[:-1])][]
				
		

