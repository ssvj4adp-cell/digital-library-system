# لغات البرمجة المستخدمة في المشروع

## 1️⃣ JavaScript
**الاستخدام:**
- Backend API (Node.js + Express.js)
- Frontend (React.js)
- إدارة الحالة (Redux)
- البيانات الديناميكية (JSON)

**الملفات:**
```
backend/
  ├── server.js
  ├── package.json
  ├── src/
  │   ├── config/
  │   │   └── database.js
  │   ├── models/
  │   │   ├── User.js
  │   │   ├── Book.js
  │   │   ├── Circulation.js
  │   │   ├── Reservation.js
  │   │   ├── AuditLog.js
  │   │   └── SystemSettings.js
  │   ├── middleware/
  │   │   └── auth.js
  │   └── routes/
  │       ├── auth.routes.js
  │       ├── books.routes.js
  │       ├── circulation.routes.js
  │       ├── users.routes.js
  │       ├── admin.routes.js
  │       └── settings.routes.js

frontend/
  ├── package.json
  ├── src/
  │   ├── services/api.js
  │   ├── redux/
  │   │   ├── store.js
  │   │   └── authSlice.js
  │   ├── i18n/config.js
  │   └── components/Layout/Navbar.jsx
```

---

## 2️⃣ Python
**الاستخدام:**
- خدمات متقدمة في الخلفية
- معالجة البيانات والفهرسة
- جدولة المهام المتكررة
- التحليل والإحصائيات

**الملفات:**
```
backend/
  ├── requirements.txt
  ├── services/
  │   ├── email_service.py          # خدمة البريد الإلكتروني
  │   ├── cataloging_service.py     # الفهرسة التلقائية Z39.50
  │   ├── scheduler.py              # جدولة المهام المتكررة
  │   └── analytics.py              # التحليل والإحصائيات
```

**الفئات:**
- `EmailService`: إرسال الإشعارات والبريد
- `Z39_50_Service`: الفهرسة التلقائية
- `LibraryScheduler`: جدولة المهام
- `LibraryAnalytics`: التحليل والتقارير

---

## 3️⃣ SQL
**الاستخدام:**
- مخطط قاعدة البيانات (PostgreSQL)
- جداول وعلاقات البيانات
- فهارس واستعلامات

**الملفات:**
```
database/
  └── schema.sql                   # مخطط البيانات الكامل
```

**الجداول:**
- `users` - معلومات المستخدمين
- `books` - بيانات الكتب
- `circulations` - الإعارة والترجيع
- `reservations` - الحجوزات
- `audit_logs` - سجل العمليات
- `system_settings` - إعدادات النظام

---

## 4️⃣ JSON
**الاستخدام:**
- إعدادات التطبيق
- البيانات الديناميكية
- الترجمات والنصوص

**الملفات:**
```
backend/
  ├── package.json
  ├── .env.example

frontend/
  ├── package.json
  ├── .env.example
  ├── src/i18n/locales/
  │   ├── ar.json                  # الترجمات العربية
  │   └── en.json                  # الترجمات الإنجليزية
```

---

## 5️⃣ YAML
**الاستخدام:**
- إعدادات Docker
- تكوين الخدمات

**الملفات:**
```
docker-compose.yml                # إعدادات Docker والخدمات
```

---

## 6️⃣ Markdown
**الاستخدام:**
- الوثائق والتوثيق
- شرح المشروع والمعمارية

**الملفات:**
```
README.md                          # الصفحة الرئيسية
docs/
  ├── API_DOCUMENTATION.md        # توثيق الـ APIs
  ├── ARCHITECTURE.md             # شرح المعمارية
  └── LANGUAGES.md                # ملف اللغات (هذا الملف)
```

---

## 7️⃣ JSX
**الاستخدام:**
- مكونات React
- واجهة المستخدم

**الملفات:**
```
frontend/src/
  └── components/Layout/
      └── Navbar.jsx              # شريط التنقل
```

---

## 📊 الإحصائيات:

| اللغة | الملفات | الاستخدام |
|------|--------|----------|
| **JavaScript** | 20+ | Backend API + Frontend |
| **Python** | 4 | خدمات متقدمة |
| **SQL** | 1 | قاعدة البيانات |
| **JSON** | 8 | الإعدادات والترجمات |
| **YAML** | 1 | Docker |
| **Markdown** | 3+ | الوثائق |
| **JSX** | 1+ | مكونات React |

---

## 🔗 الاتصالات بين اللغات:

```
JavaScript (Node.js) ←→ Python (Background Services)
        ↓
    PostgreSQL (SQL)
        ↓
JavaScript (React) ←→ APIs

Python Services:
  - Email & Notifications
  - Cataloging (Z39.50)
  - Scheduling
  - Analytics & Reports
```

---

## 🚀 كيفية التشغيل:

### Backend (Node.js):
```bash
cd backend
npm install
npm run dev
```

### Python Services:
```bash
cd backend
pip install -r requirements.txt
python services/email_service.py
python services/scheduler.py
```

### Frontend (React):
```bash
cd frontend
npm install
npm run dev
```

---

## 📝 الملاحظات المهمة:

1. **JavaScript** يستخدم للـ APIs والواجهة الفعلية
2. **Python** يستخدم للعمليات المعقدة والخدمات الثقيلة
3. **SQL** يتعامل مع قاعدة البيانات مباشرة
4. **JSON** للإعدادات والبيانات المنظمة
5. يمكن دمج Python و Node.js عبر APIs

