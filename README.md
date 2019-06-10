# polybot
Cross-lingual chatbot creation platform. The input requests are matched to keywords using MUSE (https://github.com/facebookresearch/MUSE), so the input can be given in any language and the patterns/keywords can also be written in any language for which there are MUSE cross-lingual embeddings available.

## Features:
* multiple "bots" (topics) supported via estimated confidence
* unigram and bigram keywords
* keyword weighting
* "grabbing initiative" in each bot/module

## Dependencies:
* polyglot (for multilingual NER)
* googletrans (for translating the response)
* sklearn
* numpy

## Usage demo:
    import polybot
    #jason, please continue

## Adding a bot:
    #jason, that's also up to you
