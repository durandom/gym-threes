class Card(object):

    value = None
    unique_id = None

    def __init__(self, value, unique_id):
        self.value = value
        self.unique_id = unique_id

    def get_merged_with(self, other):
        if self.value == 1:
            if other.value == 2:
                return Card(3, self.unique_id)
        elif self.value == 2:
            if other.value == 1:
                return Card(3, self.unique_id)
        else:
            if other.value == self.value:
                return Card(self.value * 2, self.unique_id)

        return None
        
    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return self.value.__bool__()