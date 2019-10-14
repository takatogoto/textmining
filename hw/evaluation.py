import argparse
from typing import List, Iterator, Set, Dict, Optional, Tuple
from collections import Counter
from pathlib import Path
import torch
import torch.nn as nn
import sys
import os
sys.path.append('.')
from best_model import BEST_MODEL

RESERVED = ['<pad>', '<unk>']

PAD_IDX = 0 
UNK_IDX = 1

class Vocab:
    """ Mapper of words <--> index """
    def __init__(self, types):
        # types is list of strings
        assert isinstance(types, list)
        #assert isinstance(types[0], str)

        self.idx2word = types
        self.word2idx = {word: idx for idx, word in enumerate(types)}
        assert len(self.idx2word) == len(self.word2idx)

    def __len__(self):
        return len(self.idx2word)

    @staticmethod
    def load(path):
        types = [line.strip() for line in path.open()]
        for idx, tok in enumerate(RESERVED): # check reserved
            assert types[idx] == tok
        return Vocab(types)


class TextDataset:
    def __init__(self, vocab, path):
        self.vocab = vocab
        # for simplicity, loading everything to memory; on large datasets this will cause OOM
        text = [line.strip().split() for line in path.open()]

        # words to index; out-of-vocab words are replaced with UNK
        xs = [[self.vocab.word2idx.get(tok, UNK_IDX) for tok in tokss] 
              for tokss in text]
        self.data = xs

    def as_batches(self, batch_size, shuffle=False): # data already shuffled
        data = self.data
        
        for i in range(0, len(data), batch_size): # i incrememt by batch_size
            batch = data[i: i + batch_size]  # slice
            yield self.batch_as_tensors(batch)
  
    @staticmethod
    def batch_as_tensors(batch):
        n_ex = len(batch)
        max_len = max(len(seq) for seq in batch)
        seqs_tensor = torch.full(size=(n_ex, max_len), fill_value=PAD_IDX,
                                 dtype=torch.long)
    
        for i, seq in enumerate(batch):
            seqs_tensor[i, 0:len(seq)] = torch.tensor(seq)
      
        return seqs_tensor


def main(args):

    vocab = Vocab.load(Path(args.vocab_file))
    assert len(vocab) == 10002

    test_data = TextDataset(vocab=vocab, path=Path(args.input_file))

    checkpoint = torch.load(args.model_file, map_location=lambda storage, loc: storage)
    
    model = BEST_MODEL(len(vocab), len(vocab))
    
    model.load_state_dict(checkpoint['state_dict'])

    loss_func = nn.NLLLoss(reduction='none')
    
    with torch.no_grad():
        model.eval()
        val_loss = 0
        n_val_batches = 0
        
        for seqs in test_data.as_batches(batch_size=args.batch_size, shuffle=False):
            # Move input to desired device
            seq_loss = torch.zeros(1).to(torch.device('cpu'))
            for i in range(1, seqs.size()[1]-1):
                # Move input to desired device
                cur_seqs = seqs[:, :i].to(torch.device('cpu'))
                cur_tars = seqs[:, i].to(torch.device('cpu'))

                log_probs = model(cur_seqs)
                seq_loss += loss_func(log_probs, cur_tars).sum() / len(seqs)
            
            seq_loss /= (seqs.shape[1] - 1)
            val_loss += seq_loss.item() 
            n_val_batches += 1
        avg_val_loss = val_loss / n_val_batches
    
    print("Test Average NLL is %.6f" % avg_val_loss)
    with open(args.output_file, 'w') as res:
        res.write("%.6f" % avg_val_loss)
    
    return 
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-model_file', type=str, help='<modelfile>')
    p.add_argument('-input_file', type=str, help='<inputfile>')
    p.add_argument('-output_file', type=str, help='<outputfile>')
    p.add_argument('-vocab_file', type=str, help='<vocabfile>')
    p.add_argument('-batch_size', type=int, default=256)
    args = p.parse_args()
    main(args)
