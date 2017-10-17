# import modules & set up logging
import gensim, logging
from gensim.models import Word2Vec
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = Word2Vec.load("./my-word2vec")
print("(你, 我)的相似度是：", model.wv.similarity("你", "我"))
print("'你'的word2vec向量：")
print(model.wv['你'])
