from django.shortcuts import redirect, render

def authenticated_user_only(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper


def unauthenticated_user_only(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper