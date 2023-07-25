import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> CL | CL Conj CL | CL Conj VP
DP -> Det N
AN -> Adj N | Adj Adj N | Adj Adj Adj N
NP -> N | DP | DP P N | DP P DP| DP Adv | AN | Det AN
VS -> V | V P | Adv V | V adv
VP -> VS | VS NP | VS NP P NP 
CL -> NP VP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    tokens = nltk.tokenize.word_tokenize(sentence.lower())
    processed = [token for token in tokens if any(char.isalpha() for char in token)]
    return processed

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks_list = []

    sub_np_chunk(tree, chunks_list)

    return chunks_list

def sub_np_chunk(tree, chunks_list):
    if chunks_list is None:
        chunks_list = []

    if tree.label() == "NP" and not any(subtree.label() == "NP" for subtree in tree):
        chunks_list.append(tree)

    for subtree in tree:
        if isinstance(subtree, nltk.Tree):
            sub_np_chunk(subtree, chunks_list)

    return


if __name__ == "__main__":
    main()
