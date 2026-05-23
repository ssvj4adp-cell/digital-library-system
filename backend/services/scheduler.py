"""
نظام جدولة المهام المتكررة
Background Scheduler for Daily Tasks
"""

import schedule
import time
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email_service import EmailService

load_dotenv()


class LibraryScheduler:
    """
    جدولة المهام المتكررة في المكتبة:
    - إرسال التنبيهات اليومية
    - حساب الغرامات
    - تنظيف بيانات قاعدة البيانات
    """

    def __init__(self):
        self.email_service = EmailService()
        self.reminder_time = os.getenv('DAILY_REMINDER_TIME', '08:00')
        self.daily_fine_rate = float(os.getenv('DAILY_FINE_RATE', 5))

    def schedule_jobs(self):
        """
        جدولة جميع المهام المتكررة
        """
        # جدولة التنبيهات اليومية
        schedule.every().day.at(self.reminder_time).do(self.send_daily_reminders)

        # جدولة حساب الغرامات (كل ساعة)
        schedule.every().hour.do(self.calculate_daily_fines)

        # جدولة تنظيف البيانات (كل 3 أيام)
        schedule.every(3).days.do(self.cleanup_old_data)

        print("✅ تم جدولة جميع المهام")

    def send_daily_reminders(self):
        """
        إرسال التنبيهات اليومية للطلاب ذوي الكتب المتأخرة
        """
        print(f"\n📧 جاري إرسال التنبيهات اليومية في {datetime.now()}")

        try:
            # هنا يتم الاتصال بـ API للحصول على الطلاب الذين لديهم كتب متأخرة
            # مثال:
            # students_with_overdue = get_students_with_overdue_books()

            # for student in students_with_overdue:
            #     self.email_service.send_overdue_reminder(
            #         student['name'],
            #         student['email'],
            #         student['overdue_books']
            #     )

            print("✅ تم إرسال التنبيهات بنجاح")

        except Exception as e:
            print(f"❌ خطأ في إرسال التنبيهات: {str(e)}")

    def calculate_daily_fines(self):
        """
        حساب الغرامات اليومية للكتب المتأخرة
        """
        print(f"💰 جاري حساب الغرامات اليومية في {datetime.now()}")

        try:
            # هنا يتم الاتصال بـ API لتحديث الغرامات
            # مثال:
            # overdue_circulations = get_overdue_circulations()

            # for circulation in overdue_circulations:
            #     days_late = calculate_days_late(circulation['due_date'])
            #     fine = days_late * self.daily_fine_rate
            #     update_fine(circulation['id'], fine)

            print("✅ تم تحديث الغرامات")

        except Exception as e:
            print(f"❌ خطأ في حساب الغرامات: {str(e)}")

    def cleanup_old_data(self):
        """
        تنظيف البيانات القديمة (السجلات المؤرشفة)
        """
        print(f"🧹 جاري تنظيف البيانات القديمة في {datetime.now()}")

        try:
            # يتم حذف السجلات القديمة التي تجاوزت سنة واحدة
            # مثال:
            # old_archived_records = get_archived_before(datetime.now() - timedelta(days=365))
            # for record in old_archived_records:
            #     delete_record(record['id'])

            print("✅ تم تنظيف البيانات القديمة")

        except Exception as e:
            print(f"❌ خطأ في تنظيف البيانات: {str(e)}")

    def run(self):
        """
        تشغيل جدولة المهام
        """
        print("🚀 بدء جدولة المهام...")
        self.schedule_jobs()

        # حلقة المراقبة المستمرة
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # فحص المهام كل دقيقة
            except KeyboardInterrupt:
                print("\n⛔ تم إيقاف جدولة المهام")
                break
            except Exception as e:
                print(f"❌ خطأ في حلقة جدولة المهام: {str(e)}")
                time.sleep(60)


if __name__ == "__main__":
    scheduler = LibraryScheduler()
    scheduler.run()
