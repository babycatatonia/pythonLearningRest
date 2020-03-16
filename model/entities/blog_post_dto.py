class BlogPostDto:
    def __init__(self, id=None, title=None, text=None, authorName=None ):
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
    
    def serialize(self):
        return {"id": self._id,
                "title": self._title,
                "text": self._text,
                "authorName": self._authorName}

