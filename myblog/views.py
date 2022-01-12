from django.shortcuts import render, get_object_or_404
from .models import Post,Profile,Comment
from .forms import PostForm,Category
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context

def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    context = {
        'cats'              : cats,
        'category_post'     : category_post
    }
    return render(request, 'category_view.html', context)

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cats_menu"] = cats_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_message = 'Post successful created'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context 

class CommentCreateView(SuccessMessageMixin, CreateView):
    model = Comment
    # form_class = PostForm
    template_name = 'create_comment.html'
    fields = '__all__'
    # success_message = 'Post successful created'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context

class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    success_message = 'Post Successful Deleted'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context["cats_menu"] = cats_menu
        return context



