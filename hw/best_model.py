import torch

PAD_IDX =0
class BEST_MODEL(torch.nn.Module):
    def __init__(self, vocab_size, n_class,  emb_dim=20, hid=100, num_layers=1, dropout=0.5):
        super(BEST_MODEL, self).__init__()
        self.embedding = torch.nn.Embedding(num_embeddings=vocab_size, 
                                      embedding_dim=emb_dim, padding_idx=PAD_IDX)
        self.rnn = torch.nn.RNN(input_size= emb_dim, hidden_size= hid,
                                num_layers = num_layers, dropout=dropout)
        self.linear = torch.nn.Linear(hid, n_class)
        
        self.dropout1 = torch.nn.Dropout1(p=dropout)
        self.dropout2 = torch.nn.Dropout1(p=dropout)


    def forward(self, seqs, log_probs=True):
        batch_size, max_len = seqs.shape

        
        scores = self.embedding(seqs)  # embs[Batch x SeqLen x EmbDim]
        #print("embsshape1 [Batch x SeqLen x EmbDim]", scores.shape)

        #out, next_h = self.rnn(embs, prev_h)
        # input of shape (seq_len, batch, input_size)
        scores = scores.permute(1, 0, 2)
        scores = self.dropout1(scores)

        scores, _ = self.rnn(scores) 
        scores = self.dropout2(scores)
        #print("after rnn (seq_len, batch, num_directions * hidden_size)",
        #      scores.shape)

        # output of shape (seq_len, batch, num_directions * hidden_size)

        #scores = self.linear(scores) # should be [seq_len, batch, n_class]
        scores = self.linear(scores[max_len-1,:,:])
        #print("after liner", scores.shape)

        #print("scores size", scores.shape)
        #scores = scores.sum(dim=0) # sum over all all steps in seq [batch, n_class]
        #scores = scores[max_len-1, :, :]
        
        if log_probs:
          return torch.log_softmax(scores, dim=1)
        else:
          return torch.softmax(scores, dim=1)
          
