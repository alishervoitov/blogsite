# Generated by Django 4.0.1 on 2022-01-11 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('react', models.CharField(blank=True, max_length=10, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='blog.article')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacts', to='blog.person')),
            ],
        ),
    ]
