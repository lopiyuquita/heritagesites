# Generated by Django 2.1.2 on 2018-10-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryArea',
            fields=[
                ('country_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_area_name', models.CharField(max_length=100, unique=True)),
                ('m49_code', models.SmallIntegerField()),
                ('iso_alpha3_code', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'UNSD M49 Country or Area',
                'verbose_name_plural': 'UNSD M49 Countries or Areas',
                'db_table': 'country_area',
                'ordering': ['country_area_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DevStatus',
            fields=[
                ('dev_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('dev_status_name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'UNSD M49 Country or Area Development Status',
                'verbose_name_plural': 'UNSD M49 Country or Area Development Statuses',
                'db_table': 'dev_status',
                'ordering': ['dev_status_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HeritageSite',
            fields=[
                ('heritage_site_id', models.AutoField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('justification', models.TextField(blank=True, null=True)),
                ('date_inscribed', models.TextField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('area_hectares', models.FloatField(blank=True, null=True)),
                ('transboundary', models.IntegerField()),
            ],
            options={
                'verbose_name': 'UNESCO Heritage Site',
                'verbose_name_plural': 'UNESCO Heritage Sites',
                'db_table': 'heritage_site',
                'ordering': ['site_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HeritageSiteCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'UNESCO Heritage Site Category',
                'verbose_name_plural': 'UNESCO Heritage Site Categories',
                'db_table': 'heritage_site_category',
                'ordering': ['category_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HeritageSiteJurisdiction',
            fields=[
                ('heritage_site_jurisdiction_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'UNESCO Heritage Site Jurisdiction',
                'verbose_name_plural': 'UNESCO Heritage Site Jurisdictions',
                'db_table': 'heritage_site_jurisdiction',
                'ordering': ['heritage_site', 'country_area'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IntermediateRegion',
            fields=[
                ('intermediate_region_id', models.AutoField(primary_key=True, serialize=False)),
                ('intermediate_region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNSD M49 Intermediate Region',
                'verbose_name_plural': 'UNSD M49 Intermediate Regions',
                'db_table': 'intermediate_region',
                'ordering': ['intermediate_region_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('planet_id', models.AutoField(primary_key=True, serialize=False)),
                ('planet_name', models.CharField(max_length=50, unique=True)),
                ('unsd_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Planet',
                'verbose_name_plural': 'Planets',
                'db_table': 'planet',
                'ordering': ['planet_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNSD M49 Region',
                'verbose_name_plural': 'UNSD M49 Regions',
                'db_table': 'region',
                'ordering': ['region_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubRegion',
            fields=[
                ('sub_region_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNSD M49 Subregion',
                'verbose_name_plural': 'UNSD M49 Subregions',
                'db_table': 'sub_region',
                'ordering': ['sub_region_name'],
                'managed': False,
            },
        ),
    ]
