from NLPModelSingleton import *
from RomParser import *
from RomObject import *
from RuleConstructor import *


class Rom:
    sympos = ["PUNCT", "SYM", "X"]

    def __init__(self, sentence):
        self._id = None
        self.sentence = sentence
        self.objects = []
        self.object_map = {}
        self.relational_matrix = None
        self.doc = None
        self.create_objects_from_sentence(self.sentence)
        self.create_relation_from_object()

    def __str__(self):
        result = '-' * 50 + f'\nSentence: {self.sentence}\n'
        for obj in self.objects:
            result += str(obj)
        return result + '\n'

    def __repr__(self):
        return self.__str__()

    def set_id(self, ID):
        self._id = ID
        for i, obj in enumerate(self.objects):
            obj.set_id(self._id + RomParser.pad_with_zeros(i, 2))

    def get_id(self):
        if self._id is None:
            return "None"
        return self._id

    def get_objects(self):
        return self.objects

    def get_sentence(self):
        return self.sentence

    def get_indexed_token(self):
        result = ""
        for i, obj in enumerate(self.objects):
            result += f' {obj.get_text()}-({0},{i})'
        return result.strip() + "."

    def create_objects_from_sentence(self, sentence):
        self.doc = NLPModelSingleton.get_instance().nlp(sentence)
        for token in self.doc:
            # print(f'Text: {token.text},\tPOS: {token.pos_},\tDEP: {token.dep_},\tHead: {token.head.text}')
            if token.pos_ not in Rom.sympos:
                romObj = RomObject(token)
                self.objects.append(romObj)
                self.object_map[token] = romObj

    def create_relation_from_object(self):
        for token in self.object_map:
            if token.dep_ == "ROOT":
                continue
            from_obj = self.object_map[token]
            to_obj = self.object_map[token.head]
            relation_type = RuleConstructor.get_instance().get_relation_by_dep(token.dep_)
            if relation_type is not RelationType.NONE:
                RomObjectFactory.connect(from_obj, to_obj, relation_type)

    def get_relational_matrix(self):
        if self.relational_matrix is None:
            matrix = [[0] * len(self.objects) for _ in range(len(self.objects))]
            for i, obj1 in enumerate(self.objects):
                for j, obj2 in enumerate(self.objects):
                    matrix[i][j] = int(obj1.find_relation_with(obj2))
            self.relational_matrix = matrix
            return matrix
        return self.relational_matrix

    def self_merging(self):
        if self.doc is None:
            print(f'Error in Rom.self_merging: self.doc is None')
            return



class RomComposite:
    def __init__(self, rom_list):
        self.roms = rom_list
        self.sentences = " ".join([rom.get_sentence() for rom in self.roms])
        self.objects = []
        self.object_map = {}
        for rom in self.roms:
            for obj in rom.get_objects():
                self.objects.append(obj)
            for token in rom.object_map:
                self.object_map[token] = rom.object_map[token]
        self.relational_matrix = None

    def __str__(self):
        return "\n".join(str(rom) for rom in self.roms)

    def __repr__(self):
        return self.__str__()

    def get_objects(self):
        return self.objects

    def get_sentence(self):
        return self.sentences

    def get_indexed_token(self):
        result = ""
        for i, rom in enumerate(self.roms):
            for j, obj in enumerate(rom.get_objects()):
                result += f' {obj.get_text()}-({i},{j})'
            result += "."
        return result.strip()


if __name__ == '__main__':
    rom1 = Rom("This is a cat.")
    rom2 = Rom("This is a dog.")

    compositeRom = RomComposite([rom1, rom2])
    print(rom1.get_relational_matrix())
