#The prototype pattern is useful when one needs to create objects based on an existing object by using a cloning technique.

import copy


class Website:
    def __init__(self, name, domain, description, author, **kwargs):
        '''
        Examples of optional attributes (kwargs):
              category, creation_date, technologies, keywords.
        '''

        self.name = name
        self.domain = domain
        self.description = description
        self.author = author

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        summary = [f'Website "{self.name}"\n',]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')
        return ''.join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj
    def unregister(self, indetifier):
        del self.objects[identifier]


    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrecnt object identifier")
        obj = copy.deepcopy(found)

        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj

