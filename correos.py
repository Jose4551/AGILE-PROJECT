import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas

# Configura los detalles de tu cuenta de correo
sender_email = 'hugo.galvan8823@alumnos.udg.mx'
recipient_email = 'jose.calleros8842@alumnos.udg.mx'

# Crear el PDF
pdf_filename = "felicitacion.pdf"

c = canvas.Canvas(pdf_filename)
c.setFont("Helvetica", 12)
c.drawString(100, 750, "¡Felicitaciones José!")
c.drawString(100, 730, "Espero que tengas un día maravilloso.")
c.save()

# Crea el mensaje
subject = 'Felicitaciones'
message = """
¡Hola!

Quería felicitarte en tu día especial. Adjunto encontrarás una felicitación en formato PDF.

Saludos,
José Guillermo
"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Adjunta el PDF al mensaje
with open(pdf_filename, "rb") as pdf_file:
    pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
    pdf_attachment.add_header('content-disposition', 'attachment', filename=pdf_filename)
    msg.attach(pdf_attachment)

# Establece la conexión al servidor SMTP de tu proveedor de correo
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Cambia esto según tu proveedor de correo
    server.starttls() 
    #Credenciales remitente (correo, contraseña)
    server.login(sender_email, "")
    
    # Envía el mensaje
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("Correo con PDF enviado con éxito")
except Exception as e:
    print(f"Error al enviar el correo: {str(e)}")
