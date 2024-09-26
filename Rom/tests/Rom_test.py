from random import randint, choice
import unittest

from Rom.NLPModelSingleton import NLPModelSingleton
from Rom.Rom import Rom, RomComposite


class TestRomComposite(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Computational geometry claims the two aims of solving practical problems and producing beautiful " \
                    "mathematics. There is a natural tension between these goals: the most elegant formulation of a " \
                    "problem rarely occurs in practice. But surprisingly often the aims complement each other. This " \
                    "chapter discusses the interplay between an important practical problem|nite element mesh " \
                    "generation, and a ourishing theoretical area|optimal triangulation algorithms."

    def test_sentences_split(self):
        sents = NLPModelSingleton.split_into_sentences(self.text)
        self.assertEqual(len(sents), 4)

    def test_rom_generation(self):
        sents = NLPModelSingleton.split_into_sentences(self.text)
        roms = []
        for sent in sents:
            roms.append(Rom(sent))
        self.assertEqual(len(roms), 4)
        self.assertEqual(len(roms[0].get_objects()), 14)

    def test_rom_composite_generation(self):
        sents = NLPModelSingleton.split_into_sentences(self.text)
        roms = []
        for sent in sents:
            roms.append(Rom(sent))
        rom_composite = RomComposite(roms)
        random_rom = choice(roms)
        self.assertIn(choice(random_rom.get_objects()), rom_composite.get_objects())

    def test_add_rom_to_composite(self):
        sents = NLPModelSingleton.split_into_sentences(self.text)
        roms = [Rom(sent) for sent in sents]

        rom_composite = RomComposite()
        rom_composite.add_rom(roms[0])

        actual_sentence = rom_composite.get_sentence().strip()
        expected_sentence = sents[0].strip()

        self.assertEqual(
            actual_sentence,
            expected_sentence,
            f"Test failed: The sentence in the composite does not match the expected sentence.\n"
            f"Expected: {expected_sentence}\nActual: {actual_sentence}"
        )

    def test_pop_rom_from_composite(self):
        sents = NLPModelSingleton.split_into_sentences(self.text)
        roms = [Rom(sent) for sent in sents]

        rom_composite = RomComposite(roms[:])
        poped_rom = rom_composite.pop_rom()

        actual_sentence = rom_composite.get_sentence().strip()
        expected_sentence = " ".join(sents[1:]).strip()

        self.assertEqual(
            actual_sentence,
            expected_sentence,
            f"Test failed: The sentence in the composite does not match the expected sentence.\n"
            f"Expected: {expected_sentence}\nActual: {actual_sentence}"
        )

        self.assertIs(poped_rom, roms[0])

        removed_obj = roms[0].get_objects()[0]
        self.assertNotIn(
            removed_obj,
            rom_composite.get_objects(),
            f"Test failed: The removed object is still inside the composite,\n"
            f"Removed Object: {removed_obj}\n"
            f"Current Objects: {rom_composite.get_objects()}"
        )


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRomComposite)
    runner = unittest.TextTestRunner()
    runner.run(suite)
