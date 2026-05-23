"""
منظومة خدمة الإشعارات والبريد الإلكتروني
Email & Notification Service for Digital Library System
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
from dotenv import load_dotenv

load_dotenv()


class EmailService:
    """خدمة البريد الإلكتروني"""

    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.sender_email = os.getenv('EMAIL_USER')
        self.sender_password = os.getenv('EMAIL_PASSWORD')
        self.library_name = os.getenv('LIBRARY_NAME', 'منظومة المكتبة الإلكترونية')

    def send_email(self, recipient_email, subject, body_html, body_text=None):
        """
        إرسال بريد إلكتروني
        
        Args:
            recipient_email (str): البريد الإلكتروني للمستقبل
            subject (str): موضوع الرسالة
            body_html (str): محتوى الرسالة بصيغة HTML
            body_text (str): محتوى الرسالة بصيغة نصية عادية
        
        Returns:
            bool: True إذا نجحت العملية، False إذا فشلت
        """
        try:
            # إنشاء الرسالة
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Date"] = datetime.now().isoformat()

            # إضافة المحتوى النصي
            if body_text:
                message.attach(MIMEText(body_text, "plain", "utf-8"))

            # إضافة محتوى HTML
            message.attach(MIMEText(body_html, "html", "utf-8"))

            # إرسال البريد
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(
                    self.sender_email,
                    recipient_email,
                    message.as_string()
                )

            print(f"✅ تم إرسال البريد بنجاح إلى {recipient_email}")
            return True

        except Exception as e:
            print(f"❌ فشل إرسال البريد: {str(e)}")
            return False

    def send_overdue_reminder(self, student_name, student_email, books_data):
        """
        إرسال تنبيه بالكتب المتأخرة
        
        Args:
            student_name (str): اسم الطالب
            student_email (str): البريد الإلكتروني للطالب
            books_data (list): قائمة الكتب المتأخرة
                [{
                    'title': 'عنوان الكتاب',
                    'due_date': '2024-06-15',
                    'days_overdue': 5,
                    'fine_amount': 25
                }]
        """
        # بناء جدول الكتب
        books_html = ""
        total_fine = 0
        
        for book in books_data:
            days_overdue = book.get('days_overdue', 0)
            fine_amount = book.get('fine_amount', 0)
            total_fine += fine_amount
            
            books_html += f"""
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="padding: 10px;">{book['title']}</td>
                <td style="padding: 10px;">{book['due_date']}</td>
                <td style="padding: 10px; color: red;">+{days_overdue} أيام</td>
                <td style="padding: 10px; color: red; font-weight: bold;">{fine_amount} ريال</td>
            </tr>
            """

        body_html = f"""
        <html dir="rtl">
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; }}
                .header {{ background-color: #2c3e50; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; background-color: #ecf0f1; }}
                .warning {{ background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; margin: 15px 0; }}
                table {{ width: 100%; border-collapse: collapse; background-color: white; }}
                th {{ background-color: #3498db; color: white; padding: 10px; text-align: right; }}
                .footer {{ text-align: center; color: #7f8c8d; font-size: 12px; padding: 20px; }}
                .button {{ background-color: #e74c3c; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📚 {self.library_name}</h1>
                    <p>تنبيه الكتب المتأخرة</p>
                </div>
                
                <div class="content">
                    <h2>مرحباً {student_name},</h2>
                    
                    <div class="warning">
                        <strong>⚠️ تنبيه مهم:</strong><br>
                        لديك كتب متأخرة الإرجاع مع ترتب غرامات عليها.
                    </div>
                    
                    <h3>الكتب المتأخرة:</h3>
                    <table>
                        <tr>
                            <th>عنوان الكتاب</th>
                            <th>تاريخ الاستحقاق</th>
                            <th>أيام التأخير</th>
                            <th>الغرامة</th>
                        </tr>
                        {books_html}
                    </table>
                    
                    <h3 style="color: #e74c3c; text-align: center;">
                        إجمالي الغرامات: <span style="font-size: 24px;">{total_fine} ريال</span>
                    </h3>
                    
                    <p style="text-align: center;">
                        <a href="http://localhost:3000/my-books" class="button">عرض كتبي</a>
                    </p>
                    
                    <p style="color: #7f8c8d; font-size: 14px;">
                        يرجى إرجاع الكتب أو تسديد الغرامات في أقرب وقت ممكن.
                    </p>
                </div>
                
                <div class="footer">
                    <p>تم إرسال هذه الرسالة تلقائياً من منظومة المكتبة الإلكترونية</p>
                    <p>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
            </div>
        </body>
        </html>
        """

        body_text = f"""
        مرحباً {student_name},

        لديك كتب متأخرة الإرجاع:

        {chr(10).join([f"- {book['title']} (تأخير: {book.get('days_overdue', 0)} أيام، غرامة: {book.get('fine_amount', 0)} ريال)" for book in books_data])}

        إجمالي الغرامات: {total_fine} ريال

        يرجى إرجاع الكتب أو تسديد الغرامات في أقرب وقت ممكن.
        """

        return self.send_email(student_email, f"تنبيه: كتب متأخرة - {self.library_name}", body_html, body_text)

    def send_reservation_ready(self, student_name, student_email, book_title):
        """
        إرسال إشعار بأن الكتاب المحجوز جاهز للاستلام
        """
        body_html = f"""
        <html dir="rtl">
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; }}
                .header {{ background-color: #27ae60; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; background-color: #d5f4e6; }}
                .success {{ background-color: #d4edda; border-left: 5px solid #28a745; padding: 15px; margin: 15px 0; }}
                .button {{ background-color: #27ae60; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 0; }}
                .footer {{ text-align: center; color: #7f8c8d; font-size: 12px; padding: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📚 {self.library_name}</h1>
                    <p>إشعار - الكتاب جاهز للاستلام</p>
                </div>
                
                <div class="content">
                    <h2>مرحباً {student_name},</h2>
                    
                    <div class="success">
                        <strong>✅ خبر سار!</strong><br>
                        الكتاب الذي قمت بحجزه متاح الآن.
                    </div>
                    
                    <h3>تفاصيل الكتاب:</h3>
                    <p style="background-color: white; padding: 15px; border-radius: 5px;">
                        <strong>العنوان:</strong> {book_title}<br>
                        <strong>الحالة:</strong> جاهز للاستلام<br>
                        <strong>تاريخ الإشعار:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </p>
                    
                    <p style="text-align: center; color: #7f8c8d;">
                        يرجى استلام الكتاب من المكتبة خلال 7 أيام من الآن.
                    </p>
                    
                    <p style="text-align: center;">
                        <a href="http://localhost:3000/my-reservations" class="button">عرض حجوزاتي</a>
                    </p>
                </div>
                
                <div class="footer">
                    <p>تم إرسال هذه الرسالة تلقائياً من منظومة المكتبة الإلكترونية</p>
                </div>
            </div>
        </body>
        </html>
        """

        return self.send_email(student_email, f"✅ كتابك جاهز - {book_title}", body_html)

    def send_checkout_confirmation(self, student_name, student_email, book_title, due_date):
        """
        إرسال تأكيد الإعارة
        """
        body_html = f"""
        <html dir="rtl">
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; }}
                .header {{ background-color: #3498db; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; background-color: #ecf0f1; }}
                .info-box {{ background-color: white; padding: 15px; border-radius: 5px; margin: 15px 0; border-left: 5px solid #3498db; }}
                .button {{ background-color: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px 0; }}
                .footer {{ text-align: center; color: #7f8c8d; font-size: 12px; padding: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📚 {self.library_name}</h1>
                    <p>تأكيد الإعارة</p>
                </div>
                
                <div class="content">
                    <h2>مرحباً {student_name},</h2>
                    
                    <p>تم استعارة الكتاب بنجاح. إليك تفاصيل الإعارة:</p>
                    
                    <div class="info-box">
                        <strong>📖 عنوان الكتاب:</strong> {book_title}<br>
                        <strong>📅 تاريخ الاستحقاق:</strong> {due_date}<br>
                        <strong>⏰ وقت الإعارة:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </div>
                    
                    <p style="color: #e74c3c; font-weight: bold;">
                        ⚠️ تذكير: يجب إرجاع الكتاب قبل تاريخ الاستحقاق لتجنب الغرامات.
                    </p>
                    
                    <p style="text-align: center;">
                        <a href="http://localhost:3000/my-books" class="button">عرض كتبي المستعارة</a>
                    </p>
                </div>
                
                <div class="footer">
                    <p>تم إرسال هذه الرسالة تلقائياً من منظومة المكتبة الإلكترونية</p>
                </div>
            </div>
        </body>
        </html>
        """

        return self.send_email(student_email, f"✅ تأكيد إعارة - {book_title}", body_html)


if __name__ == "__main__":
    # اختبار الخدمة
    email_service = EmailService()
    
    # اختبار إرسال تنبيه بالكتب المتأخرة
    books_test_data = [
        {
            'title': 'البرمجة بـ Python',
            'due_date': '2024-06-10',
            'days_overdue': 5,
            'fine_amount': 25
        },
        {
            'title': 'خوارزميات متقدمة',
            'due_date': '2024-06-12',
            'days_overdue': 3,
            'fine_amount': 15
        }
    ]
    
    result = email_service.send_overdue_reminder(
        "محمد أحمد",
        "student@university.edu",
        books_test_data
    )
    
    print(f"نتيجة الإرسال: {result}")
