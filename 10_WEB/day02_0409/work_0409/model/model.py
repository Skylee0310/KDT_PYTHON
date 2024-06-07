import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, vocab_size, input_size, hidden_size, num_layers, dropout, output_size):
        super(LSTM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, input_size)
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden_size, output_size)
        self.init_weights()
    
    def init_weights(self):
        initrange = 0.5
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text):
        embedded = self.embedding(text)
        out, _ = self.lstm(embedded)
        out = self.fc(out[:, -1, :])
        return out