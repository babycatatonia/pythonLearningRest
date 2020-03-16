from FlaskLearning.model.entities.blog_post import BlogPost
from FlaskLearning.model.entities.blog_post_mapper import BlogPostMapper
from FlaskLearning.model.blog_post_repo_iface import BlogPostRepoInterface
class InMemoryStore(BlogPostRepoInterface):
    def __init__(self):
        self._blogPosts = []
        self._initPopulation()
    
    def addBlogPost(self, blogPost):
        self._blogPosts.append(blogPost)
        return blogPost

    def addBlogPosts(self, blogPostList):
        self._blogPosts.append(blogPostList)

    def removeBlogPost(self, id):
        everyBlogPostIdList = list(map(lambda bp: bp.getId(), self._blogPosts))
        if id not in everyBlogPostIdList:
            return False
        self._blogPosts = list(filter(lambda  bp: bp.getId() != id, self._blogPosts))
        return True
    
    def updateBlogPost(self, toUpdateBlogPost):
        everyBlogPostIdList = list(map(lambda bp: bp.getId(), self._blogPosts))
        id = toUpdateBlogPost.getId()
        if id not in everyBlogPostIdList:
            return False
        self._blogPosts = list(filter(lambda  bp: toUpdateBlogPost.getId() != bp.getId(), self._blogPosts))
        self._blogPosts.append(toUpdateBlogPost)
        return True
        

    def getAllBlogPosts(self):
        return self._blogPosts

    def getBlogPostsCount(self):
        return len(self._blogPosts)

    def getAuthorsCount(self):
        authors = set()
        for blogPost in self._blogPosts:
            authors.add(blogPost.getAuthorName())
        return len(authors)

    def getBlogPostById(self, id):
        for blogPost in self._blogPosts:
            if blogPost.getId() == id:
                return blogPost
    
    def _initPopulation(self):
        self._blogPosts = [
        BlogPost("Uptown Girl Blouse","Sociosqu facilisis duis ...", "Stefan Bubanj"),
        BlogPost("Entity Apparel","Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "Stefan Nikolic"),
        BlogPost("Simply Sweet Blouse","Donec eget leo eget mauris tristique tincidunt.", "Stefan R. Bubanj"),
        BlogPost("On Cloud Nine Pillow","Phasellus mattis orci eget iaculis pellentesque.", "Stefan Bubanj III"),
        BlogPost("Knock Your Socks Off Lace-Up Heels","Curabitur faucibus quis lorem ac aliquam.", "Stefan Bubanj"),
        ]