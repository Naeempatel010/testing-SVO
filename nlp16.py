from nltk.parse.corenlp import CoreNLPParser
from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parse,= dep_parser.raw_parse('The quick brown fox jumps over the lazy dog.')
#print(parse.to_conll(4))
parser=CoreNLPParser(url='http://localhost:9000')

#for governor, dep, dependent in parse.triples():
    #print(governor)
noun_types = ["NN", "NNP", "NNPS","NNS","PRP"]
sentence="Naeem is a good boy"
pred_verb_phrase_siblings = None
adjective_types = ["JJ","JJR","JJS"]
verb_types = ["VB","VBD","VBG","VBN", "VBP", "VBZ"]
#next(parser.raw_parse('Naeem loves to play football and he hates cricket')).pretty_print()
p=next(parser.raw_parse(sentence))

sub_tree=p
def get_subject(sub_tree):
        
    sub_nodes = []
    sub_nodes = sub_tree.subtrees()
    sub_nodes = [each for each in sub_nodes if each.pos()]
    subject = None

    for each in sub_nodes:
        if each.label() in noun_types:
            subject = each.leaves()
            break

    return subject

s=get_subject(p)
print(s)
def get_object(sub_tree):
        siblings = None
        Object = None
        for each_tree in sub_tree:
            if each_tree.label() in ["NP","PP"]:
                sub_nodes = each_tree.subtrees()
                sub_nodes = [each for each in sub_nodes if each.pos()]

                for each in sub_nodes:
                    if each.label() in noun_types:
                        Object = each.leaves()
                        break
                break
            else:
                sub_nodes = each_tree.subtrees()
                sub_nodes = [each for each in sub_nodes if each.pos()]
                for each in sub_nodes:
                    if each.label() in adjective_types:
                        Object = each.leaves()
                        break
                # Get first noun in the tree
        pred_verb_phrase_siblings = None
        return Object
o=get_object(p)
print(o)
def get_predicate(sub_tree):
        sub_nodes = []
        sub_nodes = sub_tree.subtrees()
        sub_nodes = [each for each in sub_nodes if each.pos()]
        predicate = None
        pred_verb_phrase_siblings = []
        sub_tree  = ParentedTree.convert(sub_tree)
        for each in sub_nodes:
            if each.label() in self.verb_types:
                sub_tree = each
                predicate = each.leaves()

        #get all predicate_verb_phrase_siblings to be able to get the object
        sub_tree  = ParentedTree.convert(sub_tree)
        if predicate:
             pred_verb_phrase_siblings = self.tree_root.subtrees()
             pred_verb_phrase_siblings = [each for each in pred_verb_phrase_siblings if each.label() in ["NP","PP","ADJP","ADVP"]]
             self.pred_verb_phrase_siblings = pred_verb_phrase_siblings

        return {'predicate':predicate}


    

