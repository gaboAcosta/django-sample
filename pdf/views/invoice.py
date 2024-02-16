
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseBadRequest
from pdf.services import PDFRenderService
from pdf.serializers import InvoiceDTO


class InvoiceView(APIView):

    @staticmethod
    @api_view(['POST'])
    def render_pdf(request):
        dto = InvoiceDTO(data=request.data)
        if not dto.is_valid():
            return HttpResponseBadRequest("BAD REQUEST")
        pdf_result = PDFRenderService.render_to_pdf('invoice.html', dto.data)

        if pdf_result.error:
            return HttpResponseBadRequest("Invalid PDF")
        return HttpResponse(pdf_result.stream, content_type='application/pdf')

