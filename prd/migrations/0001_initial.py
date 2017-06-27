# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 10:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Build number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira subtask for build')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('released', models.BooleanField(default=False, verbose_name='Is released')),
                ('date_released', models.DateTimeField(blank=True, null=True, verbose_name='Build date')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='BuildRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.CharField(blank=True, max_length=40, null=True, verbose_name='Git revision')),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Build')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalBuild',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Build number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira subtask for build')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('released', models.BooleanField(default=False, verbose_name='Is released')),
                ('date_released', models.DateTimeField(blank=True, null=True, verbose_name='Build date')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Created')),
                ('updated', models.DateField(blank=True, editable=False, verbose_name='Updated')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical build',
            },
        ),
        migrations.CreateModel(
            name='HistoricalHotFix',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='HotFix number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira task for hotfix')),
                ('date_released', models.DateTimeField(blank=True, editable=False, verbose_name='HotFix date')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='Updated')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('build', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prd.Build')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical HotFix',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Product title')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Product Description')),
                ('wiki_url', models.URLField(blank=True, null=True, verbose_name='Wiki/Confluence URL')),
                ('jira', models.CharField(choices=[('AB', 'Agency Banking(AB)'), ('AIB', 'AIB(AIB)'), ('AIT', 'AIT(AIT)'), ('AP', 'Algerie Poste(AP)'), ('AMAN', 'AMAN(AMAN)'), ('ARPM', 'Architecture and Product Management(ARPM)'), ('ATT', 'ARIS (TestTool)(ATT)'), ('ATME', 'ATM Emulator(ATME)'), ('ASB', 'ATM Scenario Builder(ASB)'), ('AVB', 'Avers Bank(AVB)'), ('BA', 'Bank of Africa(BA)'), ('BAN', 'Bankmed(BAN)'), ('BANM', 'BANM(BANM)'), ('B_OB_ITI', 'BPC BT OB IT Infrastructure(B_OB_ITI)'), ('B_MC_LD', 'BPC MC Legal Department(B_MC_LD)'), ('B_MC_TS', 'BPC MC Technical Support(B_MC_TS)'), ('BCS', 'BPC-CSA(BCS)'), ('BPCO', 'BPCO(BPCO)'), ('CGBL', 'CardGen NG(CGBL)'), ('CASH', 'Cash Management(CASH)'), ('CBI', 'CBI(CBI)'), ('CBP', 'ChargeBack project(CBP)'), ('CHIEF', 'Chief Bank(CHIEF)'), ('DAB', 'DAB(DAB)'), ('DPAP', 'Data Preparation and Personalization(DPAP)'), ('DAT', 'Datafast(DAT)'), ('DVPT', 'DevOps test(DVPT)'), ('DTA', 'Documentation tasks(DTA)'), ('DSKB', 'DSK Bank(DSKB)'), ('ECOM', 'e-Commerce(ECOM)'), ('EBC', 'EBC(EBC)'), ('ECA', 'ERSTE CSAS ATM Pilot Implimentation(ECA)'), ('ECC', 'ERSTE CSAS CC(ECC)'), ('EDS', 'Erste DefectSynch(EDS)'), ('EGI', 'Erste Group Implementation(EGI)'), ('EGT', 'Erste Group testing(EGT)'), ('EPS', 'Erste Production Support(EPS)'), ('ESC', 'ERSTE SLSP CC Pilot Implementation(ESC)'), ('ECMB', 'EuroCommerce Bank(ECMB)'), ('ERM', 'Fraud Monitoring (SVFM)(ERM)'), ('FRP', 'Fraud project(FRP)'), ('GAL', 'Galnaftogaz(GAL)'), ('GAZ', 'Gazprombank(GAZ)'), ('GNS', 'Generic NS Front End(GNS)'), ('QA', 'Global_QA(QA)'), ('GRB', 'Group B internal(GRB)'), ('ICC', 'ICC(ICC)'), ('IRA', 'ING Romania(IRA)'), ('IE', 'InPlat Technologies(IE)'), ('SVAT', 'Internet/Mobile bank(SVAT)'), ('ITB', 'ITBI(ITB)'), ('JKB', 'JKB(JKB)'), ('KRB', 'Kredobank(KRB)'), ('KSB', 'Kreshhatik SmartBank(KSB)'), ('KS', 'Kreshhatik SVGate(KS)'), ('MEA', 'MEA(MEA)'), ('NAG', 'NagraID(NAG)'), ('EBS', 'NETS EBS(EBS)'), ('NCT', 'New CoreWorkflow Test 2(NCT)'), ('NSTP', 'NonStop(NSTP)'), ('OAB', 'Oman Arab Bank(OAB)'), ('PDR', 'PA DSS recertification(PDR)'), ('PP', 'Payroll Portal(PP)'), ('PB', 'PervoBank(PB)'), ('PMA', 'PMA(PMA)'), ('PSCB', 'PSCB Implementation(PSCB)'), ('PSCBS', 'PSCB Support(PSCBS)'), ('RPI', 'R&D_2017_Prototype for Indonesia(RPI)'), ('RAJ', 'Rajfajzenbank-Aval(RAJ)'), ('RS', 'Redsys Support(RS)'), ('ROS', 'RosEuroBank(ROS)'), ('RSHB', 'Rosselhozbank(RSHB)'), ('SALES', 'Sales(SALES)'), ('SAMB', 'Saman Bank(SAMB)'), ('SE', 'Sberbank estimations(SE)'), ('SBIN', 'SBIN(SBIN)'), ('SX', 'Senagat  Bank(SX)'), ('SVINST', 'SmartInstaller(SVINST)'), ('CORE', 'SmartVista Back Office(CORE)'), ('SVCI', 'SmartVista Continuous Integration and Testing(SVCI)'), ('SIP', 'SmartVista Integration Platform(SIP)'), ('SVKRN', 'SmartVista Kernel(SVKRN)'), ('SLB', 'SmartVista Load Balancer(SLB)'), ('SNG', 'SmartVista New Generation(SNG)'), ('SVNTF', 'SmartVista Notification Gateway(SVNTF)'), ('BPP', 'SmartVista Presales Support(BPP)'), ('SRD', 'SmartVista R&D(SRD)'), ('SRM', 'SmartVista Reconciliation module(SRM)'), ('SSM', 'SmartVista System Monitoring(SSM)'), ('SVWF', 'SmartVista Workflow(SVWF)'), ('SVTWO', 'SmartVista-2 Development (outdated)(SVTWO)'), ('SG', 'SMS Gate(SG)'), ('SMT', 'SMT(SMT)'), ('SPEBS', 'SPEBS(SPEBS)'), ('SVBOIM', 'SVBO team infrastructure maintenance(SVBOIM)'), ('SVBOAT', 'SVBO2 autotesting(SVBOAT)'), ('CORES', 'SVBO2 services(CORES)'), ('TI', 'Trac Imported(TI)'), ('TC', 'Transportcard(TC)'), ('UC', 'UkrCard(UC)'), ('FM', 'Unified Fraud Monitoring (FM)'), ('UX', 'UX/UI Design(UX)'), ('YOTA', 'Yota Bank(YOTA)'), ('YOS', 'YOTA Support(YOS)')], db_index=True, help_text='Jira project key', max_length=20, verbose_name='Jira project code')),
                ('created', models.DateField(blank=True, editable=False)),
                ('updated', models.DateField(blank=True, editable=False)),
                ('specification_repo', models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], help_text='Gitlab repository for product specifications', null=True, verbose_name='Specifications repository')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('inst', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='acm.Institution')),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical product',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRelease',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Release number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira task for release')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('released', models.BooleanField(default=False, verbose_name='Is released')),
                ('date_released', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Created')),
                ('updated', models.DateField(blank=True, editable=False, verbose_name='Updated')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical release',
            },
        ),
        migrations.CreateModel(
            name='HistoricalReleasePart',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Module name')),
                ('gitlab_id', models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], null=True, verbose_name='Gitlab project')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical release part',
            },
        ),
        migrations.CreateModel(
            name='HotFix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='HotFix number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira task for hotfix')),
                ('date_released', models.DateTimeField(auto_now_add=True, verbose_name='HotFix date')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Build')),
            ],
            options={
                'verbose_name': 'HotFix',
            },
        ),
        migrations.CreateModel(
            name='HotFixRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.CharField(blank=True, max_length=40, null=True, verbose_name='Git revision')),
                ('hotfix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.HotFix')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Product title')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Product Description')),
                ('wiki_url', models.URLField(blank=True, null=True, verbose_name='Wiki/Confluence URL')),
                ('jira', models.CharField(choices=[('AB', 'Agency Banking(AB)'), ('AIB', 'AIB(AIB)'), ('AIT', 'AIT(AIT)'), ('AP', 'Algerie Poste(AP)'), ('AMAN', 'AMAN(AMAN)'), ('ARPM', 'Architecture and Product Management(ARPM)'), ('ATT', 'ARIS (TestTool)(ATT)'), ('ATME', 'ATM Emulator(ATME)'), ('ASB', 'ATM Scenario Builder(ASB)'), ('AVB', 'Avers Bank(AVB)'), ('BA', 'Bank of Africa(BA)'), ('BAN', 'Bankmed(BAN)'), ('BANM', 'BANM(BANM)'), ('B_OB_ITI', 'BPC BT OB IT Infrastructure(B_OB_ITI)'), ('B_MC_LD', 'BPC MC Legal Department(B_MC_LD)'), ('B_MC_TS', 'BPC MC Technical Support(B_MC_TS)'), ('BCS', 'BPC-CSA(BCS)'), ('BPCO', 'BPCO(BPCO)'), ('CGBL', 'CardGen NG(CGBL)'), ('CASH', 'Cash Management(CASH)'), ('CBI', 'CBI(CBI)'), ('CBP', 'ChargeBack project(CBP)'), ('CHIEF', 'Chief Bank(CHIEF)'), ('DAB', 'DAB(DAB)'), ('DPAP', 'Data Preparation and Personalization(DPAP)'), ('DAT', 'Datafast(DAT)'), ('DVPT', 'DevOps test(DVPT)'), ('DTA', 'Documentation tasks(DTA)'), ('DSKB', 'DSK Bank(DSKB)'), ('ECOM', 'e-Commerce(ECOM)'), ('EBC', 'EBC(EBC)'), ('ECA', 'ERSTE CSAS ATM Pilot Implimentation(ECA)'), ('ECC', 'ERSTE CSAS CC(ECC)'), ('EDS', 'Erste DefectSynch(EDS)'), ('EGI', 'Erste Group Implementation(EGI)'), ('EGT', 'Erste Group testing(EGT)'), ('EPS', 'Erste Production Support(EPS)'), ('ESC', 'ERSTE SLSP CC Pilot Implementation(ESC)'), ('ECMB', 'EuroCommerce Bank(ECMB)'), ('ERM', 'Fraud Monitoring (SVFM)(ERM)'), ('FRP', 'Fraud project(FRP)'), ('GAL', 'Galnaftogaz(GAL)'), ('GAZ', 'Gazprombank(GAZ)'), ('GNS', 'Generic NS Front End(GNS)'), ('QA', 'Global_QA(QA)'), ('GRB', 'Group B internal(GRB)'), ('ICC', 'ICC(ICC)'), ('IRA', 'ING Romania(IRA)'), ('IE', 'InPlat Technologies(IE)'), ('SVAT', 'Internet/Mobile bank(SVAT)'), ('ITB', 'ITBI(ITB)'), ('JKB', 'JKB(JKB)'), ('KRB', 'Kredobank(KRB)'), ('KSB', 'Kreshhatik SmartBank(KSB)'), ('KS', 'Kreshhatik SVGate(KS)'), ('MEA', 'MEA(MEA)'), ('NAG', 'NagraID(NAG)'), ('EBS', 'NETS EBS(EBS)'), ('NCT', 'New CoreWorkflow Test 2(NCT)'), ('NSTP', 'NonStop(NSTP)'), ('OAB', 'Oman Arab Bank(OAB)'), ('PDR', 'PA DSS recertification(PDR)'), ('PP', 'Payroll Portal(PP)'), ('PB', 'PervoBank(PB)'), ('PMA', 'PMA(PMA)'), ('PSCB', 'PSCB Implementation(PSCB)'), ('PSCBS', 'PSCB Support(PSCBS)'), ('RPI', 'R&D_2017_Prototype for Indonesia(RPI)'), ('RAJ', 'Rajfajzenbank-Aval(RAJ)'), ('RS', 'Redsys Support(RS)'), ('ROS', 'RosEuroBank(ROS)'), ('RSHB', 'Rosselhozbank(RSHB)'), ('SALES', 'Sales(SALES)'), ('SAMB', 'Saman Bank(SAMB)'), ('SE', 'Sberbank estimations(SE)'), ('SBIN', 'SBIN(SBIN)'), ('SX', 'Senagat  Bank(SX)'), ('SVINST', 'SmartInstaller(SVINST)'), ('CORE', 'SmartVista Back Office(CORE)'), ('SVCI', 'SmartVista Continuous Integration and Testing(SVCI)'), ('SIP', 'SmartVista Integration Platform(SIP)'), ('SVKRN', 'SmartVista Kernel(SVKRN)'), ('SLB', 'SmartVista Load Balancer(SLB)'), ('SNG', 'SmartVista New Generation(SNG)'), ('SVNTF', 'SmartVista Notification Gateway(SVNTF)'), ('BPP', 'SmartVista Presales Support(BPP)'), ('SRD', 'SmartVista R&D(SRD)'), ('SRM', 'SmartVista Reconciliation module(SRM)'), ('SSM', 'SmartVista System Monitoring(SSM)'), ('SVWF', 'SmartVista Workflow(SVWF)'), ('SVTWO', 'SmartVista-2 Development (outdated)(SVTWO)'), ('SG', 'SMS Gate(SG)'), ('SMT', 'SMT(SMT)'), ('SPEBS', 'SPEBS(SPEBS)'), ('SVBOIM', 'SVBO team infrastructure maintenance(SVBOIM)'), ('SVBOAT', 'SVBO2 autotesting(SVBOAT)'), ('CORES', 'SVBO2 services(CORES)'), ('TI', 'Trac Imported(TI)'), ('TC', 'Transportcard(TC)'), ('UC', 'UkrCard(UC)'), ('FM', 'Unified Fraud Monitoring (FM)'), ('UX', 'UX/UI Design(UX)'), ('YOTA', 'Yota Bank(YOTA)'), ('YOS', 'YOTA Support(YOS)')], help_text='Jira project key', max_length=20, unique=True, verbose_name='Jira project code')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('specification_repo', models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], help_text='Gitlab repository for product specifications', null=True, verbose_name='Specifications repository')),
                ('inst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm.Institution', verbose_name='Group')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Release number')),
                ('jira', models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira task for release')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('released', models.BooleanField(default=False, verbose_name='Is released')),
                ('date_released', models.DateField(blank=True, null=True, verbose_name='Release date')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Product')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ReleasePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Module name')),
                ('gitlab_id', models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], null=True, verbose_name='Gitlab project')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Product')),
                ('release', models.ForeignKey(blank=True, help_text='Specific release number. Skip if all releases have one configurations', null=True, on_delete=django.db.models.deletion.CASCADE, to='prd.Release')),
            ],
        ),
        migrations.AddField(
            model_name='hotfixrevision',
            name='release_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.ReleasePart'),
        ),
        migrations.AddField(
            model_name='historicalreleasepart',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prd.Product'),
        ),
        migrations.AddField(
            model_name='historicalreleasepart',
            name='release',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prd.Release'),
        ),
        migrations.AddField(
            model_name='historicalrelease',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prd.Product'),
        ),
        migrations.AddField(
            model_name='historicalbuild',
            name='release',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='prd.Release'),
        ),
        migrations.AddField(
            model_name='buildrevision',
            name='release_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.ReleasePart'),
        ),
        migrations.AddField(
            model_name='build',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Release'),
        ),
        migrations.AlterUniqueTogether(
            name='releasepart',
            unique_together=set([('name', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('name', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='hotfix',
            unique_together=set([('build', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='build',
            unique_together=set([('name', 'release')]),
        ),
    ]
