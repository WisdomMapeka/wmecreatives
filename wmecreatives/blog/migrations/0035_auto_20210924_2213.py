# Generated by Django 3.2.7 on 2021-09-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_todayscode_styleshit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='styleshit',
            field=models.CharField(blank=True, choices=[('magula.min.css', 'magula.min.css'), ('zenburn.css', 'zenburn.css'), ('arta.css', 'arta.css'), ('nord.min.css', 'nord.min.css'), ('stackoverflow-dark.css', 'stackoverflow-dark.css'), ('paraiso-light.min.css', 'paraiso-light.min.css'), ('dark.css', 'dark.css'), ('atelier-lakeside-dark.css', 'atelier-lakeside-dark.css'), ('androidstudio.css', 'androidstudio.css'), ('lightfair.css', 'lightfair.css'), ('qtcreator_light.css', 'qtcreator_light.css'), ('magula.css', 'magula.css'), ('night-owl.min.css', 'night-owl.min.css'), ('color-brewer.css', 'color-brewer.css'), ('far.css', 'far.css'), ('atom-one-dark.min.css', 'atom-one-dark.min.css'), ('devibeans.min.css', 'devibeans.min.css'), ('qtcreator-dark.min.css', 'qtcreator-dark.min.css'), ('solarized-dark.css', 'solarized-dark.css'), ('srcery.min.css', 'srcery.min.css'), ('atelier-heath-dark.css', 'atelier-heath-dark.css'), ('gruvbox-light.css', 'gruvbox-light.css'), ('srcery.css', 'srcery.css'), ('obsidian.css', 'obsidian.css'), ('paraiso-light.css', 'paraiso-light.css'), ('atelier-dune-light.css', 'atelier-dune-light.css'), ('tomorrow-night-bright.min.css', 'tomorrow-night-bright.min.css'), ('atelier-sulphurpool-light.css', 'atelier-sulphurpool-light.css'), ('lioshi.min.css', 'lioshi.min.css'), ('kimbie.light.css', 'kimbie.light.css'), ('sunburst.min.css', 'sunburst.min.css'), ('vs2015.min.css', 'vs2015.min.css'), ('tomorrow-night-blue.min.css', 'tomorrow-night-blue.min.css'), ('pojoaque.jpg', 'pojoaque.jpg'), ('atelier-estuary-dark.css', 'atelier-estuary-dark.css'), ('foundation.css', 'foundation.css'), ('darcula.css', 'darcula.css'), ('color-brewer.min.css', 'color-brewer.min.css'), ('grayscale.css', 'grayscale.css'), ('sunburst.css', 'sunburst.css'), ('tomorrow.css', 'tomorrow.css'), ('tomorrow-night-blue.css', 'tomorrow-night-blue.css'), ('atom-one-light.css', 'atom-one-light.css'), ('tomorrow-night-bright.css', 'tomorrow-night-bright.css'), ('atelier-savanna-dark.css', 'atelier-savanna-dark.css'), ('a11y-dark.min.css', 'a11y-dark.min.css'), ('kimbie-dark.min.css', 'kimbie-dark.min.css'), ('pojoaque.css', 'pojoaque.css'), ('vs.css', 'vs.css'), ('kimbie-light.min.css', 'kimbie-light.min.css'), ('stackoverflow-light.css', 'stackoverflow-light.css'), ('atelier-forest-dark.css', 'atelier-forest-dark.css'), ('dracula.css', 'dracula.css'), ('atelier-plateau-dark.css', 'atelier-plateau-dark.css'), ('default.css', 'default.css'), ('rainbow.css', 'rainbow.css'), ('xcode.min.css', 'xcode.min.css'), ('foundation.min.css', 'foundation.min.css'), ('hopscotch.css', 'hopscotch.css'), ('brown-papersq.png', 'brown-papersq.png'), ('agate.min.css', 'agate.min.css'), ('lioshi.css', 'lioshi.css'), ('atom-one-light.min.css', 'atom-one-light.min.css'), ('school-book.min.css', 'school-book.min.css'), ('atom-one-dark.css', 'atom-one-dark.css'), ('qtcreator_dark.css', 'qtcreator_dark.css'), ('isbl-editor-dark.css', 'isbl-editor-dark.css'), ('lightfair.min.css', 'lightfair.min.css'), ('atelier-estuary-light.css', 'atelier-estuary-light.css'), ('github.min.css', 'github.min.css'), ('night-owl.css', 'night-owl.css'), ('routeros.css', 'routeros.css'), ('atelier-heath-light.css', 'atelier-heath-light.css'), ('monokai.css', 'monokai.css'), ('vs2015.css', 'vs2015.css'), ('ir-black.min.css', 'ir-black.min.css'), ('monokai-sublime.css', 'monokai-sublime.css'), ('monokai.min.css', 'monokai.min.css'), ('kimbie.dark.css', 'kimbie.dark.css'), ('an-old-hope.css', 'an-old-hope.css'), ('atom-one-dark-reasonable.css', 'atom-one-dark-reasonable.css'), ('codepen-embed.css', 'codepen-embed.css'), ('atelier-forest-light.css', 'atelier-forest-light.css'), ('github-dark.min.css', 'github-dark.min.css'), ('brown-paper.min.css', 'brown-paper.min.css'), ('isbl-editor-light.css', 'isbl-editor-light.css'), ('brown-paper.css', 'brown-paper.css'), ('monokai-sublime.min.css', 'monokai-sublime.min.css'), ('mono-blue.min.css', 'mono-blue.min.css'), ('nnfx-dark.min.css', 'nnfx-dark.min.css'), ('codepen-embed.min.css', 'codepen-embed.min.css'), ('atelier-plateau-light.css', 'atelier-plateau-light.css'), ('far.min.css', 'far.min.css'), ('xt256.css', 'xt256.css'), ('github-dark-dimmed.min.css', 'github-dark-dimmed.min.css'), ('a11y-light.min.css', 'a11y-light.min.css'), ('atelier-sulphurpool-dark.css', 'atelier-sulphurpool-dark.css'), ('isbl-editor-light.min.css', 'isbl-editor-light.min.css'), ('github.css', 'github.css'), ('shades-of-purple.min.css', 'shades-of-purple.min.css'), ('googlecode.css', 'googlecode.css'), ('arta.min.css', 'arta.min.css'), ('school-book.png', 'school-book.png'), ('nnfx-dark.css', 'nnfx-dark.css'), ('github-gist.css', 'github-gist.css'), ('ir-black.css', 'ir-black.css'), ('shades-of-purple.css', 'shades-of-purple.css'), ('grayscale.min.css', 'grayscale.min.css'), ('vs.min.css', 'vs.min.css'), ('arduino-light.min.css', 'arduino-light.min.css'), ('nord.css', 'nord.css'), ('rainbow.min.css', 'rainbow.min.css'), ('ocean.css', 'ocean.css'), ('ascetic.min.css', 'ascetic.min.css'), ('gradient-dark.css', 'gradient-dark.css'), ('atom-one-dark-reasonable.min.css', 'atom-one-dark-reasonable.min.css'), ('railscasts.css', 'railscasts.css'), ('stackoverflow-dark.min.css', 'stackoverflow-dark.min.css'), ('default.min.css', 'default.min.css'), ('mono-blue.css', 'mono-blue.css'), ('agate.css', 'agate.css'), ('purebasic.css', 'purebasic.css'), ('hybrid.min.css', 'hybrid.min.css'), ('idea.min.css', 'idea.min.css'), ('androidstudio.min.css', 'androidstudio.min.css'), ('googlecode.min.css', 'googlecode.min.css'), ('atelier-dune-dark.css', 'atelier-dune-dark.css'), ('gruvbox-dark.css', 'gruvbox-dark.css'), ('gml.min.css', 'gml.min.css'), ('dark.min.css', 'dark.min.css'), ('atelier-cave-dark.css', 'atelier-cave-dark.css'), ('xt256.min.css', 'xt256.min.css'), ('hybrid.css', 'hybrid.css'), ('arduino-light.css', 'arduino-light.css'), ('a11y-dark.css', 'a11y-dark.css'), ('idea.css', 'idea.css'), ('xcode.css', 'xcode.css'), ('ascetic.css', 'ascetic.css'), ('docco.css', 'docco.css'), ('tomorrow-night-eighties.css', 'tomorrow-night-eighties.css'), ('isbl-editor-dark.min.css', 'isbl-editor-dark.min.css'), ('gml.css', 'gml.css'), ('nnfx-light.min.css', 'nnfx-light.min.css'), ('gradient-light.css', 'gradient-light.css'), ('atelier-seaside-dark.css', 'atelier-seaside-dark.css'), ('school-book.css', 'school-book.css'), ('pojoaque.min.css', 'pojoaque.min.css'), ('paraiso-dark.min.css', 'paraiso-dark.min.css'), ('nnfx.css', 'nnfx.css'), ('tomorrow-night.css', 'tomorrow-night.css'), ('purebasic.min.css', 'purebasic.min.css'), ('routeros.min.css', 'routeros.min.css'), ('gradient-dark.min.css', 'gradient-dark.min.css'), ('paraiso-dark.css', 'paraiso-dark.css'), ('qtcreator-light.min.css', 'qtcreator-light.min.css'), ('docco.min.css', 'docco.min.css'), ('atelier-seaside-light.css', 'atelier-seaside-light.css'), ('atelier-lakeside-light.css', 'atelier-lakeside-light.css'), ('stackoverflow-light.min.css', 'stackoverflow-light.min.css'), ('atelier-cave-light.css', 'atelier-cave-light.css'), ('solarized-light.css', 'solarized-light.css'), ('a11y-light.css', 'a11y-light.css'), ('gradient-light.min.css', 'gradient-light.min.css'), ('atelier-savanna-light.css', 'atelier-savanna-light.css'), ('obsidian.min.css', 'obsidian.min.css'), ('an-old-hope.min.css', 'an-old-hope.min.css')], default='shades-of-purple.min.css', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(blank=True, help_text='31 letters max will give a better out look', null=True),
        ),
        migrations.AlterField(
            model_name='todayscode',
            name='styleshit',
            field=models.CharField(blank=True, choices=[('magula.min.css', 'magula.min.css'), ('zenburn.css', 'zenburn.css'), ('arta.css', 'arta.css'), ('nord.min.css', 'nord.min.css'), ('stackoverflow-dark.css', 'stackoverflow-dark.css'), ('paraiso-light.min.css', 'paraiso-light.min.css'), ('dark.css', 'dark.css'), ('atelier-lakeside-dark.css', 'atelier-lakeside-dark.css'), ('androidstudio.css', 'androidstudio.css'), ('lightfair.css', 'lightfair.css'), ('qtcreator_light.css', 'qtcreator_light.css'), ('magula.css', 'magula.css'), ('night-owl.min.css', 'night-owl.min.css'), ('color-brewer.css', 'color-brewer.css'), ('far.css', 'far.css'), ('atom-one-dark.min.css', 'atom-one-dark.min.css'), ('devibeans.min.css', 'devibeans.min.css'), ('qtcreator-dark.min.css', 'qtcreator-dark.min.css'), ('solarized-dark.css', 'solarized-dark.css'), ('srcery.min.css', 'srcery.min.css'), ('atelier-heath-dark.css', 'atelier-heath-dark.css'), ('gruvbox-light.css', 'gruvbox-light.css'), ('srcery.css', 'srcery.css'), ('obsidian.css', 'obsidian.css'), ('paraiso-light.css', 'paraiso-light.css'), ('atelier-dune-light.css', 'atelier-dune-light.css'), ('tomorrow-night-bright.min.css', 'tomorrow-night-bright.min.css'), ('atelier-sulphurpool-light.css', 'atelier-sulphurpool-light.css'), ('lioshi.min.css', 'lioshi.min.css'), ('kimbie.light.css', 'kimbie.light.css'), ('sunburst.min.css', 'sunburst.min.css'), ('vs2015.min.css', 'vs2015.min.css'), ('tomorrow-night-blue.min.css', 'tomorrow-night-blue.min.css'), ('pojoaque.jpg', 'pojoaque.jpg'), ('atelier-estuary-dark.css', 'atelier-estuary-dark.css'), ('foundation.css', 'foundation.css'), ('darcula.css', 'darcula.css'), ('color-brewer.min.css', 'color-brewer.min.css'), ('grayscale.css', 'grayscale.css'), ('sunburst.css', 'sunburst.css'), ('tomorrow.css', 'tomorrow.css'), ('tomorrow-night-blue.css', 'tomorrow-night-blue.css'), ('atom-one-light.css', 'atom-one-light.css'), ('tomorrow-night-bright.css', 'tomorrow-night-bright.css'), ('atelier-savanna-dark.css', 'atelier-savanna-dark.css'), ('a11y-dark.min.css', 'a11y-dark.min.css'), ('kimbie-dark.min.css', 'kimbie-dark.min.css'), ('pojoaque.css', 'pojoaque.css'), ('vs.css', 'vs.css'), ('kimbie-light.min.css', 'kimbie-light.min.css'), ('stackoverflow-light.css', 'stackoverflow-light.css'), ('atelier-forest-dark.css', 'atelier-forest-dark.css'), ('dracula.css', 'dracula.css'), ('atelier-plateau-dark.css', 'atelier-plateau-dark.css'), ('default.css', 'default.css'), ('rainbow.css', 'rainbow.css'), ('xcode.min.css', 'xcode.min.css'), ('foundation.min.css', 'foundation.min.css'), ('hopscotch.css', 'hopscotch.css'), ('brown-papersq.png', 'brown-papersq.png'), ('agate.min.css', 'agate.min.css'), ('lioshi.css', 'lioshi.css'), ('atom-one-light.min.css', 'atom-one-light.min.css'), ('school-book.min.css', 'school-book.min.css'), ('atom-one-dark.css', 'atom-one-dark.css'), ('qtcreator_dark.css', 'qtcreator_dark.css'), ('isbl-editor-dark.css', 'isbl-editor-dark.css'), ('lightfair.min.css', 'lightfair.min.css'), ('atelier-estuary-light.css', 'atelier-estuary-light.css'), ('github.min.css', 'github.min.css'), ('night-owl.css', 'night-owl.css'), ('routeros.css', 'routeros.css'), ('atelier-heath-light.css', 'atelier-heath-light.css'), ('monokai.css', 'monokai.css'), ('vs2015.css', 'vs2015.css'), ('ir-black.min.css', 'ir-black.min.css'), ('monokai-sublime.css', 'monokai-sublime.css'), ('monokai.min.css', 'monokai.min.css'), ('kimbie.dark.css', 'kimbie.dark.css'), ('an-old-hope.css', 'an-old-hope.css'), ('atom-one-dark-reasonable.css', 'atom-one-dark-reasonable.css'), ('codepen-embed.css', 'codepen-embed.css'), ('atelier-forest-light.css', 'atelier-forest-light.css'), ('github-dark.min.css', 'github-dark.min.css'), ('brown-paper.min.css', 'brown-paper.min.css'), ('isbl-editor-light.css', 'isbl-editor-light.css'), ('brown-paper.css', 'brown-paper.css'), ('monokai-sublime.min.css', 'monokai-sublime.min.css'), ('mono-blue.min.css', 'mono-blue.min.css'), ('nnfx-dark.min.css', 'nnfx-dark.min.css'), ('codepen-embed.min.css', 'codepen-embed.min.css'), ('atelier-plateau-light.css', 'atelier-plateau-light.css'), ('far.min.css', 'far.min.css'), ('xt256.css', 'xt256.css'), ('github-dark-dimmed.min.css', 'github-dark-dimmed.min.css'), ('a11y-light.min.css', 'a11y-light.min.css'), ('atelier-sulphurpool-dark.css', 'atelier-sulphurpool-dark.css'), ('isbl-editor-light.min.css', 'isbl-editor-light.min.css'), ('github.css', 'github.css'), ('shades-of-purple.min.css', 'shades-of-purple.min.css'), ('googlecode.css', 'googlecode.css'), ('arta.min.css', 'arta.min.css'), ('school-book.png', 'school-book.png'), ('nnfx-dark.css', 'nnfx-dark.css'), ('github-gist.css', 'github-gist.css'), ('ir-black.css', 'ir-black.css'), ('shades-of-purple.css', 'shades-of-purple.css'), ('grayscale.min.css', 'grayscale.min.css'), ('vs.min.css', 'vs.min.css'), ('arduino-light.min.css', 'arduino-light.min.css'), ('nord.css', 'nord.css'), ('rainbow.min.css', 'rainbow.min.css'), ('ocean.css', 'ocean.css'), ('ascetic.min.css', 'ascetic.min.css'), ('gradient-dark.css', 'gradient-dark.css'), ('atom-one-dark-reasonable.min.css', 'atom-one-dark-reasonable.min.css'), ('railscasts.css', 'railscasts.css'), ('stackoverflow-dark.min.css', 'stackoverflow-dark.min.css'), ('default.min.css', 'default.min.css'), ('mono-blue.css', 'mono-blue.css'), ('agate.css', 'agate.css'), ('purebasic.css', 'purebasic.css'), ('hybrid.min.css', 'hybrid.min.css'), ('idea.min.css', 'idea.min.css'), ('androidstudio.min.css', 'androidstudio.min.css'), ('googlecode.min.css', 'googlecode.min.css'), ('atelier-dune-dark.css', 'atelier-dune-dark.css'), ('gruvbox-dark.css', 'gruvbox-dark.css'), ('gml.min.css', 'gml.min.css'), ('dark.min.css', 'dark.min.css'), ('atelier-cave-dark.css', 'atelier-cave-dark.css'), ('xt256.min.css', 'xt256.min.css'), ('hybrid.css', 'hybrid.css'), ('arduino-light.css', 'arduino-light.css'), ('a11y-dark.css', 'a11y-dark.css'), ('idea.css', 'idea.css'), ('xcode.css', 'xcode.css'), ('ascetic.css', 'ascetic.css'), ('docco.css', 'docco.css'), ('tomorrow-night-eighties.css', 'tomorrow-night-eighties.css'), ('isbl-editor-dark.min.css', 'isbl-editor-dark.min.css'), ('gml.css', 'gml.css'), ('nnfx-light.min.css', 'nnfx-light.min.css'), ('gradient-light.css', 'gradient-light.css'), ('atelier-seaside-dark.css', 'atelier-seaside-dark.css'), ('school-book.css', 'school-book.css'), ('pojoaque.min.css', 'pojoaque.min.css'), ('paraiso-dark.min.css', 'paraiso-dark.min.css'), ('nnfx.css', 'nnfx.css'), ('tomorrow-night.css', 'tomorrow-night.css'), ('purebasic.min.css', 'purebasic.min.css'), ('routeros.min.css', 'routeros.min.css'), ('gradient-dark.min.css', 'gradient-dark.min.css'), ('paraiso-dark.css', 'paraiso-dark.css'), ('qtcreator-light.min.css', 'qtcreator-light.min.css'), ('docco.min.css', 'docco.min.css'), ('atelier-seaside-light.css', 'atelier-seaside-light.css'), ('atelier-lakeside-light.css', 'atelier-lakeside-light.css'), ('stackoverflow-light.min.css', 'stackoverflow-light.min.css'), ('atelier-cave-light.css', 'atelier-cave-light.css'), ('solarized-light.css', 'solarized-light.css'), ('a11y-light.css', 'a11y-light.css'), ('gradient-light.min.css', 'gradient-light.min.css'), ('atelier-savanna-light.css', 'atelier-savanna-light.css'), ('obsidian.min.css', 'obsidian.min.css'), ('an-old-hope.min.css', 'an-old-hope.min.css')], default='shades-of-purple.min.css', max_length=100, null=True),
        ),
    ]
