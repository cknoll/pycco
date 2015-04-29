#!/usr/bin/env python
"""
This is a general docstring of the module.

It can

span


multiple lines.
"""


"""::
This is a reviewer-multiline-String.
It can also span multiple lines.

And it can contain **markdown** formatted text,
like [Links](http://) or `explicitly_featured(source, code)`.

This example source file shows the use case of this review-mod:

Suppose someone asked you for comments (in a general sense) on their code,
you can add review comments (in a technical sense) marked by e.g.  `#::`
instead of just `#` right at the specific location in the source file.
The script extracts them and generates a nicely formated html file with
a split view: reviewer comments right, complete source code left.

Thus, your reviewer comments are much easier to overview and follow than
without the split view.
::"""

# here comes some code
# ordinary comments are left unchanged

import sys
a = "foo"
b = "bar"


def func1(x, y):
    pass
    pass
    pass

    # very interesting code
    pass
    pass
    pass
    pass

    # complicated algorithm
    if 1:
        for i in range(100):
            pass
            pass  # comment 1
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass

            # short comment 2
            #:: This part should be better documented
            pass
            pass
            pass
            pass
            pass
            z = 1 + 1
            #:: IMHO `z = 2 + 2`??

            pass
            pass
    else:
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        # TODO: this should be outsourced to an extra module
        #:: I think `sys.foo.bar` does this already
        pass
        pass
        pass

    return x + y

class MyClass1(object):
    """
    This is the docstring of the class
    """

    def __init__(self, *args, **kwargs):
        pass
        pass
        pass

    @property
    def get1(self):
        #:: This method needs a docstring
        pass
        pass
        pass
        pass
        pass
        return 1

