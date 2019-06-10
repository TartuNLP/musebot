# polybot
Cross-lingual chatbot creation platform. The input requests are matched to keywords using MUSE (https://github.com/facebookresearch/MUSE), so the input can be given in any language and the patterns/keywords can also be written in any language for which there are MUSE cross-lingual embeddings available.

Features:
* multiple "bots" (topics) supported
* unigram and bigram keywords
* response weighting
* "grabbing attention" in each bot/module
