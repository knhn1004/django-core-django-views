from django.contrib.messages.api import success
from django.http import request
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostModelForm
from blog.models import PostModel


def post_model_robust_view(req, id=None):
    """
    Robust View to be DRY (not recommended)
    """
    obj = None
    context = {}
    success_message = 'A new post was created'
    template = 'detail-view.html'

    if id is None:
        template = 'create-view.html'
    else:  # id is not None
        obj = get_object_or_404(PostModel, id=id)
        context['object'] = obj
        if 'edit' in req.get_full_path():
            template = 'update-view.html'
        if 'delete' in req.get_full_path():
            template = 'delete-view.html'
            if req.method == 'POST':
                obj.delete()
                messages.success(req, 'Post Deleted')
                return HttpResponseRedirect('/blog/')

    if 'edit' in req.get_full_path() or 'create' in req.get_full_path():
        form = PostModelForm(req.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(req, success_message)
            if obj is not None:  # updated successfully
                return HttpResponseRedirect('/blog/{id}'.format()(obj.id))
            context['form'] = PostModelForm()

    return render(req, template, context)


#@login_required(login_url='/login/')
def post_model_list_view(req):
    qs = PostModel.objects.all()
    #print(qs)

    #print(req.GET)  # query dict
    #query = req.GET['q']
    query = req.GET.get('q')

    if query:
        qs = qs.filter(title__icontains=query)

    template = "list-view.html"
    context = {"object_list": qs}

    return render(req, template, context)


def post_model_detail_view(req, id=None):
    print("keyword: ", id)

    obj = get_object_or_404(PostModel, id=id)
    context = {"object": obj}
    template = "detail-view.html"

    return render(req, template, context)


def post_model_create_view(req):

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