# Generated by Django 3.1.3 on 2023-05-08 08:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('curr_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=1000)),
                ('lot_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('seller_photo', models.ImageField(upload_to='photos/seller/%Y/%m/%d/')),
                ('contact_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('lot_id', models.IntegerField()),
                ('Wishlisted_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timecap', models.DateTimeField(auto_now_add=True)),
                ('price', models.TextField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='aunctionItem.auction')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_messsages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('product_name', models.CharField(db_index=True, max_length=200)),
                ('is_live', models.BooleanField(default=False)),
                ('base_price', models.IntegerField(default=0.0)),
                ('current_price', models.IntegerField(default=0.0)),
                ('description', models.CharField(max_length=500)),
                ('main_photo', models.ImageField(upload_to='photos/main/%Y/%m/%d/')),
                ('photo1', models.ImageField(blank=True, upload_to='photos/optional/%Y/%m/%d/')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/optional/%Y/%m/%d/')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/optional/%Y/%m/%d/')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/optional/%Y/%m/%d/')),
                ('is_trending', models.BooleanField(default=False)),
                ('on_banner', models.BooleanField(default=False)),
                ('year_published', models.DateTimeField(default=datetime.datetime(2023, 5, 8, 8, 47, 36, 386385))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lots', to='aunctionItem.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aunctionItem.seller')),
            ],
            options={
                'ordering': ('product_name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auction', to='aunctionItem.lot'),
        ),
    ]
