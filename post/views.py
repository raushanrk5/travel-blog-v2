from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import PostForm
from .models import Post, Category, EditorsChoice, Comment, Contact
from taggit.models import Tag
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  PIL import Image

from django.core.mail import send_mail

def articles(request, slug=None):
    keyword = request.GET.get("keyword")
    tags = Tag.objects.all()
    if keyword:
        print(keyword)
        object_list = Post.objects.filter(title__contains=keyword)


    elif slug!=None:
        category = get_object_or_404(Category, category_slug=slug)
        object_list = category.posts.all()

    else:
        object_list = Post.objects.all()

    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    editors_choices = EditorsChoice.objects.all()

    latest_posts = Post.objects.all().order_by('-created_date')

    return render(request, "articles.html", {"articles": posts, "tags": tags, "categories": categories, "editors_choices":editors_choices, "latest_posts": latest_posts})


def index(request):
    return render(request, "index.html")


def about(request):
    categories = Category.objects.all()
    return render(request, "about.html", {"categories": categories})


@login_required(login_url="user:login")
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    categories = Category.objects.all()
    context = {"articles": posts, "categories": categories}
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def add_article(request):
    form = PostForm(request.POST, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.slug = slugify(article.title)
        article.author = request.user
        article.save()

        messages.success(request, "The article was created successfully")
        return redirect("post:dashboard")
    categories = Category.objects.all()
    return render(request, "addarticle.html", {"form": form, "categories":categories})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created_date')[:4]

    categories = Category.objects.all()

    editors_choices = EditorsChoice.objects.all()
    return render(request, "detail.html", {"post": post, "comments": comments, 'similar_posts': similar_posts, "categories": categories, "editors_choices": editors_choices})


@login_required(login_url="user:login")
def update_article(request, slug):
    article = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "The article has been updated successfully")
        return redirect("post:dashboard")
    categories = Category.objects.all()
    return render(request, "update.html", {"form": form, "categories":categories})


@login_required(login_url="user:login")
def delete_article(request, slug):
    article = get_object_or_404(Post, slug=slug)
    article.delete()
    messages.success(request, "Article Successfully Deleted")
    return redirect("post:dashboard")


def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        email = request.POST.get("email")
        print(email)
        new_comment = Comment(comment_author=comment_author, comment_content=comment_content, email=email)
        new_comment.post = post
        print(new_comment)
        new_comment.save()
    return redirect(reverse("post:detail", kwargs={"slug": slug}))


def show_categories(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'category.html', {"categories": categories})

def gallery(request):
    posts = Post.objects.all()
    print(posts)
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'posts': posts, "categories": categories})


def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        email_subject = f'New contact {email}: {subject}'
        email_message = message
        send_mail(email_subject, email_message, "kumarraushanrk5@gmail.com", ["punnu2422@gmail.com",])
        return render(request, 'contact_success.html', {"categories": categories})
    return render(request, 'contact.html', {"categories": categories})

