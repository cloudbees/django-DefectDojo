# Generated by Django 2.2.17 on 2021-02-27 17:14

from django.db import migrations
import logging
logger = logging.getLogger(__name__)


def populate_last_status_update(apps, schema_editor):
    # We can't import the models directly as it may be a newer
    # version than this migration expects. We use the historical version.
    logger.info('Setting last_status_update timestamp on findings to be initially equal to last_reviewed timestamp (may take a while)')

    findings = apps.get_model('dojo', 'Finding').objects.all()

    i = 0
    for find in findings:
        # by default it is 'now' from the migration, but last_reviewed is better default for existing findings
        find.last_status_update = find.last_reviewed
        find.save()
        i += 1

        if i > 0 and i % 1000 == 0:
            logger.info('%s findings updated...', i)


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0080_last_status_update'),
    ]

    operations = [
        migrations.RunPython(populate_last_status_update, migrations.RunPython.noop),
    ]
