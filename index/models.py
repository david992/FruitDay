from django.db import models

# Create your models here.
# 创建用户
class User(models.Model):
  uphone=models.CharField(max_length=11,verbose_name="联系方式")
  upwd=models.CharField(max_length=20,verbose_name="密码")
  uname=models.CharField(max_length=30,verbose_name="用户名")
  uemail=models.EmailField(verbose_name="邮箱")
  isActive=models.BooleanField(default=True,verbose_name="活跃状态")

  def __str__(self):
    return self.uname

  class Meta:
    db_table = 'user'
    verbose_name="用户"
    verbose_name_plural=verbose_name


class GoodsType(models.Model):
  title = models.CharField(max_length=20,verbose_name='类型标题')
  picture = models.ImageField(upload_to='static/upload/goodstype',
                              null=True,verbose_name="类型图片")
  desc = models.TextField(verbose_name='类型描述')

  def __str__(self):
    return self.title

  def to_dict(self):
    dic = {
      'title':self.title,
      'picture':self.picture.__str__(),
      'desc':self.desc,
    }
    return dic

  class Meta:
    db_table = "goods_type"
    verbose_name = "商品类型"
    verbose_name_plural = verbose_name


class Goods(models.Model):
  title = models.CharField(max_length=40,verbose_name='商品名称')
  price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
  spec = models.CharField(max_length=20,verbose_name='商品规格')
  picture = models.ImageField(upload_to='static/upload/goods',
                              null=True,verbose_name='商品图片')
  goodsType = models.ForeignKey(GoodsType,on_delete=models.CASCADE,verbose_name='商品类型')
  isActive = models.BooleanField(default = True,verbose_name='是否上架')

  def __str__(self):
    return self.title

  class Meta:
    db_table = "goods"
    verbose_name = "商品"
    verbose_name_plural = verbose_name

class CartInfo(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
  goods = models.ForeignKey(Goods,on_delete=models.CASCADE,db_column='goods_id')
  ccount = models.IntegerField(db_column='ccount')

  def __str__(self):
    return self.ccount

  class Meta:
    db_table = 'cart_info'









