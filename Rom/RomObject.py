from Relation import Relation, RelationType


class RomObject:
    def __init__(self, token):
        """
        Initializes a new instance of RomObject.

        Args:
            text (str, optional): The text associated with the object. Defaults to None.
            pos (str, optional): The part-of-speech tag associated with the object. Defaults to None.
        """
        self._token = token
        self._text = token.text
        self._pos = token.pos_
        self._dep = token.dep_
        self._id = None
        self.relation_set = set()
        self._is_destroyed = False

    def __str__(self):
        result = f'<Text: {self._text}, POS: {self._pos}\nRelations:\n'
        for relation in self.relation_set:
            result += str(relation) + '\n'
        return result + '>\n'

    def __repr__(self):
        return self.__str__()

    def set_id(self, ID):
        self._id = ID

    def get_id(self):
        return self._id

    def get_text(self):
        """
        Retrieves the text associated with the object.

        Returns:
            str: The text of the object.
        """
        return self._text

    def get_pos(self):
        """
        Retrieves the part-of-speech (POS) tag associated with the object.

        Returns:
            str: The POS tag of the object.
        """
        return self._pos

    def get_degree(self):
        """
        Calculates the number of relations associated with this object.

        Returns:
            int: The number of relations.
        """
        return len(self.relation_set)

    def remove_relation(self, relation):
        """
        Removes a relation from the object's relation set and destroys it.

        Args:
            relation (Relation): The relation to be removed.
        """
        if relation in self.relation_set:
            self.relation_set.discard(relation)
            relation.destroy()

    def add_relation(self, relation):
        """
        Adds a relation to the object's relation set if the relation involves this object.

        Args:
            relation (Relation): The relation to be added.

        Notes:
            If the relation does not involve this object, an error message is printed.
        """
        if not relation.in_relation(self):
            print(f"Error in RomObject.add_relation: <Rom Object: {self}, Relation: {relation}>")
            return

        self.relation_set.add(relation)

    def disconnect_with(self, obj):
        """
        Removes all relations between this object and another specified object.

        Args:
            obj (RomObject): The object to disconnect relations from.
        """
        remove_set = set()
        for rel in self.relation_set:
            if rel.in_relation(obj):
                remove_set.add(rel)

        for rel in remove_set:
            rel.destroy()

    def destroy(self):
        """
        Destroys the current RomObject by removing all its relations and marking it as destroyed.

        This method iterates through all relations associated with the object, destroys each of them,
        and then marks the object itself as destroyed by setting the `_is_destroyed` attribute to True.
        """
        remove_set = set(self.relation_set)
        for rel in remove_set:
            rel.destroy()

        self._is_destroyed = True

    def is_destroyed(self):
        """
        Checks if the RomObject has been destroyed.

        Returns:
            bool: True if the object is destroyed, False otherwise.
        """
        return self._is_destroyed

    def find_relation_with(self, obj):
        if obj is self:
            return RelationType.NONE

        for rel in self.relation_set:
            if self is rel.get_from_object() and obj is rel.get_to_object():
                return rel.get_relation_type()

        return RelationType.NONE


class RomObjectFactory:
    """
    A factory class for creating and managing relations between RomObject instances.
    """

    @staticmethod
    def connect(from_obj: RomObject, to_obj: RomObject, relation_type: RelationType):
        """
        Establishes a relation between two RomObject instances with the specified relation type.

        Args:
            from_obj (RomObject): The source object of the relation.
            to_obj (RomObject): The target object of the relation.
            relation_type (RelationType): The type of the relation to be established.

        Raises:
            Exception: If an error occurs while creating or adding the relation.
        """
        try:
            relation = Relation(from_obj, to_obj, relation_type)
            from_obj.add_relation(relation)
            to_obj.add_relation(relation)
        except Exception as e:
            print(e)
