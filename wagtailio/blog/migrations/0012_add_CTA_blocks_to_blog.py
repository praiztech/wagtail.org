# Generated by Django 3.2.18 on 2023-05-18 21:48

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtailio.utils.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_blogpage_airtable_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('h2', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='patterns/components/streamfields/headings/heading-2.html')), ('h3', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='patterns/components/streamfields/headings/heading-3.html')), ('h4', wagtail.blocks.CharBlock(form_classname='title', icon='title', template='patterns/components/streamfields/headings/heading-4.html')), ('intro', wagtail.blocks.RichTextBlock(group='DO NOT USE', icon='pilcrow', template='patterns/components/streamfields/rich_text_block/rich_text_block.html')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow', template='patterns/components/streamfields/rich_text_block/rich_text_block.html')), ('blockquote', wagtail.blocks.CharBlock(form_classname='title', icon='openquote', template='patterns/components/streamfields/quotes/standalone_quote_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='patterns/components/streamfields/image/image.html')), ('document', wagtail.documents.blocks.DocumentChooserBlock(icon='doc-full-inverse', template='patterns/components/streamfields/document/document.html')), ('imagecaption', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock())], group='DO NOT USE', label='Image caption')), ('textimage', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock()), ('alignment', wagtailio.utils.blocks.SimpleImageFormatChoiceBlock())], group='DO NOT USE', icon='image')), ('colourtext', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())], group='DO NOT USE', icon='pilcrow')), ('calltoaction', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('background', wagtailio.utils.blocks.BackgroundColourChoiceBlock())], group='DO NOT USE', icon='pilcrow')), ('tripleimage', wagtail.blocks.StructBlock([('first_image', wagtail.images.blocks.ImageChooserBlock()), ('second_image', wagtail.images.blocks.ImageChooserBlock()), ('third_image', wagtail.images.blocks.ImageChooserBlock())], group='DO NOT USE', icon='image')), ('stats', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('stat', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())], icon='code'), group='DO NOT USE')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code', template='patterns/components/streamfields/embed/embed.html')), ('markdown', wagtailio.utils.blocks.MarkDownBlock(template='patterns/components/streamfields/code_block/code_block.html')), ('codeblock', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('django', 'Django templating language'), ('html', 'HTML'), ('javascript', 'Javascript'), ('python', 'Python'), ('scss', 'SCSS')])), ('code', wagtail.blocks.TextBlock())], template='patterns/components/streamfields/code_block/code_block.html')), ('backers', wagtail.blocks.StructBlock([('gold_backers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))]))), ('silver_backers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))]))), ('bronze_backers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock(required=False))]))), ('linked_backers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock(required=False))]))), ('named_backers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock())])))], group='DO NOT USE')), ('teaser', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(page_type=['blog.BlogPage'], required=False)), ('url_chooser', wagtail.blocks.URLBlock(required=False)), ('image_for_external_link', wagtail.images.blocks.ImageChooserBlock(required=False)), ('heading_for_external_link', wagtail.blocks.TextBlock(required=False)), ('subheading_for_ext_link', wagtail.blocks.TextBlock(label='Subheading for external link', required=False))], group='CTA options')), ('get_started_block', wagtail.snippets.blocks.SnippetChooserBlock('core.GetStartedSnippet', group='CTA options', icon='th-list', template='patterns/components/streamfields/get_started_block/get_started_block.html')), ('sign_up_form', wagtail.snippets.blocks.SnippetChooserBlock('core.SignupFormSnippet', group='CTA options', icon='envelope-open-text', template='patterns/components/streamfields/sign_up_form_block/sign_up_form_block.html')), ('standalone_cta', wagtail.blocks.StructBlock([('cta', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(label='CTA text', max_length=255, required=False)), ('cta_page', wagtail.blocks.PageChooserBlock(label='CTA page', required=False)), ('cta_url', wagtail.blocks.URLBlock(label='CTA URL', required=False))])), ('description', wagtail.blocks.TextBlock(label='Short description', max_length=100, required=False))], group='CTA options'))], use_json_field=True),
        ),
    ]
