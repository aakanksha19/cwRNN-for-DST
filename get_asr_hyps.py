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
				out1 = open(os.path.join(output_folder,subfolder+"_live.txt"),'w')
				out2 = open(os.path.join(output_folder,subfolder+"_batch.txt"),'w')
				for turn in range(turns):
					out1.write('turn '+str(turn)+"\n")
					out2.write('turn '+str(turn)+"\n")
					sys1_hyps = data['turns'][turn]['input']['live']['asr-hyps']
					sys2_hyps = data['turns'][turn]['input']['batch']['asr-hyps']
					for hyp in sys1_hyps:
						out1.write(hyp['asr-hyp']+"\t"+str(hyp['score'])+"\n")
					for hyp in sys2_hyps:
						out2.write(hyp['asr-hyp']+"\t"+str(hyp['score'])+"\n")
				out1.close()
				out2.close()
					
