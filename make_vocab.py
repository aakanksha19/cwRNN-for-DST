import sys
import os
import pickle
from nltk import word_tokenize
from nltk.util import ngrams

input_folder = sys.argv[1]
vocab = {}
word_id = 0
for file in os.listdir(input_folder):
	input = open(os.path.join(input_folder,file),'r')
	print file
	for line in input:
		if line.startswith("turn "):
			continue
		tokens = word_tokenize(line.split('\t')[0])
		bigrams = ngrams(tokens,2)
		trigrams = ngrams(tokens,3)
		for word in tokens:
			if word in vocab:
				continue
			else:
				vocab[word] = word_id
				word_id += 1
		for word in bigrams:
			if word in vocab:
				continue
			else:
				vocab[word] = word_id
				word_id += 1
		for word in trigrams:
			if word in vocab:
				continue
			else:
				vocab[word] = word_id
				word_id += 1

pickle.dump(vocab,open('vocab.pkl','wb'))
