# vim: expandtab tabstop=4 shiftwidth=4

import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

import minnow

class TestProcessor(unittest.TestCase):
    def test_instantiation(self):
        proc = minnow.Processor(Path('/foo/input'), Path('/foo/output'))
        print(proc)

    def test_run(self):
        with TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            proc = minnow.Processor(temp_dir, Path('/foo/output'))
            proc.run()
