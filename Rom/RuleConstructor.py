import csv
from Relation import RelationType


class RuleConstructor:
    _instance = None
    _csv_dict = None

    def __new__(cls, filename='rules.csv'):
        if cls._instance is None:
            cls._instance = super(RuleConstructor, cls).__new__(cls)
            cls._instance._initialize(filename)
        return cls._instance

    def _initialize(self, filename):
        self.filename = filename
        self._csv_dict = {}
        try:
            with open(filename, 'r') as file:
                self._csv_dict = list(csv.DictReader(file))
        except Exception as e:
            print(e)

    @staticmethod
    def get_instance(filename='rules.csv'):
        if RuleConstructor._instance is None:
            RuleConstructor._instance = RuleConstructor(filename)
        return RuleConstructor._instance

    def get_relation_by_dep(self, dep, pos='NONPOS'):
        try:
            for row in self._csv_dict:
                if row['DEP'] == dep:
                    return RelationType(int(row.get(pos, 0)))
        except Exception as e:
            print(e)
        return RelationType(0)


if __name__ == '__main__':
    rc = RuleConstructor.get_instance()
    relation = rc.get_relation_by_dep('acl')
    print(int(relation))
