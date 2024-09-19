from enum import IntEnum


class RelationType(IntEnum):
    NONE = 0,
    ConstraintRelation = 1,
    EqualRelation = 2,
    PlainConnectionRelation = 3,
    ConnectionRelation = 4,
    PredicateRelation = 5,
    PlainPredicateRelation = 6,

    def __str__(self):
        return self.name


class Relation:
    """
    Represents a relationship between two objects with a specific type.

    Attributes:
        from_object (Any): The starting object of the relation.
        to_object (Any): The ending object of the relation.
        relation_type (RelationType): The type of the relation, based on the `RelationType` enum.
    """

    def __init__(self, from_object=None, to_object=None, relation_type=None):
        """
        Initializes a Relation object with optional starting and ending objects and a relation type.

        Args:
            from_object (RomObject, optional): The starting object of the relation. Defaults to None.
            to_object (RomObject, optional): The ending object of the relation. Defaults to None.
            relation_type (RelationType, optional): The type of the relation. Defaults to None.
        """
        self.from_object = from_object
        self.to_object = to_object
        self.relation_type = relation_type

    def __str__(self):
        """
        Returns a string representation of the Relation object.

        Returns:
            str: A string that describes the relation including its from and to objects' OData and relation type name.
        """
        return f"Relation <{self.from_object.get_text()}, {self.to_object.get_text()}> -> {self.relation_type}"

    def set_from_object(self, obj):
        """
        Sets the starting object of the relation.

        Args:
            obj (RomObject): The object to set as the starting point of the relation.
        """
        self.from_object = obj

    def set_to_obj(self, obj):
        """
        Sets the ending object of the relation.

        Args:
            obj (RomObject): The object to set as the ending point of the relation.
        """
        self.to_object = obj

    def get_from_object(self):
        """
        Retrieves the starting object of the relation.

        Returns:
            RomObject: The starting object of the relation.
        """
        return self.from_object

    def get_to_object(self):
        """
        Retrieves the ending object of the relation.

        Returns:
            RomObject: The ending object of the relation.
        """
        return self.to_object

    def get_relation_type(self):
        """
        Retrieves the type of the relation.

        Returns:
            RelationType: The type of the relation.
        """
        return self.relation_type

    def self_pointing(self):
        """
        Checks if the relation is self-pointing (i.e., the from and to objects are the same).

        Returns:
            bool: True if the relation is self-pointing, False otherwise.
        """
        return self.from_object is self.to_object

    def is_incomplete(self):
        """
        Checks if the relation is incomplete (i.e., if any of the attributes are None).

        Returns:
            bool: True if the relation is incomplete, False otherwise.
        """
        return self.from_object is None or self.to_object is None or self.relation_type is None

    def is_equal_relation(self):
        """
        Checks if the relation type is an EqualRelation.

        Returns:
            bool: True if the relation type is EqualRelation, False otherwise.
        """
        return self.relation_type == RelationType.EqualRelation

    def in_relation(self, obj):
        """
        Checks if the given object is part of the relation (either as from_object or to_object).

        Args:
            obj (RomObject): The object to check.

        Returns:
            bool: True if the object is in the relation, False otherwise.
        """
        return obj is self.from_object or obj is self.to_object

    def destroy(self):
        """
        Destroys the relation by removing it from the from_object and to_object if they exist.
        """
        if self.from_object:
            self.from_object.remove_relation(self)
        if self.to_object:
            self.to_object.remove_relation(self)
