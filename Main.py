from Model import Sequential

model = Sequential()
model.add(num_neuron = 5, input_shape = (15,))
model.add(num_neuron = 5, activation = 'relu')
model.add(num_neuron = 5, activation = 'relu')
model.add(num_neuron = 5, activation = 'softmax')




