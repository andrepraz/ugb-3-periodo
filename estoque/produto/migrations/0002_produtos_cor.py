# Generated by Django 4.1 on 2022-11-10 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='cor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='produto.cores'),
            preserve_default=False,
        ),
    ]
