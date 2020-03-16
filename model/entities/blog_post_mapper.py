from FlaskLearning.model.entities.blog_post import BlogPost
from FlaskLearning.model.entities.blog_post_dto import BlogPostDto
import base64
class BlogPostMapper:
    def fromEntityToDto(self, entity):
        return BlogPostDto(entity.getId(), entity.getTitle(), entity.getText(), entity.getAuthorName())
    
    def fromDtoToEntity(self, dto):
        return BlogPost(dto.getTitle(), dto.getText(), dto.getAuthorName())
