from django.urls import path,re_path
from app_admin import views

urlpatterns = [
    path('login/',views.log_in,name='login'),# 登录
    path('logout/',views.log_out,name='logout'),# 注销
    path('register/',views.register,name="register"), # 注册
    path('user_manage/',views.admin_user,name="user_manage"), # 用户管理
    path('create_user/',views.admin_create_user,name="create_user"), # 新建用户
    path('del_user/',views.admin_del_user,name='del_user'), # 删除用户
    path('change_pwd',views.admin_change_pwd,name="change_pwd"), # 管理员修改用户密码
    path('modify_pwd',views.change_pwd,name="modify_pwd"), # 普通用户修改密码
    path('project_manage/',views.admin_project,name='project_manage'), # 文集管理
    path('doc_manage/',views.admin_doc,name='doc_manage'), # 文档管理
    path('doctemp_manage/',views.admin_doctemp,name='doctemp_manage'), # 文档模板管理
    path('setting/',views.admin_setting,name="sys_setting"), # 应用设置
    path('check_code/',views.check_code,name='check_code'), # 注册验证码
    path('forget_pwd/',views.forget_pwd,name='forget_pwd'), # 忘记密码
    path('send_email_vcode/',views.send_email_vcode,name='send_email_vcode'), # 忘记密码发送邮件验证码

]