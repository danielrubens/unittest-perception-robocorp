from robocorp.tasks import task
from utilities.pdf.definitiion import HTMLConversor

@task
def convert_html_to_pdf():
    conversor = HTMLConversor()
    conversor.to_pdf()