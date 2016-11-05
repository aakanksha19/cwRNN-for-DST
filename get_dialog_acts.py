import sys
import os
import json

input_folder = sys.argv[1]
output_folder = sys.argv[2]
for folder in os.listdir(input_folder):
	for subfolder in os.listdir(os.path.join(input_folder,folder)):
		for file in os.listdir(os.path.join(os.path.join(input_folder,folder),subfolder)):
			if file == 'log.json':
				print subfolder
				path = os.path.join(os.path.join(input_folder,folder),subfolder)
				data = json.load(open(os.path.join(path,file),'r'))
				turns = len(data['turns'])
				out1 = open(os.path.join(output_folder,subfolder+"_acts.txt"),'w')
				for turn in range(turns):
					out1.write('turn '+str(turn)+"\n")
					acts = data['turns'][turn]['output']['dialog-acts']
					for act in acts:
						slots = ""
						for slot in act['slots']:
							slots = slot[0]+" "+slot[1]+" "
							out1.write(act['act']+" "+slots.strip()+"\t"+"1.0"+"\n")
				out1.close()
					
