# vim: expandtab tabstop=4 shiftwidth=4

import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

import minnow

class TestDataMetadataPair(unittest.TestCase):
    def test_instantiation(self):
        dmd = minnow.DataMetadataPair(Path('/foo'), Path('/foo.properties'))
        print(dmd)

    def test_list_pairs_at_path(self):
        with TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            base_names = ['foo', 'bar', 'baz']

            for name in base_names:
                temp_dir.joinpath(name).touch()
                temp_dir.joinpath(name+'.properties').touch()

            # throw in a couple unpaired files
            temp_dir.joinpath('roger').touch()
            temp_dir.joinpath('shrubber.properties').touch()

            pairs = minnow.list_pairs_at_path(temp_dir)
            self.assertEqual(len(pairs), 3)

            found = {k:False for k in base_names}

            for pair in pairs:
                found[pair.data_path.name] = True

            self.assertTrue(all(found.values()))

    def test_empty_extension(self):
        self.assertRaises(minnow.MinnowPathException, minnow.list_pairs_at_path, Path('/tmp'), '')

    def test_non_dot_extension(self):
        self.assertRaises(minnow.MinnowPathException, minnow.list_pairs_at_path, Path('/tmp'), 'foo')
