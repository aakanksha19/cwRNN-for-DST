#Output Features = goal-labels, method-label, requested-slots

import os
import json
import cPickle as pickle

class GetOutputFeatures(object):

    def __init__(self,input_folder,output_folder):
        self.read_json(input_folder,output_folder)

    def read_json(self,input_folder,output_folder):
        big_dict = {}
        for folder in os.listdir(os.path.join(input_folder)):
            for subfolder in os.listdir(os.path.join(input_folder,folder)):
                ip_file = open(os.path.join(input_folder,folder,subfolder,"label.json"),"r")
                data = json.load(ip_file)
                n_turns = len(data["turns"])
                list = []
                for turn in range(n_turns):
                    dict = {}
                    dict["turn-index"] = turn
                    dict["goal-labels"] = data["turns"][turn]["goal-labels"]
                    dict["method-label"] = data["turns"][turn]["method-label"]
                    dict["requested-slots"] = data["turns"][turn]["requested-slots"]
                    list.append(dict)
                big_dict[subfolder] = list
                print subfolder
        with open(os.path.join(output_folder,"output_features") + ".p", 'w') as op_file:
            pickle.dump(big_dict, op_file)


if __name__ == "__main__":
    input_folder = "/Users/AC/Desktop/ML/dstc_project/dstc2_traindev/data"
    output_folder = "/Users/AC/Desktop/ML/dstc_project/output_features"
    op = GetOutputFeatures(input_folder,output_folder)