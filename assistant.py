import random
import json
import torch
from brain import NeuralNetwork
from neural_network import *
from voice_input import voiceInput
from voice_output import voiceOutput
from functionality import *
# ------------------------------------------------------------------

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# -------------------------------------------------------------------

with open('content.json','r') as jd:
    contents = json.load(jd)

# -------------------------------------------------------------------

FILE = 'TrainingData.pth'
data = torch.load(FILE)

# -------------------------------------------------------------------

model_state = data['model_state']
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']

# ---------------------------------------------------------------
model = NeuralNetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# ---------------------------------------------------------------
def assistant():
    stm = voiceInput()
    result = str(stm)
    if stm=="exit" or stm == None:
        voiceOutput('Goodbye Sir')
        exit()
    
    stm = tokenize(stm)
    w = bag_of_words(stm,all_words)  
    w = w.reshape(1,w.shape[0])   
    w = torch.from_numpy(w).to(device)
    output = model(w)

# ---------------------------------------------------------------
 
    _ , predicted = torch.max(output,dim=1) 
    item = predicted.item()
    tag = tags[item]
    probs = torch.softmax(output,dim=1)
    prob = probs[0][item]
    if prob.item() > 0.75:
        for content in contents['content']:
            if tag == content['tag']:
                reply = random.choice(content['responses'])
                if 'time' in reply:
                    get_error(reply)
                elif 'date' in reply:
                    get_error(reply)
                elif 'day' in reply:
                    get_error(reply)
                elif "wikipedia" in reply:
                    voiceOutput('Searching Sir...')
                    get_input_error(reply,stm)
                elif "google" in reply:
                    voiceOutput('Searching Sir...')
                    get_input_error(reply,result)
                else:    
                    voiceOutput(reply)

# ---------------------------------------------------------------
while True:
    assistant()
