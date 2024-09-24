import json
import os


class RomContainer:
    _roms = {}

    @staticmethod
    def add_rom(rom):
        rom_id = 't' + str(len(RomContainer._roms))
        RomContainer._roms[rom_id] = rom
        rom.set_id(rom_id)

    @staticmethod
    def display_information():
        pass


class RomParser:
    @staticmethod
    def rom_to_json(rom):
        rom_dict = dict()
        rom_name = 'text1'
        rom_dict['objects'] = []
        rom_dict['relations'] = []
        rom_dict['text'] = rom.get_sentence()
        relation_set = set()
        for i, obj in enumerate(rom.get_objects()):
            rom_dict['objects'].append(RomParser.rom_object_to_dict(obj, i, rom_name))
            for rel in obj.get_relations():
                relation_set.add(rel)

        for rel in relation_set:
            rom_dict['relations'].append(RomParser.relation_to_dict(rel, rom_name))

        return rom_dict

    @staticmethod
    def rom_object_to_dict(obj, i, rom_name):
        obj_dict = dict()
        obj_dict['name'] = f'object_{RomParser.pad_with_zeros(i, 2)}'
        obj_dict['rom_name'] = rom_name
        obj_dict['romnum'] = 'rom0'
        obj_dict['type'] = type(obj).__name__
        obj_dict['text'] = obj.get_text()
        obj_dict['class'] = obj.get_pos()
        obj_dict['node_id'] = obj.get_id()
        obj_dict['iswrong'] = 'False'
        obj_dict['sentence'] = ''
        return obj_dict

    @staticmethod
    def relation_to_dict(relation, rom_name):
        rel_dict = dict()
        rel_dict['rom_name'] = rom_name
        rel_dict['f_object'] = relation.get_from_object().get_id()
        rel_dict['t_object'] = relation.get_to_object().get_id()
        rel_dict['type'] = str(int(relation.get_relation_type()))
        rel_dict['name'] = f'FF{relation.get_from_object().get_id()}{relation.get_to_object().get_id()}'
        rel_dict['romnum'] = 'rom0'
        return rel_dict

    @staticmethod
    def pad_with_zeros(i, n):
        """
        Converts an integer to a string and pads it with leading zeros if its length is less than n.

        Args:
            i (int): The integer to be converted to a string.
            n (int): The desired length of the output string.

        Returns:
            str: The formatted string with leading zeros if necessary.
        """
        return str(i).zfill(n)

    @staticmethod
    def save_as_json(rom):
        """
        Converts the given rom object to a dictionary using RomParser.rom_to_json
        and saves it as a JSON file in the Rom/outdata folder in the project root directory.

        Args:
            rom: The rom object to be converted and saved.
        """
        RomContainer.add_rom(rom)
        rom_dict = RomParser.rom_to_json(rom)

        save_path = os.path.join("Rom", "outdata", "rom.json")

        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'w', encoding='utf-8') as json_file:
            json.dump(rom_dict, json_file, ensure_ascii=False, indent=4)

        print(f"ROM saved successfully at: {save_path}")
