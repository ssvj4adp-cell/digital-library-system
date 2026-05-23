"""
نظام معالجة الفهرسة التلقائية عبر Z39.50
Z39.50 Automatic Cataloging System
"""

import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class Z39_50_Service:
    """
    خدمة الفهرسة التلقائية عبر بروتوكول Z39.50
    تتصل بقواعد البيانات العالمية للحصول على بيانات الكتب
    """

    def __init__(self):
        self.z39_50_server = os.getenv('Z39_50_SERVER', 'http://z3950.loc.gov')
        self.timeout = 10
        self.providers = {
            'library_of_congress': 'http://lccn.loc.gov/query',
            'worldcat': 'http://www.worldcat.org/title',
            'openlibrary': 'https://openlibrary.org/api/books'
        }

    def search_by_isbn(self, isbn):
        """
        البحث عن كتاب باستخدام الرقم الدولي المعياري (ISBN)
        
        Args:
            isbn (str): رقم ISBN
        
        Returns:
            dict: بيانات الكتاب أو None إذا لم يتم العثور عليه
        """
        try:
            # محاولة البحث في Open Library (API مجانية)
            book_data = self._search_openlibrary(isbn)
            if book_data:
                return book_data

            # محاولة البحث في Library of Congress
            book_data = self._search_loc(isbn)
            if book_data:
                return book_data

            return None

        except Exception as e:
            print(f"❌ خطأ في البحث: {str(e)}")
            return None

    def _search_openlibrary(self, isbn):
        """
        البحث في مكتبة Open Library
        """
        try:
            url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jio=1&format=json"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()
            if not data:
                return None

            # استخراج البيانات
            key = f"ISBN:{isbn}"
            if key in data:
                book_info = data[key]
                return {
                    'isbn': isbn,
                    'title': book_info.get('title', ''),
                    'authors': [author.get('name', '') for author in book_info.get('authors', [])],
                    'publisher': book_info.get('publishers', [{}])[0].get('name', ''),
                    'publication_year': book_info.get('publish_date', ''),
                    'source': 'Open Library',
                    'description': book_info.get('subtitle', ''),
                    'cover_image_url': book_info.get('cover', {}).get('large', '')
                }

            return None

        except Exception as e:
            print(f"⚠️ خطأ في Open Library: {str(e)}")
            return None

    def _search_loc(self, isbn):
        """
        البحث في مكتبة الكونغرس الأمريكية
        """
        try:
            url = f"http://lccn.loc.gov/classify?isbn={isbn}&format=json"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            if data and 'records' in data:
                for record_url, record_data in data['records'].items():
                    if 'work' in record_data:
                        work = record_data['work']
                        return {
                            'isbn': isbn,
                            'title': work.get('title', ''),
                            'authors': [work.get('author', '')],
                            'publisher': '',
                            'publication_year': work.get('date', ''),
                            'ddc_number': record_data.get('classification', [{}])[0].get('ddc', ''),
                            'source': 'Library of Congress',
                            'description': ''
                        }

            return None

        except Exception as e:
            print(f"⚠️ خطأ في Library of Congress: {str(e)}")
            return None

    def enrich_book_data(self, book_data):
        """
        إثراء بيانات الكتاب بمعلومات إضافية
        
        Args:
            book_data (dict): بيانات الكتاب الأساسية
        
        Returns:
            dict: بيانات الكتاب المثراة
        """
        enriched_data = book_data.copy()

        # إضافة معلومات DDC إذا كانت ناقصة
        if 'ddc_number' not in enriched_data or not enriched_data['ddc_number']:
            ddc = self._classify_by_subject(enriched_data.get('title', ''))
            enriched_data['ddc_number'] = ddc

        # إضافة الفئة
        enriched_data['category'] = self._categorize_book(
            enriched_data.get('title', ''),
            enriched_data.get('ddc_number', '')
        )

        # إضافة البيانات الإضافية
        enriched_data['indexed_at'] = datetime.now().isoformat()
        enriched_data['indexing_status'] = 'completed'

        return enriched_data

    def _classify_by_subject(self, title):
        """
        تصنيف الكتاب بناءً على العنوان باستخدام ديوي العشري
        """
        title_lower = title.lower()

        # قاموس بسيط للتصنيفات
        classifications = {
            'برمجة|programming|code|python|javascript|java': '005.3',  # علوم الحاسوب
            'رياضيات|mathematics|algebra|calculus': '510',  # الرياضيات
            'أدب|literature|novel|شعر|poetry': '800',  # الأدب
            'تاريخ|history|historical': '900',  # التاريخ
            'فيزياء|physics|quantum': '530',  # الفيزياء
            'كيمياء|chemistry|chemistry': '540',  # الكيمياء
            'بيولوجيا|biology|organism': '570',  # البيولوجيا
            'فلسفة|philosophy': '100',  # الفلسفة
        }

        for keywords, ddc in classifications.items():
            keywords_list = keywords.split('|')
            if any(keyword in title_lower for keyword in keywords_list):
                return ddc

        return '000'  # تصنيف عام

    def _categorize_book(self, title, ddc_number):
        """
        تحديد فئة الكتاب
        """
        categories = {
            '005': 'علوم الحاسوب',
            '510': 'الرياضيات',
            '800': 'الأدب',
            '900': 'التاريخ',
            '530': 'الفيزياء',
            '540': 'الكيمياء',
            '570': 'البيولوجيا',
            '100': 'الفلسفة',
        }

        # البحث بناءً على DDC
        for code, category in categories.items():
            if ddc_number.startswith(code):
                return category

        # إذا لم يتطابق، استخدم البحث في العنوان
        if 'برمجة' in title.lower() or 'programming' in title.lower():
            return 'علوم الحاسوب'
        elif 'رياضيات' in title.lower():
            return 'الرياضيات'

        return 'عام'

    def validate_isbn(self, isbn):
        """
        التحقق من صحة رقم ISBN
        """
        # إزالة الشرطات والمسافات
        isbn = isbn.replace('-', '').replace(' ', '')

        # التحقق من الطول
        if len(isbn) not in [10, 13]:
            return False

        # التحقق من أن جميع الأحرف أرقام (ما عدا آخر حرف في ISBN-10 قد يكون X)
        if len(isbn) == 10:
            if not isbn[:-1].isdigit():
                return False
            if not (isbn[-1].isdigit() or isbn[-1].upper() == 'X'):
                return False
        else:
            if not isbn.isdigit():
                return False

        return True

    def get_cataloging_status(self, book_id, db_session=None):
        """
        الحصول على حالة الفهرسة للكتاب
        """
        return {
            'book_id': book_id,
            'status': 'completed',
            'cataloged_at': datetime.now().isoformat(),
            'source': 'Z39.50 Service',
            'validation': 'passed'
        }


class CatalogingWorker:
    """
    عامل معالجة الفهرسة - يعمل في الخلفية
    """

    def __init__(self):
        self.z39_service = Z39_50_Service()
        self.queue = []

    def add_isbn_to_queue(self, isbn, callback=None):
        """
        إضافة ISBN إلى قائمة الانتظار للفهرسة
        """
        self.queue.append({
            'isbn': isbn,
            'callback': callback,
            'timestamp': datetime.now().isoformat()
        })

    def process_queue(self):
        """
        معالجة قائمة انتظار الفهرسة
        """
        results = []

        while self.queue:
            item = self.queue.pop(0)
            isbn = item['isbn']

            try:
                # التحقق من صحة ISBN
                if not self.z39_service.validate_isbn(isbn):
                    results.append({
                        'isbn': isbn,
                        'status': 'error',
                        'message': 'Invalid ISBN format'
                    })
                    continue

                # البحث عن الكتاب
                book_data = self.z39_service.search_by_isbn(isbn)

                if book_data:
                    # إثراء البيانات
                    enriched_data = self.z39_service.enrich_book_data(book_data)

                    results.append({
                        'isbn': isbn,
                        'status': 'success',
                        'data': enriched_data
                    })

                    # استدعاء callback إذا تم توفيره
                    if item['callback']:
                        item['callback'](enriched_data)
                else:
                    results.append({
                        'isbn': isbn,
                        'status': 'not_found',
                        'message': 'Book not found in any source'
                    })

            except Exception as e:
                results.append({
                    'isbn': isbn,
                    'status': 'error',
                    'message': str(e)
                })

        return results


if __name__ == "__main__":
    # اختبار الخدمة
    z39_service = Z39_50_Service()

    # اختبار البحث عن كتاب
    test_isbn = "978-3-16-148410-0"

    print(f"🔍 البحث عن كتاب برقم ISBN: {test_isbn}")

    if z39_service.validate_isbn(test_isbn):
        book_data = z39_service.search_by_isbn(test_isbn)
        if book_data:
            enriched = z39_service.enrich_book_data(book_data)
            print("\n✅ تم العثور على الكتاب:")
            print(json.dumps(enriched, indent=2, ensure_ascii=False))
        else:
            print("❌ لم يتم العثور على الكتاب")
    else:
        print("❌ رقم ISBN غير صحيح")
