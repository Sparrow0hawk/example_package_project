# an example class for our package
import numpy as np
import pandas as pd
import pkg_resources

# define the name of package directory with scripts for resource retrieval
resource_package = 'example_package'

class Magic:

    def __init__(self, name):
        # set a class attribute
        self.name = name

    def get_name(self):

        print(self.name)

        return self.name

    def do_magic(self):

        print(self.name +' is doing magic.')

        return self.name +' is doing magic.'

    def get_heads(self):

        # example of retrieving resources from package data folders using pkg_resources
        heads_tbl = pd.read_csv(pkg_resources.resource_filename(resource_package, 'data/test_data.csv'))

        return heads_tbl
