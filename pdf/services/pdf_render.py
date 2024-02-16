
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


class PDFRenderResponse:
    stream: BytesIO
    error: str

    def __init__(self, stream, error):
        self.stream = stream
        self.error = error


class PDFRenderService:
    @staticmethod
    def render_to_pdf(template_src: str, context_dict: object) -> PDFRenderResponse:
        template = get_template(template_src)
        html = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if pdf.err:
            return PDFRenderResponse(error=pdf.err, stream=None)
        return PDFRenderResponse(stream=result.getvalue(), error=None)
