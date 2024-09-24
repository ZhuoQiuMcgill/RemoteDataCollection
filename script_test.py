from Rom.Rom import Rom, RomComposite
from Rom.RomParser import RomParser

rom1 = Rom('Although he was very busy with his work, Peter had had enough of it.')
rom2 = Rom('He loves cat.')
rom = RomComposite([rom1, rom2])
print(RomParser.save_as_json(rom))
