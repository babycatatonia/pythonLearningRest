import uuid
class BlogPost:
    def __init__(self, title, text, authorName, id=None):
        #if not isinstance(client, Person):
            #return #TODO: raise an event
        if id == None:
            self._id = str(uuid.uuid1())
        else:
            self._id = id
            
        self._title = title
        self._text = text
        self._authorName = authorName

    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def getText(self):
        return self._text

    def getAuthorName(self):
        return self._authorName

