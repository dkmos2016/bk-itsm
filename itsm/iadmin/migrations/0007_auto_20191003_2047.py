# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2019-10-21 14:17


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iadmin', '0006_auto_20190919_2000'),
    ]

    operations = [
        migrations.RemoveField(model_name='customnotice', name='creator',),
        migrations.AddField(
            model_name='customnotice',
            name='updated_by',
            field=models.CharField(default='system', max_length=64, verbose_name='\u66f4\u65b0\u4eba'),
        ),
        migrations.AddField(
            model_name='customnotice',
            name='version',
            field=models.CharField(default='V1', max_length=32, verbose_name='\u7248\u672c'),
        ),
        migrations.AlterField(
            model_name='customnotice',
            name='action',
            field=models.CharField(
                choices=[
                    ('TERMINATE', '\u5355\u636e\u7ec8\u6b62\u901a\u77e5'),
                    ('FOLLOW', '\u9080\u8bf7\u5173\u6ce8\u901a\u77e5'),
                    ('INVITE', '\u9080\u8bf7\u8bc4\u4ef7\u901a\u77e5'),
                    ('SUPERVISE', '\u5355\u636e\u7763\u529e\u901a\u77e5'),
                    ('SUSPEND', '\u5355\u636e\u6302\u8d77\u901a\u77e5'),
                    ('UNSUSPEND', '\u5355\u636e\u6062\u590d\u901a\u77e5'),
                    ('TRANSITION', '\u5355\u636e\u5f85\u529e\u901a\u77e5'),
                    ('FINISHED', '\u5355\u636e\u7ed3\u675f\u901a\u77e5'),
                ],
                default='default',
                max_length=32,
                verbose_name='\u901a\u77e5\u6a21\u677f\u7c7b\u578b',
            ),
        ),
        migrations.AlterField(
            model_name='customnotice',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]