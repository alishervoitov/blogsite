from django.shortcuts import redirect
def not_logged(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('articles')
        return func(request,*args,**kwargs)
    return wrapper