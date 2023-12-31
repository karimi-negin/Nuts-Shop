# Generated by Django 4.2.2 on 2023-06-17 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Management', '0006_alter_inventoryproduct_quantity_alter_order_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryproduct',
            name='Inventory',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.product', verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='inventoryproduct',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.inventoryproduct', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ثبت شد', 'ثبت شد'), ('آماده ارسال', 'آماده ارسال')], default='ثبت شد', max_length=20, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='سفارش دهنده'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='مقدار هر بسته به گرم'),
        ),
        migrations.AddField(
            model_name='inventoryproduct',
            name='inventory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Management.inventory', verbose_name='انبار'),
        ),
    ]
