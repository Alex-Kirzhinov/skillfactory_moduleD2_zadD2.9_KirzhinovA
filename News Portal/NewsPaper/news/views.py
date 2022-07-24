from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm, AuthorForm


class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'NW'
        return super().form_valid(form)


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', )
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'AR'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', )
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'NW'
        return super().form_valid(form)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.article_or_news = 'AR'
        return super().form_valid(form)


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class UserUpdate(LoginRequiredMixin, UpdateView):
    form_class = AuthorForm
    model = Author
    template_name = 'author_edit.html'
    success_url = '/posts/'

    def get_object(self, **kwargs):
        return self.request.user