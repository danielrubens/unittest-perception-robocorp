from robocorp.tasks import task
from utilities.pdf.definition import HTMLConversor

from __tests__.test_runner import run_test

@task
def convert_html_to_pdf():
    conversor = HTMLConversor()
    conversor.to_pdf()