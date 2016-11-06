import pickle

output_pickle = pickle.load(open("../output_features/output_features.p","rb"))

X_train = []
y_train_method = []
y_train_request = []

method_slots = ['none','byconstraints','byname','finished','byalternatives']
request_slots = ['addr','area','food','phone','pricerange','postcode','signature','name','none']
train_flist = open("../scripts/config/dstc2_train.flist")
dev_flist = open("../scripts/config/dstc2_dev.flist")
train_output = {}
test_output = {}

index = 0
for i in range(1,33):
	input_features = pickle.load(open("features/feat"+str(i)+".pkl"))
	for key in input_features:
		print key
		turns = len(input_features[key].keys())
		#print turns
		X_train.append([[]]*turns)
		y_train_method.append([[0]*len(method_slots)]*turns)
		y_train_request.append([[0]*len(request_slots)]*turns)
		for turn in range(turns):
			#print turn
			X_train[index][turn] = input_features[key][turn]
			y_train_request[index][turn][method_slots.index(output_pickle[key][turn]['method-label'])] = 1
			for slot in output_pickle[key][turn]['requested-slots']:
				y_train_request[index][turn][request_slots.index(slot)] = 1
		index += 1

pickle.dump(X_train,open("X_train.pkl","wb"))
pickle.dump(y_train_method,open("y_train_method.pkl","wb"))
pickle.dump(y_train_request,open("y_train_request.pkl","wb"))


