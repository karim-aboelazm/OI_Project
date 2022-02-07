# pip install torch >> 'Python=3.9.7'
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self,inputs,hidden,outputs):
        super(NeuralNetwork, self).__init__()
        
        self.layerOne = nn.Linear(inputs,hidden) # Layer one in inputs -> hidden

        self.layerTwo = nn.Linear(hidden,hidden) # Layer two in hidden -> hidden
        
        self.layerThree = nn.Linear(hidden,outputs) # Layer three in hidden -> output
        
        self.relu = nn.ReLU() # ReLU for relationship
    
    def forward(self,x):
        out = self.layerOne(x)
        out.relu(out)
        out = self.layerTwo(out)
        out.relu(out)
        out = self.layerThree(out)
        return out