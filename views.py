from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewsForm, UserRegisterForm
from .models import News, Category
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save
            messages.success(request, 'Ваш аккаунт успешно зарегестрирован')
            return redirect('Login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'News/register.html', {'form': form})


def login(request):
    return render(request, 'News/login.html')


class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['page_obj'] = (Paginator(self.get_queryset(), self.paginate_by).get_page
                               (self.request.GET.get('page')))
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'News/view_news.html'


class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'

# def test(request):
#     objects = ['John', 'Mike', 'Jane', 'George',
#                 'John2', 'Mike2', 'Jane2', 'George2' ]
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'News/test.html', {'page_objects': page_objects})


# def index(request):
#    news = News.objects.all()
#    categories = Category.objects.all()
#    context = {
#        'news': news,
#        'title':'Список новостей',
#    }
#    return render(request,'News/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'News/category.html', context=context)


# def view_news(request, pk):
#     #news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=pk)
#     context = {
#         'news_item': news_item
#     }
#     return render(request, 'news/view_news.html', context=context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
