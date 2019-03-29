from django.shortcuts import render, HttpResponse,redirect
from django.forms import Form
from django.forms import fields
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from status.models import User, Department
import json
import uuid


class Reg_Form(Form):
    username = fields.CharField(max_length=32,
                                error_messages={'required': '用户名不能为空!',
                                                "max_length": '最多只能32个字符！', },
                                ),
    password1 = fields.CharField(max_length=11, min_length=6,
                                 validators=[RegexValidator(r'^(?=.*[a-zA-Z\d])[!-~]{6,11}$')],
                                 error_messages={'required': '不能为空!',
                                                "max_length": '最多只能11个字符！',
                                                "min_length": '最少6个字符！',
                                                "invalid": "密码必须包含数字，字母或特殊字符。",
                                                },)
    password2 = fields.CharField(error_messages={'required': '不能为空!', })
    email = fields.EmailField(error_messages={'required': '不能为空!', 'invalid': '格式错误！'},)
    department = fields.CharField(error_messages={'required': '不能为空!'})

    def clean(self):
        pwd1 = self.cleaned_data.get('password1')
        pwd2 = self.cleaned_data.get('password2')
        if pwd1 == pwd2:
            department_num = self.cleaned_data.get('department')
            if not Department.objects.filter(department=department_num):
                raise ValidationError('没有工号', 'invalid')
            else:
                pass
        else:
            raise ValidationError('两次密码不一样', 'invalid')

def login(request):
    if request.method == "GET":
        return render(request, 'status/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = User.objects.filter(email=email)[0]
        if obj:
            if password == obj.password:
                request.session['uuid'] = str(uuid.uuid4())
                request.session["is_login"] = True
                return redirect('/home.html')
            else:
                return render(request, 'status/login.html')
        else:
            return render(request, 'status/login.html')


def register(request):
    if request.method == "GET":
        obj = Reg_Form()
        return render(request, 'status/register.html', {"obj": obj})

    else:
        ret = {"status": False, "msg": None}
        obj = Reg_Form(request.POST)
        if obj.is_valid():
            ret['status'] = True
            username = request.POST.get('username')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            department = request.POST.get('department')
            nid = Department.objects.filter(department=department)[0].id
            User.objects.create(username=username, password=password2, email=email, UD_id=nid)
        else:
            ret['msg'] = obj.errors
        return HttpResponse(json.dumps(ret))


def logout(request):
    request.session.clear()
    return render(request, 'status/login.html')
