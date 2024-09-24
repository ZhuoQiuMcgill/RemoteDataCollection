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
        for i, obj in enumerate(rom.get_objects()):
            rom_dict['objects'].append(RomParser.rom_object_to_dict(obj, i, rom_name))

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

        pass

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
