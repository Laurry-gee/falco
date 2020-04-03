# Generated by Django 3.0.3 on 2020-04-03 08:56

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


def create_default_metrics_preferences(apps, schema_editor):
    MetricsPreferences = apps.get_model("projects", "MetricsPreferences")
    Projects = apps.get_model("projects", "project")
    for row in Projects.objects.all():
        for member in row.members.all():
            MetricsPreferences.objects.create(
                project_id=row.uuid,
                user_id=member.id,
                metrics=[
                    "WPTMetricFirstViewTTI",
                    "WPTMetricFirstViewSpeedIndex",
                    "WPTMetricFirstViewLoadTime",
                ]
            )


def delete_metrics_preferences(apps, schema_editor):
    MetricsPreferences = apps.get_model("projects", "MetricsPreferences")
    MetricsPreferences.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0031_auto_20191122_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetricsPreferences',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('metrics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('WPTMetricFirstViewTTI', 'WPTMetricFirstViewTTI'), ('WPTMetricRepeatViewTTI', 'WPTMetricRepeatViewTTI'), ('WPTMetricFirstViewSpeedIndex', 'WPTMetricFirstViewSpeedIndex'), ('WPTMetricRepeatViewSpeedIndex', 'WPTMetricRepeatViewSpeedIndex'), ('WPTMetricFirstViewFirstPaint', 'WPTMetricFirstViewFirstPaint'), ('WPTMetricRepeatViewFirstPaint', 'WPTMetricRepeatViewFirstPaint'), ('WPTMetricFirstViewFirstMeaningfulPaint', 'WPTMetricFirstViewFirstMeaningfulPaint'), ('WPTMetricRepeatViewFirstMeaningfulPaint', 'WPTMetricRepeatViewFirstMeaningfulPaint'), ('WPTMetricFirstViewLoadTime', 'WPTMetricFirstViewLoadTime'), ('WPTMetricRepeatViewLoadTime', 'WPTMetricRepeatViewLoadTime'), ('WPTMetricFirstViewFirstContentfulPaint', 'WPTMetricFirstViewFirstContentfulPaint'), ('WPTMetricRepeatViewFirstContentfulPaint', 'WPTMetricRepeatViewFirstContentfulPaint'), ('WPTMetricFirstViewTimeToFirstByte', 'WPTMetricFirstViewTimeToFirstByte'), ('WPTMetricRepeatViewTimeToFirstByte', 'WPTMetricRepeatViewTimeToFirstByte'), ('WPTMetricFirstViewVisuallyComplete', 'WPTMetricFirstViewVisuallyComplete'), ('WPTMetricRepeatViewVisuallyComplete', 'WPTMetricRepeatViewVisuallyComplete'), ('WPTMetricLighthousePerformance', 'WPTMetricLighthousePerformance')], max_length=100), default=['WPTMetricFirstViewTTI', 'WPTMetricFirstViewSpeedIndex', 'WPTMetricFirstViewLoadTime'], null=True, size=None)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('project', 'user')},
            },
        ),
        migrations.RunPython(
            create_default_metrics_preferences,
            reverse_code=delete_metrics_preferences,
        )
    ]