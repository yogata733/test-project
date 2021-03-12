from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm
# 認証OKの場合にユーザーを有効化するために必要
from django.views.generic import TemplateView
from .forms import activate_user


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# 認証確認用ビュー


class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)
