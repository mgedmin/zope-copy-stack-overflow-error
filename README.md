# Debugging stack overflow errors when copying large collections with zope.copy

The error showed up while using zope.copy on a BTreeContainer subclass
containing over 9000 EmailMessage objects, which are simple objects inheriting
from Persistent and Contained, with only string attributes.

The error was RuntimeError: maximum recursion depth exceeded

Run tox to reproduce the problem.
