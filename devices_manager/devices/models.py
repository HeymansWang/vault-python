from django.db import models

# Create your models here.
class DeviceType(models.Model):
    """设备类型"""
    name = models.CharField(max_length=20, verbose_name='类型名称')
    code = models.CharField(max_length=20, verbose_name='类型编码')
    desc = models.CharField(max_length=50, verbose_name='类型描述', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级类型')

    class Meta:
        verbose_name = '设备类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Device(models.Model):
    """设备"""
    name = models.CharField(max_length=20, verbose_name='设备名称')
    code = models.CharField(max_length=20, verbose_name='设备编码')
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, verbose_name='设备类型')
    desc = models.CharField(max_length=50, verbose_name='设备描述', null=True, blank=True)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DeviceInstance(models.Model):
    """设备实例"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='设备')
    code = models.CharField(max_length=20, verbose_name='设备实例编码')
    name = models.CharField(max_length=20, verbose_name='设备实例名称')
    desc = models.CharField(max_length=50, verbose_name='设备实例描述', null=True, blank=True)

    class Meta:
        verbose_name = '设备实例'
        verbose_name_plural = verbose_name