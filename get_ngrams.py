#!/bin/python

import os
import sys
import pickle

input_folder = "../output_folder/" #sys.argv[1]
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
for file in os.listdir(input_folder):
	input = open(os.path.join(input_folder,file),'r')
	features[file] = []
	i = 0
	current_turn_features = []
	turn_wise_features = {}
	idd = 0
	unigrams = []
	bigrams = []
	trigrams = []
	for line in input:
		if "turn" in line:
			words=[]
			current_turn_features =  unigrams + bigrams + trigrams
			turn_wise_features[idd] = current_turn_features
			make_feature_vector(current_turn_features)
			idd = idd + 1 
			current_turn_features = []
			continue
		else:
			ws=line.split()
			for element in ws:
				words.append(element)
				unigrams = find_ngrams(words, 1)
				bigrams = find_ngrams(words, 2)
				trigrams = find_ngrams(words, 3)
