


# from rest_framework.views import APIView
# from rest_framework.response import Response
# import pandas as pd
# from .outlook_mail import send_outlook_mail


# class SendBulkEmail(APIView):

#     def post(self, request):

#         subject = request.data.get("subject")
#         message = request.data.get("message")

#         excel_file = request.FILES.get("file")
#         pdf_file = request.FILES.get("pdf")

#         df = pd.read_excel(excel_file)

#         email_list = df["email"].dropna().tolist()

#         results = []

#         for email in email_list:

#             try:

#                 pdf_file.seek(0)

#                 send_outlook_mail(
#                     email,
#                     subject,
#                     message,
#                     pdf_file
#                 )

#                 results.append({
#                     "email": email,
#                     "status": "Sent"
#                 })

#             except Exception as e:

#                 results.append({
#                     "email": email,
#                     "status": "Failed"
#                 })

#         return Response({
#             "total": len(results),
#             "results": results
#         })



from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from .outlook_mail import send_outlook_mail


class SendBulkEmail(APIView):

    def post(self, request):

        subject = request.data.get("subject")
        message = request.data.get("message")

        excel_file = request.FILES.get("file")
        # pdf_file = request.FILES.get("pdf")

        df = pd.read_excel(excel_file)

        email_list = df["email"].dropna().tolist()

        results = []

        for email in email_list:

            try:

                # pdf_file.seek(0)

                send_outlook_mail(
                    email,
                    subject,
                    message
                    # pdf_file
                )

                results.append({
                    "email": email,
                    "status": "Sent"
                })

            except Exception as e:

                results.append({
                    "email": email,
                    "status": "Failed"
                })

        return Response({
            "total": len(results),
            "results": results
        })