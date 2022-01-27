from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            msg = 'success'
            code = 1000
            total = len(data)
            result = data
            # 判断实例的类型，返回的数据可能是列表也可能是字典
            if isinstance(data, dict):
                msg = data.pop('msg', 'success')
                code = data.pop('code', 1000)
                total = data.pop('count', 0)
                result = data.pop('data', data)
                # 如果返回的data中包含 errmsg 字段，重新构建返回的JSON字典
                if 'errmsg' in data.keys():
                    # print(type(data))
                    msg = data['errmsg']
                    result = ''
                    code = 2000

            # 自定义返回数据格式
            ret = {
                'msg': msg,
                'code': code,
                'total': total,
                'data': result
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
