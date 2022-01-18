# Generated by Django 1.11.13 on 2018-09-07 11:06
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("djangocms_moderation", "0003_auto_20180903_1206")]

    operations = [
        migrations.AlterField(
            model_name="moderationrequest",
            name="is_active",
            field=models.BooleanField(
                db_index=True, default=False, verbose_name="is active"
            ),
        ),
        migrations.AlterField(
            model_name="moderationrequest",
            name="version",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="djangocms_versioning.Version",
                verbose_name="version",
            ),
        ),
    ]
