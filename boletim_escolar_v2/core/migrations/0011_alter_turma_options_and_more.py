# Generated by Django 5.1.2 on 2024-11-08 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_aluno_email_responsavel_aluno_telefone_responsavel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turma',
            options={'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_dadas_bimestre1',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_dadas_bimestre2',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_dadas_bimestre3',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_dadas_bimestre4',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_previstas_bimestre1',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_previstas_bimestre2',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_previstas_bimestre3',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aulas_previstas_bimestre4',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='nome',
        ),
        migrations.AddField(
            model_name='professor',
            name='disciplina',
            field=models.CharField(default='Indefinido', max_length=255),
        ),
        migrations.AddField(
            model_name='turma',
            name='classe',
            field=models.CharField(default='Indefinido', max_length=5),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(related_name='turmas', to='core.aluno'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='ano',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='turma',
            name='professores',
            field=models.ManyToManyField(related_name='turmas', to='core.professor'),
        ),
    ]
