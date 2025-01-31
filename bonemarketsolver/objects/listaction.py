__all__ = ['ListAction']
__author__ = "Jeremy Saklad"

import argparse
from functools import reduce

from ..data.adjustments import Adjustment
from ..data.appendages import Appendage
from ..data.buyers import Buyer
from ..data.declarations import Declaration
from ..data.embellishments import Embellishment
from ..data.skulls import Skull
from ..data.torsos import Torso

class ListAction(argparse.Action):
    """Lists enumerations referenced by provided strings then exits"""

    list_options = [enum.__name__.lower() for enum in [
                Torso,
                Skull,
                Appendage,
                Adjustment,
                Declaration,
                Embellishment,
                Buyer,
            ]]

    def __init__(self, **kwargs):
        nargs = kwargs.get('nargs')
        default = kwargs.get('default')

        super(ListAction, self).__init__(**kwargs)

        self._nargs = nargs
        self._default = default

    @staticmethod
    def printable_list(enum):
        def printable_item(member):
            return f"\n\t{enum.__name__}.{member.name}:\n\t\t{member}"

        return "{}:{}".format(enum.__name__, str().join([printable_item(member) for member in enum]))

    def __call__(self, parser, namespace, values, option_string=None):
        # Check whether this is a single value or a list of them
        if self._nargs is None or self._nargs == argparse.OPTIONAL:
            # Convert value into an Enum type and print
            print(self.printable_list(globals()[values.capitalize()]))
        else:
            # Convert values back into Enum types and print
            print(*[self.printable_list(globals()[value.capitalize()]) for value in (values if values else self._default)], sep="\n\n")

        parser.exit()
