
#from FlaskLearning.app import BlogPostOrmModel
#from FlaskLearning.model.dbstore.blog_post_model import BlogPostOrmModel

class BlogPostDbRepository():
    def __init__(self, db, ormModel):
        self._db = db
        self._ormModel = ormModel
        self._db.drop_all()
        self._db.create_all()

    def addBlogPost(self, blogPostDto):
        #newBlogPost = BlogPostOrmModel(title=blogPostDto.getTitle(), text=blogPostDto.getText(), authorName=blogPostDto.getAuthorName())
        self._ormModel.id = blogPostDto.getId()
        self._ormModel.title = blogPostDto.getTitle()
        self._ormModel.text = blogPostDto.getText()
        self._ormModel.authorname = blogPostDto.getAuthorName()

       # self._db.session.add(newBlogPost)
        self._db.session.add(self._ormModel)
        self._db.session.commit()
        self._db.session.close()

        return None

    def addBlogPosts(self, blogPostList):
        pass
    def removeBlogPost(self, id):
        pass
    def updateBlogPost(self, toUpdateBlogPost):
        pass
    def getAllBlogPosts(self):
        pass
    def getBlogPostsCount(self):
        pass
    def getAuthorsCount(self):
        pass
    def getBlogPostById(self, id):
        pass
