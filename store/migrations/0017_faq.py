# Generated by Django 4.1.2 on 2023-04-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(blank=True, max_length=500, null=True)),
                ('ans', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]