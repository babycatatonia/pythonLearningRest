from flask import *
from FlaskLearning.model.in_memory_store import InMemoryStore
from FlaskLearning.model.entities.blog_post_dto import BlogPostDto
from FlaskLearning.model.entities.blog_post import BlogPost
from FlaskLearning.services.blog_post_service import BlogPostService
from flask_sqlalchemy import SQLAlchemy
from FlaskLearning.model.dbstore.db_repo import BlogPostDbRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SBUBANJ\MSSQLSERVER14/blogpost_db?trusted_connection=yes&driver=SQL+Server'

db = SQLAlchemy(app)

from FlaskLearning.model.dbstore.blog_post_model import BlogPostOrmModel

service = BlogPostService(BlogPostDbRepository(db, BlogPostOrmModel() ))

@app.route('/')
def index():
    name = service.siteName()
    postsCount = service.blogPostsCount()
    authorsCount = service.authorsCount()
    return f'Hello from {name}!! Site info:  Blog posts count:{postsCount} , Authors count: {authorsCount}'

@app.route('/blogPost', methods=["POST"])
def createBlogPost():
        blogPostDto = BlogPostDto(title=request.form["title"], text=request.form["text"], authorName=request.form["authorName"])
        newPost = service.addBlogPost(blogPostDto)
        toJsonPost = newPost.serialize()
        response = jsonify(toJsonPost)
        response.headers['location'] = '/blogPost/'+newPost.getId()
        response.autocorrect_location_header = False
        return response,201

@app.route('/blogPost', methods=["GET"])
def getAllPosts():
    allPosts = service.getAllBlogPosts()
    prepareJson = []
    for p in allPosts:
        prepareJson.append(p.serialize())
    response = jsonify(prepareJson)
    return response,200

@app.route('/blogPost/<string:id>', methods=["GET"])
def getBlogPostById(id):
    blogPostById = service.getBlogPostById(id)
    response = blogPostById.serialize()
    return response,200 

@app.route('/blogPost/<string:id>', methods=["DELETE"])
def removeBlogPost(id):
    isIdFound = service.deleteBlogPost(id)
    if isIdFound == False:
        return abort(404)
    return jsonify(success=True)

@app.route('/blogPost/<string:id>', methods=["PUT"])
def updateBlogPost(id):
    toUpdateBlogPost = BlogPost(id=id, title=request.form["title"], text=request.form["text"], authorName=request.form["authorName"])
    isIdFound = service.updateBlogPost(toUpdateBlogPost)
    if isIdFound == False:
        return abort(404)
    return jsonify(success=True)







