"""
bridge patter
Using the bridge pattern is a good idea when you want to share an implementation among multiple objects. Basically, instead of implementing several specialized classes, defining all that is required within each class, you can define the following special components:
An abstraction that applies to all the classes
A separate interface for the different objects involved

"""

from abc import ABCMeta, abstractmethod

class ResourceContent:
    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(parth)


class ResourceContentFetcher(metaclass=ABCMeta):
    """
       Define the interface for implementation classes that fetch content.
    """

    @abstractmethod
    def fetch(self, path):
        pass

# implementation of these interfaces

class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


## similarly you can have multiple implementation of ResourceContentFetcher interface


def main():
    url_fetcher =  URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

