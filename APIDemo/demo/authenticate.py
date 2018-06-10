# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

# from course_plan.models.teacher import Teacher
# from course_plan.models.student import Student
from demo.models.user import User


class Authenticate:
    """
    Customizing authentication
    """

    def authenticate(self, request, username=None, password=None):
        # user = get_user_model().objects.get(username=username)
        user = get_user_model().objects.filter(username=username).first()
        # print('login_user_auth:{}'.format(user))
        if user and user.password == password:
            return user
        return None

    def get_user(self, user_id):
        try:
            login_user = User.objects.filter(pk=user_id).first()
            # login_user = Teacher.objects.filter(pk=user_id).first()
            # if not login_user:
            #     login_user = Student.objects.filter(pk=user_id).first()
            # if not login_user:
            #     login_user = get_user_model().objects.filter(
            #         pk=user_id).first()
            # print('login_user:{}'.format(login_user))
            return login_user
        except Exception as ex:
            print('ex:{}'.format(ex))
            return None
