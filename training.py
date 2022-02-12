import numpy as np  
import json
import torch
import torch.nn as nn
from torch.utils.data import DataLoader,Dataset
from brain import NeuralNetwork
from neural_network import *
# ------------------------------------------
with open('content.json','r') as f:
    contents = json.load(f)
# ------------------------------------------
all_words = []
tags      = []
xy        = []
# --------------------------------------------
for content in contents['content']:
      tag = content['tag']
      tags.append(tag)
      for ptrns in content['patterns']:
          w = tokenize(ptrns)
          all_words.extend(w)
          xy.append((w,tag))
# -----------------------------------------------
ignore_words = [',','?','/','.','!','$','^']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))
# ------------------------------------------------
x_train = [] 
y_train = []
# -------------------------------------------------
for (pattern_word,tag) in xy:
    bag = bag_of_words(pattern_word,all_words)
    x_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)
# -----------------------------------------
x_train = np.array(x_train)
y_train = np.array(y_train)
# -----------------------------------------
num_epoches = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)
# ----------------------------------------
print('Training The Model ... ')
class ChatDataSet(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self,index):
        return self.x_data[index],self.y_data[index]
    

    def __len__(self):
        return self.n_samples
# -------------------------------------------------
ds = ChatDataSet()
train_loader = DataLoader(dataset=ds,
                          batch_size = batch_size,
                          shuffle=True,
                          num_workers=0)
# ----------------------------------------------------
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNetwork(input_size,hidden_size,output_size).to(device=device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
# ------------------------------------------------------
for epoch in range(num_epoches):
    for (words,labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        outputs = model(words)
        loss = criterion(outputs,labels) 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1)%100 == 0:
        print(f'Epoch [{epoch+1} / {num_epoches}], loss [{loss.item():.4f}]')
    
print(f'Final Loss : [{loss.item():.4f}]')
# ------------------------------------------
data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "hidden_size":hidden_size,
    "output_size":output_size,
    "all_words":all_words,
    "tags":tags
}
# ------------------------------------------
FILE = 'TrainingData.pth'
torch.save(data,FILE)
print(f'Train completed and data saved in {FILE}')
# ---------------------------------------------
