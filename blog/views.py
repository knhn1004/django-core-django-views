from django.http import request
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostModelForm
from blog.models import PostModel


#@login_required(login_url='/login/')
def post_model_list_view(req):
    qs = PostModel.objects.all()

    print(qs)
    #return HttpResponse('some data')
    template = "list-view.html"
    context = {"object_list": qs}

    #if (req.user.is_authenticated):
    #    print('logged in')
    #    template = "list-view.html"
    #else:
    #    print('not logged in')
    #    #template_path = "list-view-public.html"
    #    return HttpResponseRedirect("/login")
    #    #raise Http404

    return render(req, template, context)


def post_model_detail_view(req, id=None):
    print("keyword: ", id)
    #obj = PostModel.objects.get(id=1)

    #try:
    #    obj = PostModel.objects.get(id=100)
    #except:
    #    raise Http404

    #qs = PostModel.objects.filter(id=100)
    #if not qs.exists() and qs.count() != 1:
    #    raise Http404
    #else:
    #    obj = qs.first()

    obj = get_object_or_404(PostModel, id=id)
    context = {"object": obj}
    template = "detail-view.html"

    return render(req, template, context)


def post_model_create_view(req):

    #if req.method == 'POST':
    #    print(req.POST)
    #    form = PostModelForm(req.POST)
    #    if form.is_valid():
    #        form.save(commit=False)
    #        print(form.cleaned_data)

    form = PostModelForm(req.POST or None)

    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        print(form.cleaned_data)

        obj.save()
        messages.success(req, 'Created a new blog post!')
        #return HttpResponseRedirect('/blog/{id}'.format(id=obj.id))
        context = {'form': PostModelForm()}

    template = 'create-view.html'
    return render(req, template, context)


def post_model_update_view(req, id):

    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(req.POST or None, instance=obj)
    #context = {'form': form, 'post': obj}
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        print(form.cleaned_data)

        obj.save()
        messages.success(req, 'Updated a blog post!')
        #context = {
        #    'form': PostModelForm(instance=obj),
        #    'post': obj,
        #}
        context = {
            'form': PostModelForm(instance=obj),
        }

    template = 'update-view.html'
    return render(req, template, context)


def post_model_delete_view(req, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if req.method == 'POST':
        obj.delete()
        messages.success(req, 'post deleted successfully!')
        return HttpResponseRedirect('/blog/')
    context = {'object': obj}
    template = 'delete-view.html'
    return render(req, template, context)