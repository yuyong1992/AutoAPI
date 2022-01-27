# 自定义异常处理
from django.db import DatabaseError
from rest_framework.views import exception_handler
from rest_framework.views import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotAuthenticated, MethodNotAllowed


# 将仅针对由引发的异常生成的响应调用异常处理程序。它不会用于视图直接返回的任何响应
# 需要在setting中配置这个异常处理方法,并且异常返回的response对象还会传到默认返回的json的renderer类中，在setting中drf配置中的DEFAULT_RENDERER_CLASSES
# 如果未声明，会采用默认的方式，如下
#
# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
# }
# 下面是我配置的已经自定义的处理
# REST_FRAMEWORK = {
#     # 全局配置异常模块
#     'EXCEPTION_HANDLER': 'utils.exception.custom_exception_handler',
#     # 修改默认返回JSON的renderer的类
#     'DEFAULT_RENDERER_CLASSES': (
#         'utils.custom_render.CustomRender',
#     ),
# }
def custom_exception_handler(exc, context):
    # 先调用REST framework默认的异常处理方法获得标准错误响应对象
    response = exception_handler(exc, context)
    # raise exc
    # print(exc)  # 错误原因   还可以做更详细的原因，通过判断exc信息类型
    # print(context)  # 错误信息
    # print('1234 = %s - %s - %s' % (context['view'], context['request'].method, exc))
    # print(response)

    # 如果response响应对象为空，则设置message这个key的值，并将状态码设为500
    # 如果response响应对象不为空，则则设置message这个key的值，并将使用其本身的状态码
    if response is None:
        if isinstance(exc, ZeroDivisionError):
            return Response({'errmsg': '除数不能为零 {exc}'.format(exc=exc)})
        if isinstance(exc, DatabaseError):
            print(exc)
            return Response({'errmsg': '数据库错误！{exc}'.format(exc=exc)})
        else:
            return Response({
                'errmsg': '服务器错误:{exc}'.format(exc=exc)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)

    else:
        # raise exc
        if isinstance(exc, NotAuthenticated):
            return Response({
                'errmsg': '没有权限:{exc}'.format(exc=exc)
            }, status=response.status_code, exception=True)
        if isinstance(exc, ValidationError):
            # raise exc
            return Response({
                'errmsg': '验证未通过:{exc}'.format(exc=exc)
            }, status=response.status_code, exception=True)
        if isinstance(exc, MethodNotAllowed):
            return Response({
                'errmsg': '不支持的方法:{exc}'.format(exc=exc)
            }, status=response.status_code, exception=True)
        else:
            # raise exc
            return Response({
                'errmsg': '未知异常:{exc}'.format(exc=exc)
            }, status=response.status_code, exception=True)
