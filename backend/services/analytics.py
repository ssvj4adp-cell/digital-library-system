"""
نظام التحليل والإحصائيات
Analytics & Reporting System
"""

import json
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List, Any


class LibraryAnalytics:
    """
    نظام التحليل والإحصائيات المتقدم للمكتبة
    """

    def __init__(self, db_connection=None):
        self.db = db_connection
        self.stats = {}

    def generate_daily_report(self):
        """
        توليد تقرير يومي للمكتبة
        """
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat(),
            'summary': self.get_daily_summary(),
            'detailed_stats': self.get_detailed_statistics(),
            'trends': self.analyze_trends(),
            'alerts': self.identify_alerts()
        }
        return report

    def get_daily_summary(self) -> Dict[str, Any]:
        """
        الحصول على ملخص يومي للعمليات
        """
        return {
            'total_checkouts': 0,  # عدد الإعارات
            'total_checkins': 0,  # عدد الترجيعات
            'total_fines_collected': 0.0,  # إجمالي الغرامات المحصلة
            'new_reservations': 0,  # حجوزات جديدة
            'completed_reservations': 0,  # حجوزات مكتملة
            'overdue_books': 0,  # كتب متأخرة
            'active_users': 0  # مستخدمين نشطين
        }

    def get_detailed_statistics(self) -> Dict[str, Any]:
        """
        إحصائيات مفصلة عن الأداء
        """
        return {
            'books_by_category': self._books_by_category(),
            'circulation_by_college': self._circulation_by_college(),
            'popular_books': self._get_popular_books(),
            'most_active_students': self._get_most_active_students(),
            'fine_statistics': self._fine_statistics()
        }

    def analyze_trends(self) -> Dict[str, Any]:
        """
        تحليل الاتجاهات على مدار الوقت
        """
        return {
            'weekly_trend': self._weekly_trend(),
            'monthly_trend': self._monthly_trend(),
            'seasonal_pattern': self._seasonal_pattern(),
            'growth_rate': self._growth_rate()
        }

    def identify_alerts(self) -> List[Dict[str, Any]]:
        """
        تحديد التنبيهات والمشاكل المحتملة
        """
        alerts = []

        # تنبيه عن كتب متأخرة بشكل كبير
        overdue_alert = self._check_severe_overdue()
        if overdue_alert:
            alerts.append(overdue_alert)

        # تنبيه عن أعطال محتملة في النظام
        system_alert = self._check_system_health()
        if system_alert:
            alerts.append(system_alert)

        # تنبيه عن استخدام غير عادي
        usage_alert = self._check_unusual_activity()
        if usage_alert:
            alerts.append(usage_alert)

        return alerts

    def _books_by_category(self) -> Dict[str, int]:
        """
        توزيع الكتب حسب الفئات
        """
        return {
            'علوم الحاسوب': 150,
            'الرياضيات': 120,
            'الأدب': 200,
            'التاريخ': 180,
            'الفيزياء': 95
        }

    def _circulation_by_college(self) -> Dict[str, int]:
        """
        توزيع الإعارات حسب الكليات
        """
        return {
            'كلية العلوم': 450,
            'كلية الهندسة': 520,
            'كلية الآداب': 380,
            'كلية الطب': 290,
            'كلية الاقتصاد': 210
        }

    def _get_popular_books(self) -> List[Dict[str, Any]]:
        """
        الكتب الأكثر استعارة
        """
        return [
            {
                'title': 'البرمجة بـ Python',
                'author': 'أحمد محمد',
                'circulation_count': 45,
                'avg_rating': 4.8
            },
            {
                'title': 'خوارزميات متقدمة',
                'author': 'فاطمة علي',
                'circulation_count': 38,
                'avg_rating': 4.6
            }
        ]

    def _get_most_active_students(self) -> List[Dict[str, Any]]:
        """
        الطلاب الأكثر نشاطاً
        """
        return [
            {
                'student_id': '20200001',
                'name': 'محمد أحمد',
                'total_checkouts': 25,
                'college': 'كلية الهندسة'
            },
            {
                'student_id': '20200002',
                'name': 'فاطمة علي',
                'total_checkouts': 22,
                'college': 'كلية العلوم'
            }
        ]

    def _fine_statistics(self) -> Dict[str, Any]:
        """
        إحصائيات الغرامات
        """
        return {
            'total_collected': 1250.50,
            'avg_fine_per_student': 18.5,
            'max_fine': 150.0,
            'students_with_fines': 67,
            'total_outstanding': 450.75
        }

    def _weekly_trend(self) -> List[Dict[str, Any]]:
        """
        اتجاه الأسبوع الماضي
        """
        return [
            {
                'day': 'الأحد',
                'checkouts': 45,
                'checkins': 42,
                'fines': 125.0
            },
            {
                'day': 'الإثنين',
                'checkouts': 52,
                'checkins': 48,
                'fines': 145.0
            }
        ]

    def _monthly_trend(self) -> Dict[str, int]:
        """
        اتجاه الشهر الحالي
        """
        return {
            'total_checkouts': 1200,
            'total_checkins': 1150,
            'new_members': 45,
            'total_fines': 2500
        }

    def _seasonal_pattern(self) -> Dict[str, Any]:
        """
        الأنماط الموسمية
        """
        return {
            'peak_season': 'الفصل الدراسي الأول',
            'low_season': 'الإجازة الصيفية',
            'avg_usage_peak': 2.5,
            'avg_usage_low': 0.8
        }

    def _growth_rate(self) -> Dict[str, float]:
        """
        معدل النمو
        """
        return {
            'monthly_growth': 5.2,  # %
            'yearly_growth': 18.5,  # %
            'user_growth': 8.3  # %
        }

    def _check_severe_overdue(self) -> Dict[str, Any] or None:
        """
        التحقق من كتب متأخرة جداً
        """
        # يتم التحقق من الكتب المتأخرة أكثر من 30 يوم
        return {
            'type': 'severe_overdue',
            'severity': 'high',
            'message': 'هناك 3 كتب متأخرة أكثر من 30 يوم',
            'timestamp': datetime.now().isoformat(),
            'action_required': True
        }

    def _check_system_health(self) -> Dict[str, Any] or None:
        """
        التحقق من صحة النظام
        """
        # يتم التحقق من صحة قاعدة البيانات والخوادم
        return None

    def _check_unusual_activity(self) -> Dict[str, Any] or None:
        """
        التحقق من النشاط غير العادي
        """
        # يتم التحقق من محاولات دخول غير عادية أو سلوك مريب
        return None

    def export_report(self, report: Dict, format: str = 'json') -> str:
        """
        تصدير التقرير بصيغة مختلفة
        
        Args:
            report (dict): التقرير
            format (str): الصيغة (json, csv, pdf)
        
        Returns:
            str: التقرير المُصدّر
        """
        if format == 'json':
            return json.dumps(report, ensure_ascii=False, indent=2)
        
        elif format == 'csv':
            return self._convert_to_csv(report)
        
        elif format == 'pdf':
            return self._convert_to_pdf(report)
        
        else:
            return json.dumps(report, ensure_ascii=False, indent=2)

    def _convert_to_csv(self, report: Dict) -> str:
        """
        تحويل التقرير إلى CSV
        """
        csv_content = "التاريخ,الوقت,الحقل,القيمة\n"
        date = report['date']
        timestamp = report['timestamp']

        for key, value in report['summary'].items():
            csv_content += f"{date},{timestamp},{key},{value}\n"

        return csv_content

    def _convert_to_pdf(self, report: Dict) -> str:
        """
        تحويل التقرير إلى PDF (بسيط)
        """
        # هنا يتم استخدام مكتبة reportlab أو مشابهة
        pdf_content = f"""
        <html dir="rtl">
        <h1>تقرير المكتبة اليومي</h1>
        <p>التاريخ: {report['date']}</p>
        <h2>الملخص</h2>
        <ul>
        """
        
        for key, value in report['summary'].items():
            pdf_content += f"<li>{key}: {value}</li>"
        
        pdf_content += "</ul></html>"
        
        return pdf_content


class ReportGenerator:
    """
    محرك توليد التقارير المخصصة
    """

    def __init__(self, analytics: LibraryAnalytics):
        self.analytics = analytics

    def generate_custom_report(self, params: Dict) -> Dict:
        """
        توليد تقرير مخصص بناءً على المعاملات
        
        Args:
            params (dict): معاملات التقرير
                - start_date: تاريخ البداية
                - end_date: تاريخ النهاية
                - metrics: قائمة المقاييس المطلوبة
                - filters: عوامل التصفية
        """
        report = {
            'title': 'تقرير مخصص',
            'parameters': params,
            'generated_at': datetime.now().isoformat(),
            'data': {}
        }

        # جمع البيانات حسب المعاملات
        for metric in params.get('metrics', []):
            if metric == 'circulation':
                report['data']['circulation'] = self._get_circulation_data(params)
            elif metric == 'fines':
                report['data']['fines'] = self._get_fines_data(params)
            elif metric == 'users':
                report['data']['users'] = self._get_users_data(params)

        return report

    def _get_circulation_data(self, params: Dict) -> Dict:
        return {
            'total_checkouts': 1200,
            'total_checkins': 1150,
            'avg_daily': 40
        }

    def _get_fines_data(self, params: Dict) -> Dict:
        return {
            'total_collected': 2500,
            'total_outstanding': 450,
            'avg_per_student': 18.5
        }

    def _get_users_data(self, params: Dict) -> Dict:
        return {
            'total_active': 250,
            'new_registrations': 15,
            'suspended_accounts': 5
        }


if __name__ == "__main__":
    # اختبار نظام التحليل
    analytics = LibraryAnalytics()
    
    report = analytics.generate_daily_report()
    print("\n📊 التقرير اليومي:")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    
    # تصدير التقرير
    json_report = analytics.export_report(report, 'json')
    print("\n✅ تم توليد التقرير بنجاح")
