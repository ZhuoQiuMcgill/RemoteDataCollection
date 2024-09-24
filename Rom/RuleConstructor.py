import csv
import os
from Rom.Relation import RelationType


def get_rules_csv_path():
    """
    Returns the absolute path to the 'rules.csv' file located in the Rom folder of the project.

    Returns:
        str: The absolute path to 'rules.csv'.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))  # 上一级目录为根目录
    rules_csv_path = os.path.join(project_root, "Rom", "rules.csv")

    return rules_csv_path


class RuleConstructor:
    """
    A singleton class that reads relation rules from a CSV file and provides methods to retrieve relations
    based on dependency tags. This class uses a singleton pattern to ensure only one instance is created.

    Attributes:
        _instance (RuleConstructor): The singleton instance of the RuleConstructor class.
        _csv_dict (list): A list of dictionaries representing the rows of the CSV file.
        filename (str): The name of the CSV file to read relation rules from.
    """
    _instance = None
    _csv_dict = None

    def __new__(cls, filename='rules.csv'):
        """
        Creates a new instance of RuleConstructor if it does not exist; otherwise, returns the existing instance.

        Args:
            filename (str): The name of the CSV file containing the rules. Defaults to 'rules.csv'.

        Returns:
            RuleConstructor: The singleton instance of the RuleConstructor class.
        """
        if cls._instance is None:
            cls._instance = super(RuleConstructor, cls).__new__(cls)
            cls._instance._initialize(filename)
        return cls._instance

    def _initialize(self, filename):
        """
        Initializes the RuleConstructor instance by loading the rules from the specified CSV file.

        Args:
            filename (str): The name of the CSV file containing the rules.
        """
        self.filename = filename
        self._csv_dict = {}
        try:
            with open(filename, 'r') as file:
                self._csv_dict = list(csv.DictReader(file))
        except Exception as e:
            print(e)

    @staticmethod
    def get_instance(filename=get_rules_csv_path()):
        """
        Retrieves the singleton instance of RuleConstructor, creating it if necessary.

        Args:
            filename (str): The name of the CSV file containing the rules. Defaults to 'rules.csv'.

        Returns:
            RuleConstructor: The singleton instance of the RuleConstructor class.
        """
        if RuleConstructor._instance is None:
            RuleConstructor._instance = RuleConstructor(filename)
        return RuleConstructor._instance

    def get_relation_by_dep(self, dep, pos='NONPOS'):
        """
        Retrieves the relation type based on a given dependency tag and optional part-of-speech tag.

        Args:
            dep (str): The dependency tag to look up in the rules.
            pos (str): The part-of-speech tag to look up in the rules. Defaults to 'NONPOS'.

        Returns:
            RelationType: The relation type corresponding to the provided dependency and part-of-speech tag.
                          Returns RelationType(0) if no matching rule is found or an error occurs.
        """
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
