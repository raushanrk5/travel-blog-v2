from django.contrib import admin
from .models import Post,Category,EditorsChoice, Comment, Contact
# Register your models here.

# admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    prepopulated_fields = {'slug':('title',)}

    class Meta:
        model = Post


admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'email', 'post', 'comment_date', 'active')
    list_filter = ('active', 'comment_date')
    search_fields = ('comment_author', 'email', 'comment_content')


@admin.register(EditorsChoice)
class EditorsChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','post')
    raw_id_fields = ('post',)


admin.site.register(Contact)


