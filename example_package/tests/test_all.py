# an example script for performing tests
# typically all together for coverage reporting and CI

import pandas as pd
from example_package import magic

class Test(unittest.TestCase):

    def setUp(self):

        self.magic = magic.Magic(name='Dumbledore')

    def test_get_name(self):

        self.data = self.magic.get_name()

        self.assertEqual(self.data, 'Dumbledore')

    def test_do_magic(self):

        self.data = self.magic.do_magic()

        self.assertTrue(isinstance(self.data, str))

        self.assertEqual(self.data, 'Dumbledore is doing magic.')

    def test_get_heads(self):

        self.data = self.magic.get_heads()

        self.assertEqual(self.data.columns.tolist(), ['head','shoulders','knees','toes'])

        self.assertTrue(isinstance(self.data, pd.DataFrame))


if __name__ == "__main__":
    unittest.main(verbosity=2)
