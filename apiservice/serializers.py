from rest_framework import serializers
from apiservice import models
import re


class CollectionSerializer(serializers.ModelSerializer):

    def validate_name(self, name):
        # 单个字段添加校验
        # 序列化类中重写 validate_fieldname 方法，
        reg = r'^.{1,10}$'
        result = re.match(reg, name)
        if not result:
            raise serializers.ValidationError('name 格式错误')
        return name

    class Meta:
        model = models.Collection
        # fields = '__all__'
        fields = ('id', 'name', 'parent_id', 'description', 'order', 'create_time', 'update_time')


class ApiSerializer(serializers.ModelSerializer):
    # 接口返回外键对应的表中的字段
    # 表中有一个外键 collection表中的id，想要展示collection的name
    # 序列化类中先定义一个collection_name 字段，设置为只读（不设置的话，提交数据时也会校验该字段），source 为外键对应model及字段：model_name.field_name
    # 序列化的元类中自定义增加返回字段fields
    # collection_name = serializers.CharField(read_only=True, source='collection.name')
    # method_name = serializers.CharField(read_only=True, source='method.name')
    # protocol_name = serializers.CharField(read_only=True, source='protocol.name')
    # collection = CollectionSerializer()

    def validate_host(self, host):
        # 单个字段添加校验
        # 序列化类中重写 validate_fieldname 方法，
        reg = r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))'
        result = re.match(reg, host)
        if not result:
            raise serializers.ValidationError('host 格式错误')
        return host

    class Meta:
        model = models.Api
        depth = 1
        # fields = '__all__'
        fields = (
            'id', 'name', 'collection', 'method', 'protocol', 'host',
            'port', 'url', 'header', 'params', 'body', 'status', 'order', 'create_time', 'update_time')
        # validators = []


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Case
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = '__all__'
