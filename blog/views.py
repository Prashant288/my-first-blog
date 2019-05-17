from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Contents ,Question ,Comment
from .forms import *
from .admin import QuestionAdmin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def send(request):

    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    category_list = Contents.objects.order_by('id').reverse()[:5]
    context_dict = {'categories': category_list}


    return render_to_response('index.html', context_dict, context)

from django.shortcuts import get_object_or_404, render


def detail(request, question_id):
    question = get_object_or_404(Contents, pk=question_id)
    comments = Comment.objects.filter(post=question).order_by('id').reverse()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=question, user=request.user,content=content)
            comment.save()
            return HttpResponseRedirect(question.get_absolute_url())
    else:
        comment_form= CommentForm()
    return render(request, 'detail.html', {'question': question,'comments': comments, 'comment_form':comment_form,})

def search_form(request):
    return render(request, 'search.html')


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Contents.objects.filter(title__icontains=q)
            return render(request, 'results.html', {'books': books, 'query': q})
    return render(request, 'search.html', {'error': error})

def jan(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/jan.html', {'fiters': fiters})

def feb(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/feb.html', {'fiters': fiters})

def mar(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/mar.html', {'fiters': fiters})

def apr(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/apr.html', {'fiters': fiters})

def may(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/may.html', {'fiters': fiters})

def jun(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/jun.html', {'fiters': fiters})

def jul(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/jul.html', {'fiters': fiters})

def aug(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/aug.html', {'fiters': fiters})

def sep(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/sep.html', {'fiters': fiters})

def oct(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/oct.html', {'fiters': fiters})

def nov(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/nov.html', {'fiters': fiters})

def dec(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'month/dec.html', {'fiters': fiters})

def world(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/World.html', {'fiters': fiters})

def india(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/India.html', {'fiters': fiters})

def business(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Business.html', {'fiters': fiters})

def culture(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Culture.html', {'fiters': fiters})

def design(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Design.html', {'fiters': fiters})

def health(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Health.html', {'fiters': fiters})

def opinion(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Opinion.html', {'fiters': fiters})

def politics(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Politics.html', {'fiters': fiters})

def science(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Science.html', {'fiters': fiters})

def style(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Style.html', {'fiters': fiters})

def technology(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Technology.html', {'fiters': fiters})

def travel(request):
    fiters = Contents.objects.order_by('id').reverse()
    return render(request, 'tag/Travel.html', {'fiters': fiters})

def subscribe(request):
    category_list = Contents.objects.order_by('id').reverse()[:5]
    return render(request, 'home.html/',{'category_list': category_list})



def nextpage2(request):
    category_list = Contents.objects.order_by('id').reverse()[5:10]
    return render(request, 'page/page2.html/',{'category_list': category_list})

def nextpage3(request):
    category_list = Contents.objects.order_by('id').reverse()[10:15]
    return render(request, 'page/page3.html/',{'category_list': category_list})

def nextpage4(request):
    category_list = Contents.objects.order_by('id').reverse()[15:20]
    return render(request, 'page/page4.html/',{'category_list': category_list})

def nextpage5(request):
    category_list = Contents.objects.order_by('id').reverse()[20:25]
    return render(request, 'page/page5.html/',{'category_list': category_list})

def nextpage6(request):
    category_list = Contents.objects.order_by('id').reverse()[25:30]
    return render(request, 'page/page6.html/',{'category_list': category_list})

def nextpage7(request):
    category_list = Contents.objects.order_by('id').reverse()[30:35]
    return render(request, 'page/page7.html/',{'category_list': category_list})

def nextpage8(request):
    category_list = Contents.objects.order_by('id').reverse()[35:40]
    return render(request, 'page/page8.html/',{'category_list': category_list})

def nextpage9(request):
    category_list = Contents.objects.order_by('id').reverse()[40:45]
    return render(request, 'page/page9.html/',{'category_list': category_list})

def nextpage10(request):
    category_list = Contents.objects.order_by('id').reverse()[45:50]
    return render(request, 'page/page10.html/',{'category_list': category_list})
