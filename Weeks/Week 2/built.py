class Text(str):
    def duplicate(self):
        return self
    


class TrackableList(list):   
    def append(self, object):
        print(f"Appending {object} to the list")
        super().append(object)


List - TrackableList()
List.append(1)   
