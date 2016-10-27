import os
import sys

input_folder = sys.argv[1]
output_file = sys.argv[2]

features = {}
for file in os.listdir(input_folder):
	input = open(os.path.join(input_folder,file),'r')
	features[file] = []
	i = 0
	current_turn_features = []
	for line in input:
		if "turn" in line:
			if current_turn_features:
				features[file].append(current_turn_features)
			continue
		data = line.split("\t")
		hypo = data[0]
		score = data[1].strip()
		
