from django.http import HttpResponse
from django.http.response import HttpResponseRedirect

#def home(req):
#    #print(req)
#    #print(dir(req))
#    #print(req.method)
#    #print(req.is_ajax)
#    #print(req.is_ajax())
#    print(req.get_full_path())
#    return HttpResponse("<h1>Hello World</h1>")


def home(req):
    #res.write('<p>Page Not Found</p>')
    #res.content = 'some new content'

    #res = HttpResponse(content_type='application/json')
    #res.content = '''
    #{
    #    "test": "hello world!"
    #}
    #'''

    res = HttpResponse(content_type='text/html')
    res.content = 'hello world!'

    res.status_code = 200

    return res


def redirect_somewhere(req):
    return HttpResponseRedirect('https://chunhongweb.com')