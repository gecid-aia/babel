import nltk.translate.bleu_score as bleu
import nltk.translate.gleu_score as gleu
import numpy as np

text1 = "Hello, my name is Lucas and I like to code"
text2 = "Hello everyone, I'm Lucas and I like to code"

hypothesis = text1.split()
reference1 = text2.split()

def wer_score(hyp, ref, print_matrix=False):
  N = len(hyp)
  M = len(ref)
  L = np.zeros((N,M))
  for i in range(0, N):
    for j in range(0, M):
      if min(i,j) == 0:
        L[i,j] = max(i,j)
      else:
        deletion = L[i-1,j] + 1
        insertion = L[i,j-1] + 1
        sub = 1 if hyp[i] != ref[j] else 0
        substitution = L[i-1,j-1] + sub
        L[i,j] = min(deletion, min(insertion, substitution))
        # print("{} - {}: del {} ins {} sub {} s {}".format(hyp[i], ref[j], deletion, insertion, substitution, sub))
  if print_matrix:
    print("WER matrix ({}x{}): ".format(N, M))
    print(L)
  return int(L[N-1, M-1])

# ref: https://github.com/gcunhase/NLPMetrics/blob/master/notebooks/bleu.ipynb
BLEUscore = bleu.sentence_bleu([reference1], hypothesis)

# ref: https://github.com/gcunhase/NLPMetrics/blob/master/notebooks/gleu.ipynb
GLEUscore = gleu.sentence_gleu([reference1], hypothesis)

# ref: https://github.com/gcunhase/NLPMetrics/blob/master/notebooks/wer.ipynb
WERscore = wer_score(hypothesis, reference1, print_matrix=False)

print('scores:\n')
print('>> BLEU:\t{0:1.3f}'.format(BLEUscore))
print('>> GLEU:\t{0:1.3f}'.format(GLEUscore))
print('>> WER: \t{0}'.format(WERscore))