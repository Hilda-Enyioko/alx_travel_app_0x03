from alx_travel_app.celery import shared_task
from django.core.mail import send_mail
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation_email(email, booking_reference):
    send_mail(
        subject="Payment Successful!!",
        message=f"Your payment for booking {booking_reference} was successful.",
        from_email="noreply@airbnb.com",
        recipient_list=[email],
        fail_silently=False,
    )

@shared_task
def send_booking_confirmation_email(booking_id, customer_email):
    subject = "Booking Confirmation"
    message = f"Your booking (ID: {booking_id}) has been successfully created."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False
    )
