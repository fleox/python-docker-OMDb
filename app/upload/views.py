import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render


def spreadsheet_upload(request):

    credentials = {
        "type": "service_account",
        "project_id": "extreme-world-829",
        "private_key_id": "cbee36bdc285e3773aa8b745992fa9942beb0970",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAqH9Xv/5BhTB8\nTekcBjBU3v2eRK040dUv1zyqmhZnTWO5djGTHPUL+IXBdfZIe+IoBBnooXWL1kpf\nrOQn9FKKN2RYFi1Ehi5Cz7yrlovu904+yswdppTQmiDmSJGarveQbQTcchHbCag7\nC4eoj1+z6I2MyxKzNuD5bPJt5MQ86vqit7e5EjrUFegWogIUqYRedLphp39vHiDt\nw5w1CnLKGX91ddYg3jfy/ZfHfq1nN4vAdxNNcnn7r7gtJd8L6RESzmPNSiyNp4fv\nbwKI4Gkr7kaDMH0sD+6v5f6KQ2nmxrnm6okp/Hlnm73eynmeTM2DcLO6WJ1nXG6m\nx3HW0h3HAgMBAAECggEAJLg4xTXPtRc4nYiP9Iptbc+ukRrP1TORKXQhmPaTbI8A\ngdm4Kyzqu6RbgfsEvN33xd66PW+Aou1t8XxXZBIaJUPXeT6I1DWq3YsQj7e65gn2\nvNsUOlaEqJmnyZxtPAk7ICjXM1j+dDwL920EJylkeTrKt9oAr223RXLxZeajTGS8\nPrrHHAbHZCCPO5+pmyCTRMRw1SaPK1zbdiESG80y/INfmk/WZD09u/B9u3GMGA8z\nfWpZqJU29z/HpYofhbdCrXiRUwkZhmnty4nuhZIHnpsamPZ5FaM+YDT0dtKNJTbw\nT7A+Mh/tp4eillkkN70NFB0qIBLBTtcQxRWomJg3YQKBgQDkFCRIcOvCkD81pIuG\nCXeUzdzZFTjNSPF0oFfjPJVAW8zqThdroylmxoyyZmpjwSXMJ2zlufUmAtkjQj0U\nv6AiKgIMuGExDYa5+x6mscQcRyWXg9QRXFFQU0DRMx/yCbmRm0t7kHyXCp05aWsV\nsFxbhZlqk8xtOiQqLC4xlzI+MQKBgQDYPkwoQEMXp5ZwSOp/gvuy1PMCCX0OYIsD\nlwGthD8IoKB8XJBt5D/Fpt8/G0nz0yGZoP64TndAFSWM1gzmlYRhZglgs6ydJxGy\nEmfir3ueGfP23woSfjrwhCHAQFkaiQAsZuixcpkTqgxuUxHomC8E/0AHj/7eeOt2\nDXnMTfRFdwKBgCiE94kzHn9bVw91ox/18JusEw8x+PxneBYLInIJYk6jwHzj0L9b\nplBO99H95erA9rEVVABgEBBnsyHTc7yK6q0HH4QZAZNQXt4Nof1lWXzYmvIXBobr\nCrslfz9rQMKkPaaDm15hZfEDfrkjZFXfFhlgW8gWZ9wD10bywGYpAVERAoGAPD8n\nErPMvYNoi4IVK09/9rQTvEaOe/nz4R0qT4Cf2zR9YgicCLHl/phebIOa1/7Dxryv\nGwRpfwYlPxbH41pW1pgKFtIYTnR7HqS4ItUHWOYcLXS4pqxamXYGvTxwVs9CqBxH\nymCGO49OBVLJk4cK2paO7Ux2Et+Xon1gqMYzP0MCgYEAk03mQR84PnE8xEumm9xn\n2utGCaNGrgSOja3N8WDwNlkCeMrXfUuIikU9u527xrhdxkqBGJmjNlD6XSGVuDVt\n4F78v/2TO769ucXQb1/LtlU2Vdm0P+FgH45jiedRSqcc2HUGuzAoUKhXSjosRR3I\n77K87q+47RdYZ7OAOFhy9JE=\n-----END PRIVATE KEY-----\n",
        "client_email": "reparcar@extreme-world-829.iam.gserviceaccount.com",
        "client_id": "105019107357835498818",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/reparcar%40extreme-world-829.iam.gserviceaccount.com"
    }

    gc = gspread.service_account_from_dict(credentials)

    sh = gc.open("movies")
    sh.sheet1.update('A1', [[1, 2, 3], [3, 4]])
    sh.sheet1.update('B42', "it's down there somewhere, let me take another look.")

    print(sh.sheet1.get('A1'))
    
    
    return render(request, "upload.html")
