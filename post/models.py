from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    category_slug = models.SlugField(unique=True, max_length=100, default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,  verbose_name="Writer")
    title = models.CharField(max_length=200, verbose_name="Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    article_image = models.ImageField(upload_to='images/', verbose_name="Add image", null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post", related_name="comments")
#     comment_author = models.CharField(max_length=50, verbose_name="Name")
#     comment_content = models.CharField(max_length=200, verbose_name="Comment")
#     comment_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.comment_content
#
#     class Meta:
#         ordering = ['-comment_date']


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, verbose_name="Post", related_name='comments')
    email = models.EmailField(max_length=80, verbose_name="Email")
    comment_author = models.CharField(max_length=70, verbose_name="Name")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment_content


class EditorsChoice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email