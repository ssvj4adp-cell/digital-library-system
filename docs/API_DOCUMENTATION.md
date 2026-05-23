# وثائق API - منظومة المكتبة الإلكترونية

## عنوان الخادم الأساسي
```
BASE_URL = http://localhost:5000/api
```

## رؤوس الطلب المطلوبة
```
Content-Type: application/json
Authorization: Bearer {JWT_TOKEN}
```

---

## 🔐 المصادقة (Authentication)

### تسجيل الدخول
```http
POST /auth/login
Content-Type: application/json

{
  "username": "student_user",
  "password": "password123"
}
```

**الرد الناجح (200):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "user": {
      "id": 1,
      "username": "student_user",
      "email": "student@university.edu",
      "full_name": "محمد أحمد",
      "role": "student",
      "student_id": "20200001"
    }
  }
}
```

---

### تسجيل حساب جديد
```http
POST /auth/register
Content-Type: application/json

{
  "username": "new_student",
  "email": "student@university.edu",
  "password": "securePassword123",
  "full_name": "أحمد محمد علي",
  "student_id": "20200001",
  "college": "كلية العلوم"
}
```

---

## 📚 الكتب (Books)

### البحث عن الكتب
```http
GET /books/search?title=البرمجة&author=أحمد&category=علوم_حاسوب&page=1&limit=10
Authorization: Bearer {TOKEN}
```

**الرد:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "isbn": "978-3-16-148410-0",
      "title": "البرمجة بلغة Python",
      "authors": ["أحمد محمد"],
      "publisher": "دار النشر",
      "publication_year": 2020,
      "category": "علوم الحاسوب",
      "ddc_number": "005.3",
      "total_copies": 5,
      "available_copies": 3,
      "cover_image_url": "..."
    }
  ],
  "pagination": {
    "total": 45,
    "page": 1,
    "limit": 10,
    "totalPages": 5
  }
}
```

---

### إضافة كتاب جديد (موظف المكتبة فقط)
```http
POST /books
Authorization: Bearer {LIBRARIAN_TOKEN}
Content-Type: application/json

{
  "isbn": "978-3-16-148410-0",
  "title": "البرمجة بـ JavaScript",
  "authors": ["محمد علي", "فاطمة أحمد"],
  "publisher": "دار النشر الحديثة",
  "publication_year": 2023,
  "category": "علوم الحاسوب",
  "ddc_number": "005.3",
  "total_copies": 5
}
```

---

## 🔄 الإعارة والترجيع (Circulation)

### إعارة كتاب (موظف المكتبة فقط)
```http
POST /circulation/checkout
Authorization: Bearer {LIBRARIAN_TOKEN}
Content-Type: application/json

{
  "user_id": 15,
  "book_id": 3
}
```

**الرد:**
```json
{
  "success": true,
  "message": "Book checked out successfully",
  "data": {
    "circulation_id": 42,
    "book_title": "البرمجة بـ JavaScript",
    "due_date": "2024-06-15",
    "days_available": 14
  }
}
```

---

### ترجيع كتاب (موظف المكتبة فقط)
```http
POST /circulation/checkin
Authorization: Bearer {LIBRARIAN_TOKEN}
Content-Type: application/json

{
  "circulation_id": 42
}
```

**الرد:**
```json
{
  "success": true,
  "message": "Book checked in successfully",
  "data": {
    "book_title": "البرمجة بـ JavaScript",
    "return_date": "2024-06-10",
    "fine_amount": 0,
    "status": "returned"
  }
}
```

---

### الكتب المستعارة للطالب
```http
GET /circulation/user/{user_id}/borrowed
Authorization: Bearer {TOKEN}
```

---

## 👤 المستخدمون (Users)

### الملف الشخصي
```http
GET /users/profile
Authorization: Bearer {TOKEN}
```

---

### تحديث البيانات الشخصية
```http
PUT /users/profile
Authorization: Bearer {TOKEN}
Content-Type: application/json

{
  "email": "newemail@university.edu",
  "phone": "+966501234567",
  "college": "كلية الهندسة"
}
```

---

### تغيير كلمة المرور
```http
POST /users/change-password
Authorization: Bearer {TOKEN}
Content-Type: application/json

{
  "current_password": "oldPassword123",
  "new_password": "newSecurePassword456"
}
```

---

## ⚙️ إدارة النظام (Admin Only)

### قائمة المستخدمين
```http
GET /admin/users
Authorization: Bearer {ADMIN_TOKEN}
```

---

### إضافة موظف جديد
```http
POST /admin/users
Authorization: Bearer {ADMIN_TOKEN}
Content-Type: application/json

{
  "username": "librarian_1",
  "email": "librarian@university.edu",
  "password": "securePass123",
  "full_name": "فاطمة محمد",
  "role": "librarian"
}
```

---

### تحديث حالة الحساب
```http
PUT /admin/users/{user_id}/status
Authorization: Bearer {ADMIN_TOKEN}
Content-Type: application/json

{
  "status": "active" // active, frozen, suspended
}
```

---

### الحصول على إعدادات النظام
```http
GET /admin/settings
Authorization: Bearer {ADMIN_TOKEN}
```

---

### تحديث إعدادات النظام
```http
PUT /admin/settings
Authorization: Bearer {ADMIN_TOKEN}
Content-Type: application/json

{
  "daily_fine_rate": 5,
  "max_borrow_days_student": 14,
  "max_borrow_days_staff": 30,
  "max_books_per_student": 5,
  "renewal_limit": 2,
  "library_email": "library@university.edu"
}
```

---

### سجل العمليات (Audit Log)
```http
GET /admin/audit-logs?limit=100&offset=0&action=checkout&user_id=15
Authorization: Bearer {ADMIN_TOKEN}
```

---

### إحصائيات النظام
```http
GET /admin/statistics
Authorization: Bearer {ADMIN_TOKEN}
```

**الرد:**
```json
{
  "success": true,
  "data": {
    "totalUsers": 350,
    "activeUsers": 320,
    "totalBooks": 2500,
    "borrowedBooks": 450,
    "availableBooks": 2050
  }
}
```

---

## 🔌 أكواد الأخطاء

| الكود | الرسالة | الحل |
|------|--------|------|
| 400 | Bad Request | تحقق من صحة البيانات المُرسلة |
| 401 | Unauthorized | التحقق من صحة التوكن |
| 403 | Forbidden | لا توجد صلاحيات كافية |
| 404 | Not Found | المورد غير موجود |
| 500 | Server Error | خطأ في الخادم |

---

## 📝 ملاحظات مهمة

1. جميع التواريخ بصيغة `YYYY-MM-DD`
2. جميع الأوقات بصيغة UTC
3. التوكن ينتهي بعد 24 ساعة
4. استخدم HTTPS في بيئة الإنتاج
5. جميع الطلبات تتطلب `Authorization` header ما لم يُذكر غير ذلك

