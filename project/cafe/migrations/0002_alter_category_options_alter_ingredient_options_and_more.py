# Generated by Django 4.2.7 on 2023-12-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Кількість', 'verbose_name_plural': 'Кількість'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Ціна', 'verbose_name_plural': 'Ціна'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Інгредіент'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=255, verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=255, verbose_name='Замовник'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='cafe.item', verbose_name='Ваше замовлення:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефону'),
        ),
    ]
