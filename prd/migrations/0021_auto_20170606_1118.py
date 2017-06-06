# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0020_auto_20170606_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='specification_repo',
            field=models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], help_text='Gitlab repostitory for product specifications', null=True, verbose_name='Specifications repository'),
        ),
        migrations.AlterField(
            model_name='historicalreleasepart',
            name='gitlab_id',
            field=models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], null=True, verbose_name='Gitlab project'),
        ),
        migrations.AlterField(
            model_name='historicalreleasepart',
            name='work_branch',
            field=models.CharField(blank=True, default='future', max_length=200, null=True, verbose_name='Work branch'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification_repo',
            field=models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], help_text='Gitlab repostitory for product specifications', null=True, verbose_name='Specifications repository'),
        ),
        migrations.AlterField(
            model_name='releasepart',
            name='gitlab_id',
            field=models.IntegerField(blank=True, choices=[(114, 'BackOffice / BackOffice SmartVista2'), (190, 'BackOffice / Design'), (186, 'BackOffice / Specifications'), (517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (479, 'DevOps Team / Check'), (436, 'DevOps Team / Database Carousel'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (228, 'DevOps Team / Release management'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (337, 'DevOps Team / devops-service'), (225, 'DevOps Team / dictreport'), (334, 'DevOps Team / env-config'), (293, 'DevOps Team / gitlab-tools'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (331, 'DevOps Team / instance_list'), (55, 'DevOps Team / jenkins-tools'), (283, 'DevOps Team / learn_python'), (385, 'DevOps Team / qa'), (6, 'DevOps Team / sv_installer'), (396, 'DevOps Team / sv_installer_tools'), (86, 'DevOps Team / svtools'), (150, 'GroupB / BackOffice SmartVista2'), (154, 'GroupB / SVWeb'), (155, 'GroupB / adapter'), (142, 'GroupD / GroupD BackOffice'), (25, 'OLTP / SVTokenizer'), (24, 'OLTP / adapter'), (26, 'OLTP / pseudo-ips'), (332, 'OLTP / svfe2'), (65, 'OLTP / svfe_postgre'), (22, 'QATeam / Aris2TestLink'), (23, 'QATeam / Aris2TestLinkConfig'), (19, 'QATeam / ArisCustom'), (18, 'QATeam / AutotestSVWeb'), (21, 'QATeam / JMeterExtLibs'), (118, 'QATeam / Legacy'), (17, 'QATeam / NetworkData'), (172, 'QATeam / Night autotest configuration'), (20, 'QATeam / SVFECustom'), (119, 'QATeam / SVFE_configuration'), (122, 'QATeam / auto_ARIS_profiles'), (117, 'QATeam / auto_Jmeter'), (132, 'QATeam / auto_OLTP'), (116, 'QATeam / auto_WebServices'), (205, 'QATeam / auto_integration'), (185, 'QATeam / camel_conf_remap'), (217, 'QATeam / jenkins-tools'), (176, 'QATeam / service_data'), (180, 'QATeam / svweb_data'), (72, 'RnD / SmartVista'), (149, 'RnD / docs'), (335, 'RnD / help-manual'), (425, 'RnD / spec'), (13, 'SMSGate / Notification Gateway'), (559, 'SMSGate / Notification Specifications'), (383, 'SMSGate / jsmpp'), (382, 'SMSGate / sms-lib'), (12, 'SVNG / SmartMQ'), (96, 'SVNG / aggregation_lib'), (48, 'SVNG / reconciliation'), (90, 'SVWeb / Camel converters'), (566, 'SVWeb / FE Integration Service'), (537, 'SVWeb / FEAdapter'), (14, 'SVWeb / LoginModule'), (424, 'SVWeb / SV Kernel - Single Sign-On'), (219, 'SVWeb / SVNG specification'), (10, 'SVWeb / SVNGAuth'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (15, 'SVWeb / SVWI'), (9, 'SVWeb / SVWeb'), (454, 'SVWeb / com.bpcbt.iso8583'), (99, 'SVWeb / interchange_lib'), (98, 'SVWeb / module_lib'), (408, 'SVWeb / smsgateway-sv2'), (400, 'SVWeb / sync-daemon'), (92, 'SVWeb / ws_listener'), (113, 'SVWeb / wsdl-lib'), (70, 'fraud / fraud'), (443, 'java-commons / com.bpcbt.commons.bpc-commons-extension'), (444, 'java-commons / com.bpcbt.commons.bpc-commons-web-extension'), (68, 'java-commons / com.bpcbt.commons.db.db-utils'), (67, 'java-commons / com.bpcbt.commons.db.query-api'), (445, 'java-commons / com.bpcbt.commons.db.query-extension'), (427, 'java-commons / com.bpcbt.commons.db.query-mysql'), (66, 'java-commons / com.bpcbt.commons.db.query-oracle'), (420, 'java-commons / com.bpcbt.iso8583'), (442, 'java-commons / com.bpcbt.ui.richfaces-impl')], null=True, verbose_name='Gitlab project'),
        ),
        migrations.AlterField(
            model_name='releasepart',
            name='work_branch',
            field=models.CharField(blank=True, default='future', max_length=200, null=True, verbose_name='Work branch'),
        ),
    ]