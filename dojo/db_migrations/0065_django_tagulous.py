# Generated by Django 2.2.12 on 2020-04-05 16:35

from django.db import migrations, models
# import django.db.models.deletion
# from tagging.registry import register as tag_register

import tagulous.models.fields
import tagulous.models.models
import logging

logger = logging.getLogger(__name__)


class Migration(migrations.Migration):

    def copy_existing_tags_to_tags_from_django_tagging_field(apps, schema_editor):
        # We can't import the models directly as it may be a newer
        # version than this migration expects. We use the historical version.
        logger.info('Migrating tags from django-tagging to django-tagulous step1. Enable DEBUG logging to find out more.')
        import tagulous.utils
        # for model_name in ['Product']:
        for model_name in ['Product', 'test', 'finding', 'engagement', 'endpoint', 'finding_template', 'app_Analysis', 'objects']:
            model_class = apps.get_model('dojo', model_name)
            # the get_model returns a fake class proxy, which is not registered with django-tagging
            # tag_register(model_class)

            for obj in model_class.objects.all():
                # logger.debug('%s:%s:%s', model_class, obj.id, obj)
                if obj.tags:
                    tags_as_string = tagulous.utils.render_tags(obj.tags.all())
                    logger.debug('%s:%s:%s: found tags: %s', model_class, obj.id, obj, tags_as_string)
                    obj.tags_from_django_tagging = tags_as_string
                    # obj.description = tags_as_string
                    # finding.save() doesn't look at push_all_jira_issue, so we should be good
                    # if model_name == 'finding2':
                    #     obj.save(dedupe_option=False, rules_option=False, issue_updater_option=False, push_to_jira=False)
                    # else:
                    obj.save()

    def copy_tags_from_django_tagging_field_to_new_tagulous_tags_field(apps, schema_editor):
        # We can't import the models directly as it may be a newer
        # version than this migration expects. We use the historical version.
        logger.info('Migrating tags from django-tagging to django-tagulous step2. Enable DEBUG logging to find out more.')
        # for model_name in ['Product']:
        for model_name in ['Product', 'test', 'finding', 'engagement', 'endpoint', 'finding_template', 'app_Analysis', 'objects']:
            model_class = apps.get_model('dojo', model_name)

            for obj in model_class.objects.all():
                # logger.debug('%s:%s:%s', model_class, obj.id, obj)
                if obj.tags_from_django_tagging:
                    logger.debug('%s:%s:%s: found tags: %s', model_class, obj.id, obj, obj.tags_from_django_tagging)
                    obj.tags = obj.tags_from_django_tagging
                    obj.save()

        # raise ValueError('fake error to fail migration')

    dependencies = [
        ('dojo', '0064_jira_refactor_populate'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_analysis',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='finding',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='finding_template',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='objects',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AddField(
            model_name='test',
            name='tags_from_django_tagging',
            field=models.TextField(blank=True, help_text='Temporary archive with tags from the previous tagging library we used'),
        ),
        migrations.AlterField(
            model_name='child_rule',
            name='match_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('cvssv3', 'cvssv3'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('vuln_id_from_tool', 'vuln_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences'), ('tags_from_django_tagging', 'tags_from_django_tagging')], max_length=200),
        ),
        migrations.AlterField(
            model_name='rule',
            name='applied_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('cvssv3', 'cvssv3'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('vuln_id_from_tool', 'vuln_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences'), ('tags_from_django_tagging', 'tags_from_django_tagging')], max_length=200),
        ),
        migrations.AlterField(
            model_name='rule',
            name='match_field',
            field=models.CharField(choices=[('id', 'id'), ('title', 'title'), ('date', 'date'), ('cwe', 'cwe'), ('cve', 'cve'), ('cvssv3', 'cvssv3'), ('url', 'url'), ('severity', 'severity'), ('description', 'description'), ('mitigation', 'mitigation'), ('impact', 'impact'), ('steps_to_reproduce', 'steps_to_reproduce'), ('severity_justification', 'severity_justification'), ('references', 'references'), ('test', 'test'), ('is_template', 'is_template'), ('active', 'active'), ('verified', 'verified'), ('false_p', 'false_p'), ('duplicate', 'duplicate'), ('duplicate_finding', 'duplicate_finding'), ('out_of_scope', 'out_of_scope'), ('under_review', 'under_review'), ('review_requested_by', 'review_requested_by'), ('under_defect_review', 'under_defect_review'), ('defect_review_requested_by', 'defect_review_requested_by'), ('is_Mitigated', 'is_Mitigated'), ('thread_id', 'thread_id'), ('mitigated', 'mitigated'), ('mitigated_by', 'mitigated_by'), ('reporter', 'reporter'), ('numerical_severity', 'numerical_severity'), ('last_reviewed', 'last_reviewed'), ('last_reviewed_by', 'last_reviewed_by'), ('line_number', 'line_number'), ('sourcefilepath', 'sourcefilepath'), ('sourcefile', 'sourcefile'), ('param', 'param'), ('payload', 'payload'), ('hash_code', 'hash_code'), ('line', 'line'), ('file_path', 'file_path'), ('component_name', 'component_name'), ('component_version', 'component_version'), ('static_finding', 'static_finding'), ('dynamic_finding', 'dynamic_finding'), ('created', 'created'), ('scanner_confidence', 'scanner_confidence'), ('sonarqube_issue', 'sonarqube_issue'), ('unique_id_from_tool', 'unique_id_from_tool'), ('vuln_id_from_tool', 'vuln_id_from_tool'), ('sast_source_object', 'sast_source_object'), ('sast_sink_object', 'sast_sink_object'), ('sast_source_line', 'sast_source_line'), ('sast_source_file_path', 'sast_source_file_path'), ('nb_occurences', 'nb_occurences'), ('tags_from_django_tagging', 'tags_from_django_tagging')], max_length=200),
        ),

        migrations.RunPython(copy_existing_tags_to_tags_from_django_tagging_field, migrations.RunPython.noop),

        migrations.CreateModel(
            name='Tagulous_Test_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Product_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Finding_Template_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Finding_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Engagement_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_Endpoint_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Tagulous_App_Analysis_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
                'unique_together': {('slug',)},
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name='app_analysis',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_App_Analysis_tags'),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Endpoint_tags'),
        ),
        migrations.AddField(
            model_name='engagement',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Engagement_tags'),
        ),
        migrations.AddField(
            model_name='finding',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Finding_tags'),
        ),
        migrations.AddField(
            model_name='finding_template',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Finding_Template_tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Product_tags'),
        ),
        migrations.AddField(
            model_name='test',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='dojo.Tagulous_Test_tags'),
        ),

        migrations.RunPython(copy_tags_from_django_tagging_field_to_new_tagulous_tags_field, migrations.RunPython.noop),
    ]
