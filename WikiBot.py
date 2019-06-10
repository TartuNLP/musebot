#!/usr/bin/env python
# coding: utf-8

# In[1]:


import import_ipynb
from PolyBot import *
import wikipedia


# In[7]:


class WikiBot(Answers):
 
    def answer_wiki(self, frase_sorry, frase_noinfo, topic, PERSON,  CITY):
        if topic != None:
            try:
                res = ".".join(wikipedia.summary(wikipedia.search(topic, results=1)).split('.')[0:2])
                print('BOT:', res)
            except:
                print(frase_sorry)
                response = input('YOU: ').lower()
                try:
                    res = ".".join(wikipedia.summary(wikipedia.search(response, results=1)).split('.')[0:2])
                    print("BOT:", res)
                except:
                    print(frase_noinfo, response)
        else:   
            try:
                if PERSON != None:
                    res = ".".join(wikipedia.summary(wikipedia.search(PERSON, results=1)).split('.')[0:2])
                    print('BOT:', res)
                elif CITY != None:
                    res = ".".join(wikipedia.summary(wikipedia.search(CITY, results=1)).split('.')[0:2])
                    print('BOT:', res)
                else:
                    print(frase_sorry)
                    response = input('YOU: ').lower()
                    try:
                        res = ".".join(wikipedia.summary(wikipedia.search(response, results=1)).split('.')[0:2])
                        print("BOT:", res)
                    except:
                        print(frase_noinfo, response)
            except:
                print(frase_sorry)
                response = input('YOU: ').lower()
                try:
                    res = ".".join(wikipedia.summary(wikipedia.search(response, results=1)).split('.')[0:2])
                    print("BOT:", res)
                except:
                    print(frase_noinfo, response) 
        
        

    def Answer_Wiki(self, NER_dict):
        
        input_sent = NER_dict['input']
        PERSON = NER_dict['PERSON']
        language = NER_dict['language']
        CITY = NER_dict['CITY']
        WHAT = NER_dict['what_is']
        if WHAT == True:
            topic = input_sent[2:]
            topic= " ".join(topic)
        else:
            topic = None
        

        # We hard-coded dummy answers for all the languages, they provide different answers whether locality and time are given
        # in the input: if they are not given, the function will ask for it.


        if language == 'EN':
            wikipedia.set_lang("en")
            self.answer_wiki("BOT: Sorry I am not sure I understood, which topic were you looking for?",
                        "BOT: Sorry we don't have information about", topic, PERSON,  CITY)

        elif language == 'ES':
            wikipedia.set_lang("es")
            self.answer_wiki("BOT: Lo siento, no estoy seguro de haber entendido, ¿qué tema buscabas?",
                       "BOT: Lo sentimos, no tenemos información sobre", topic, PERSON, CITY)

        elif language == 'RU':
            wikipedia.set_lang("ru")
            self.answer_wiki("BOT: Извините, я не уверен, что понял, какую тему вы искали?",
                       "BOT: Извините, у нас нет информации о", topic, PERSON,  CITY)

        elif language == 'ET':
            wikipedia.set_lang("et")
            self.answer_wiki("BOT: Vabandust, et ma ei ole kindel, et sain aru, millist teemat otsisite?",
                       "BOT: Vabandame, et meil pole teavet", topic,  PERSON,  CITY)

        elif language == 'IT':
            wikipedia.set_lang("it")
            self.answer_wiki("BOT: Mi dispiace non sono sicuro di aver capito, quale argomento stavi cercando?",
                       "BOT: Ci dispiace, non abbiamo informazioni su", topic,  PERSON,  CITY)
            
        elif language == 'DE':
            wikipedia.set_lang("de")
            self.answer_wiki("BOT: Es tut mir leid, ich bin nicht sicher, ob ich verstanden habe, nach welchem Thema suchten Sie?",
                       "BOT: Entschuldigung, wir haben keine Informationen über", topic, PERSON,  CITY)


# In[8]:


wbot = WikiBot()


# In[9]:


# keywords, kw_lang, answer, cutoff=0.43, boost=0, all_lang=None, bigrams=None,  
#bigram_lang=None, bigram_cutoff = 1.8, bigram_boost = 1, b2=None, b2_lang=None, b2_cutoff=1.8, b2_boost=1, outputlangs=None

wikibot = PolyBot(['wikipedia', 'meaning', 'mean', 'sense'],
                 'EN',
                wbot.Answer_Wiki,
                 bigrams=[('what', 'is'), ('where', 'is'), ('who', 'is')],
                 bigram_cutoff = 0.8)


# In[ ]:




