# vim: expandtab tabstop=4 shiftwidth=4

import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

import minnow

class TestProperties(unittest.TestCase):
    def test_save_load(self):
        start_props = {'foo': 1, 'bar': 2, 'baz': 'boo', 'robert': 'shrubber', 'duck': True, 'witch': False}

        with TemporaryDirectory() as temp_dir:
            prop_file_path = Path(temp_dir).joinpath('foo.properties')
            minnow.save_properties(start_props, prop_file_path)
            loaded_props = minnow.load_properties(prop_file_path)

            for k, v in start_props.items():
                self.assertTrue(k in loaded_props)

                if k in loaded_props:
                    if type(v) is bool:
                        self.assertEqual(str(v).lower(), loaded_props[k])
                    else:
                        self.assertEqual(str(v), loaded_props[k])
