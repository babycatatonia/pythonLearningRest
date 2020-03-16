import unittest
import sys
import os.path
sys.path.append(
os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
print(sys.path)
from model.entities.blog_post import BlogPost



class TestBlogPostEntity(unittest.TestCase):
    def BlogPost_ObjectValidInitialization_CorrectObjectCreated(self):
        #arrange
        title = "TextTitle"
        text = "TextualContent"
        authorName = "Stefan"
        #act
        blogPost = BlogPost(title,text,authorName)
        #assert
        self.assertEqual(blogPost.getTitle(), title)
        self.assertEqual(blogPost.getText(), "8w9er8weryewr9")
        self.assertEqual(blogPost.getAuthorName(), "8w9er8weryewr9")


if __name__ == "__main__":
    unittest.main()
