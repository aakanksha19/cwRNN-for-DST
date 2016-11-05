#!/bin/python

import os
import sys
import pickle
import nltk

input_folder = "../hyps/" #sys.argv[1]
#output_file = "../output_folder" #sys.argv[2]
 
vocab = pickle.load(open("vocab.pkl", "rb" ))

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

def make_feature_vector(current_turn_features):
	fts = []
	for key,value in vocab.iteritems():
		for element in current_turn_features:
			if key == element:
				fts.append(1)
			else:
				fts.append(0)

features = {}
i = 100
for file in os.listdir(input_folder):
	i += 1
	input = open(os.path.join(input_folder,file),'r')
	current_turn_features = [0]*len(vocab.keys())
	turn_wise_features = {}
	idd = 0
	unigrams = []
	bigrams = []
	trigrams = []
	print file
	for line in input:
		#print line
		if line.startswith("turn "):
			if current_turn_features:
				turn_wise_features[idd] = current_turn_features
				idd = idd + 1 
				current_turn_features = [0]*len(vocab.keys())
			continue
		else:
			if len(line.strip().split()) == 1:
				continue
			ws=nltk.word_tokenize(line.strip().split('\t')[0])
			score = line.strip().split('\t')[1]
			bigrams = find_ngrams(ws, 2)
			trigrams = find_ngrams(ws, 3)
			for gram in ws:
				current_turn_features[vocab[gram]] += float(score)
			for gram in bigrams:
				word = gram[0]+" "+gram[1]
				current_turn_features[vocab[word]] += float(score)
			for gram in trigrams:
				word = gram[0]+" "+gram[1]+" "+gram[2]
				current_turn_features[vocab[word]] += float(score)
	features[file] = turn_wise_features
	if i%100 == 0:
		pickle.dump(features,open("feat"+str(i/100)+".pkl","wb"))
		features = {}
