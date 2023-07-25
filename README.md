# Sentence Parser with Context-Free Grammar
`pip install -r requirements.txt`
## Background

A common task in natural language processing is parsing, the process of determining the structure of a sentence. This is useful for a number of reasons: knowing the structure of a sentence can help a computer to better understand the meaning of the sentence, and it can also help the computer extract information out of a sentence. In particular, it’s often useful to extract noun phrases out of a sentence to get an understanding for what the sentence is about.

In this project, we used the context-free grammar formalism to parse English sentences to determine their structure. We applied rewriting rules repeatedly to transform symbols into other symbols. The objective was to start with a nonterminal symbol S (representing a sentence) and repeatedly apply context-free grammar rules until we generated a complete sentence of terminal symbols (i.e., words).

## Understanding

We used the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.

First, look at the text files in the sentences directory. Each file contains an English sentence. Your goal in this problem is to write a parser that is able to parse all of these sentences.

Take a look now at parser.py, and notice the context free grammar rules defined at the top of the file. We’ve already defined for you a set of rules for generating terminal symbols (in the global variable TERMINALS). Notice that Adj is a nonterminal symbol that generates adjectives, Adv generates adverbs, Conj generates conjunctions, Det generates determiners, N generates nouns (spread across multiple lines for readability), P generates prepositions, and V generates verbs.

Next is the definition of NONTERMINALS, which will contain all of the context-free grammar rules for generating nonterminal symbols. Right now, there’s just a single rule: S -> N V. With just that rule, we can generate sentences like "Holmes arrived." or "He chuckled.", but not sentences more complex than that. Editing the NONTERMINALS rules so that all of the sentences can be parsed will be up to you!

Next, take a look at the main function. It first accepts a sentence as input, either from a file or via user input. The sentence is preprocessed (via the preprocess function) and then parsed according to the context-free grammar defined by the file. The resulting trees are printed out, and all of the “noun phrase chunks” (defined in the Specification) are printed as well (via the np_chunk function).

In addition to writing context-free grammar rules for parsing these sentences, the preprocess and np_chunk functions are as follows:


The `preprocess` function was implemented to accept a sentence as input and return a lowercased list of its words. We used nltk’s word_tokenize function to perform tokenization. The function returned a list of words, where each word is a lowercased string. Any word that didn’t contain at least one alphabetic character (e.g. . or 28) was excluded from the returned list.

The `np_chunk` function was implemented to accept a tree representing the syntax of a sentence and return a list of all of the noun phrase chunks in that sentence. A “noun phrase chunk” was defined as a noun phrase that didn’t contain other noun phrases within it. The function returned a list of nltk.tree objects, where each element had the label NP.

The context-free grammar rules in the `NONTERMINALS` global variable were implemented, along with the rules in the `TERMINALS` global variable, to allow the parsing of all sentences in the sentences/ directory. We used the nonterminal symbol NP to represent a “noun phrase”, such as the subject of a sentence.

## Usage

The `parser.py` script provides the main functionality for parsing the sentences and extracting the noun phrase chunks. The script accepts a sentence as input, either from a file or via user input. The sentence is preprocessed using the `preprocess` function and then parsed according to the context-free grammar defined by the file. The resulting trees are printed out, and all of the “noun phrase chunks” are printed as well using the `np_chunk` function.

That's it! The parser has been successfully implemented to parse English sentences and extract noun phrase chunks using context-free grammar rules.
