#!/bin/python

import os
import sys
import pickle
import nltk
import operator
from operator import add

input_folder = "../hyps3/" #sys.argv[1]
#output_file = "../output_folder" #sys.argv[2]
 
vocab = pickle.load(open("vocab3.pkl", "rb" ))

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
i = 1
flist = open("../scripts/config/dstc2_dev.flist", "r")
#flist = open("../flist.txt","r")
for line in flist:
	if line == "\n":
		continue
	file = line.strip().split('/')[1]
	print file
	current_file = {}
	for end in ['acts','batch','live']:
		input = open(os.path.join(input_folder,file+"_"+end+".txt"),'r')
		current_turn_features = [0]*len(vocab.keys())
		turn_wise_features = {}
		idd = 0
		unigrams = []
		bigrams = []
		trigrams = []
		for line in input:
		#print line
			if line.startswith("turn "):
				if line.strip() != "turn 0":			
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
		current_file[file+"_"+end+".txt"] = turn_wise_features
	#print current_file[file+"_acts.txt"][6]
	#print current_file[current_file.keys()[0]][6]
	turns = len(current_file[current_file.keys()[0]].keys())
	final_dict = {}
	for turn in range(turns):
		#print current_file[file+"_acts.txt"][turn]
		#print current_file[file+"_batch.txt"][turn] 
		sum1 = map(add, current_file[file+"_acts.txt"][turn], current_file[file+"_batch.txt"][turn])
		sum2 = map(add, sum1, current_file[file+"_live.txt"][turn])
		final_dict[turn] = sum2
	features[file] = final_dict
	i+=1
	if i%50 == 0:
		pickle.dump(features,open("feat"+str(i/50)+".pkl","wb"))
		features = {}
