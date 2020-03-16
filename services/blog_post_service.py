from FlaskLearning.model.in_memory_store import InMemoryStore
from FlaskLearning.model.entities.blog_post_mapper import BlogPostMapper
from FlaskLearning.services.blog_post_service_iface import BlogPostServiceInterface
from FlaskLearning.model.dbstore.db_repo import BlogPostDbRepository
class BlogPostService(BlogPostServiceInterface):
    def __init__(self, storage):
        self._storage = storage

    def blogPostsCount(self):
        return self._storage.getBlogPostsCount()
    
    def authorsCount(self):
        return self._storage.getAuthorsCount()

    def siteName(self):
        return "Super Blogzz"


    def addBlogPost(self, newPostDto):
        mapper = BlogPostMapper()
        newblogPost = mapper.fromDtoToEntity(newPostDto)
        addedBlogPost = self._storage.addBlogPost(newblogPost)
        return mapper.fromEntityToDto(addedBlogPost)

    def getAllBlogPosts(self):
        mapper = BlogPostMapper()
        allPostsDto = map( mapper.fromEntityToDto, self._storage.getAllBlogPosts())
        return allPostsDto
        
    def getBlogPostById(self, id):
        mapper = BlogPostMapper()
        blogPost = self._storage.getBlogPostById(id)
        return mapper.fromEntityToDto(blogPost)
    
    def updateBlogPost(self, toUpdateBlogPost):
        return self._storage.updateBlogPost(toUpdateBlogPost)
    
    def deleteBlogPost(self, id):
        return self._storage.removeBlogPost(id)