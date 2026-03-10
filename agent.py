import random 
import torch.nn as nn
import torch.optim as optim
import torch
from model import Qnet


class Agent:
    def __init__(self):
        self.model = Qnet()
        self.optimizer = optim.Adam(self.model.parameters(), lr = 0.001)

        self.gamma = 0.9
        self.epsilon = 1
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.1

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 2)
        
        state = torch.tensor(state, dtype=torch.float32)

        with torch.no_grad():
            q = self.model(state)

        return torch.argmax(q).item()
    
