# Generated by Django 4.0.3 on 2022-04-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('backer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.backer')),
            ],
            options={
                'db_table': 'fundings',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('end_date', models.CharField(max_length=20)),
                ('backer', models.ManyToManyField(through='products.Funding', to='members.backer')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.publisher')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='funding',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_amount', models.IntegerField()),
                ('amount_per_session', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('total_quantity', models.IntegerField()),
                ('achievement_rate', models.IntegerField()),
                ('total_backers', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'details',
            },
        ),
    ]
