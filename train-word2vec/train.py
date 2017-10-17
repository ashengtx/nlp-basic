import os
# import modules & set up logging
import gensim, logging
from gensim.models import Word2Vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_path = "./corpus"

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname), encoding='utf8'):
                yield line.split()

sentences = MySentences(data_path) # a memory-friendly iterator
model = Word2Vec(sentences, size=300, window=5, min_count=5, workers=4)
model.save('./my-word2vec')
