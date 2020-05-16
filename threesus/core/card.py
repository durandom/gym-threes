class Card(object):

    value = None
    unique_id = None

    def __init__(self, value, unique_id):
        self.value = value
        self.unique_id = unique_id
        
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)