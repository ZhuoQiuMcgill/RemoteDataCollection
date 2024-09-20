from NLPModelSingleton import *
from RomObject import *
from RuleConstructor import *


class Rom:
    def __init__(self, sentence):
        self.model = NLPModelSingleton.get_instance()
        self.rc = RuleConstructor.get_instance()
        self.sentence = sentence
        self.objects = []
        self.sympos = ["PUNCT", "SYM", "X"]
        self.object_map = {}
        self.create_objects_from_sentence(self.sentence)
        self.create_relation_from_object()

    def __str__(self):
        result = '-' * 50 + f'\nSentence: {self.sentence}\n'
        for obj in self.objects:
            result += str(obj)
        return result + '\n'

    def __repr__(self):
        return self.__str__()

    def create_objects_from_sentence(self, sentence):
        doc = self.model.nlp(sentence)
        for token in doc:
            # print(f'Text: {token.text},\tPOS: {token.pos_},\tDEP: {token.dep_},\tHead: {token.head.text}')
            if token.pos_ not in self.sympos:
                romObj = RomObject(token)
                self.objects.append(romObj)
                self.object_map[token] = romObj

    def create_relation_from_object(self):
        for token in self.object_map:
            if token.dep_ == "ROOT":
                continue
            from_obj = self.object_map[token]
            to_obj = self.object_map[token.head]
            relation_type = self.rc.get_relation_by_dep(token.dep_)
            if relation_type is not RelationType.NONE:
                RomObjectFactory.connect(from_obj, to_obj, relation_type)

    def get_relation_matrix(self):
        matrix = [[0] * len(self.objects) for _ in range(len(self.objects))]
        for i, obj1 in enumerate(self.objects):
            for j, obj2 in enumerate(self.objects):
                matrix[i][j] = int(obj1.find_relation_with(obj2))
        return matrix


if __name__ == '__main__':
    rom = Rom("This is a black cat.")
    print(rom.get_relation_matrix())
