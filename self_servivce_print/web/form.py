from django.forms import Form
from django.forms import fields


class Add_Form(Form):
    pro_name = fields.CharField(
        error_messages={'required': '项目名不能为空!', "max_length":'最多只能32个字符', },
        max_length=32
    )

    team_leader = fields.CharField(
        error_messages={'required': '负责人不能为空!', "max_length":'最多只能32个字符'},
        max_length=32
    )
    summary = fields.CharField(
        error_messages={'required': '简介不能为空!', "max_length":'最多只能64个字符'},
        max_length=64
    )
    content = fields.CharField(
        error_messages={'required': '项目详情不能为空!'}
    )
    comments = fields.CharField(
        error_messages={'required': '备注不能为空!', "max_length": '最多只能64个字符'}
    )