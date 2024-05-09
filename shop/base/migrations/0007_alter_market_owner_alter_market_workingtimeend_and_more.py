# Generated by Django 5.0.3 on 2024-05-09 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='market_owner', to='base.user'),
        ),
        migrations.AlterField(
            model_name='market',
            name='workingTimeEnd',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='workingTimeStart',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_company', to='base.company'),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_currency', to='base.currency'),
        ),
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_market', to='base.market'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_company', to='base.company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_market', to='base.market'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_role', to='base.userrole'),
        ),
    ]
