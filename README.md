# منظومة المكتبة الإلكترونية - Digital Library System

## 📚 نظرة عامة
منظومة متكاملة لإدارة المكتبات الجامعية بناءً على معمارية **Three-Tier Architecture** مع دعم كامل للعربية والإنجليزية.

## 🏗️ المعمارية الهندسية

```
┌─────────────────────────────────────────────────────────┐
│        طبقة الواجهة (Presentation Layer - UI)          │
│  (React Dashboard, Student Portal, Admin Interface)    │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│    طبقة منطق العمل (Business Logic Layer - BLL)       │
│ (Validation, Rules, Fine Calculation, Reservations)   │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│   طبقة الوصول للبيانات (Data Access Layer - DAL)     │
│        (Database Queries, SQL Operations)              │
└─────────────────────────────────────────────────────────┘
```

## 🔑 المكونات الرئيسية

### 1️⃣ نظام إدارة الصلاحيات (RBAC)
- **Admin (مسؤول النظام)**: التحكم الكامل بالمنظومة
- **Librarian (موظف المكتبة)**: إدارة العمليات اليومية
- **Student (الطالب)**: الوصول المحدود للخدمات

### 2️⃣ إدارة الفهرس والكتب (Book Catalog)
- البحث الذكي مع Filter-on-type
- الفهرسة التلقائية عبر Z39.50 API
- تصنيف ديوي العشري (DDC)

### 3️⃣ إدارة الإعارة والترجيع (Circulation)
- معالجة عمليات الإعارة والترجيع
- حساب الغرامات التلقائي
- نظام حجز الكتب (Queue - FIFO)

### 4️⃣ إدارة الطلاب (Member Directory)
- بيانات الطالب الشاملة
- ربط SSO مع النظام الأكاديمي
- تتبع حالة الحساب

### 5️⃣ الخدمات المتقدمة
- مستودع رقمي آمن (E-Repository)
- نظام الإشعارات والبريد التلقائي
- سجل العمليات الأمني (Audit Trail)

## 🛠️ التقنيات المستخدمة

| الطبقة | التقنية |
|--------|---------|
| Frontend | React.js, Redux, Tailwind CSS, i18n |
| Backend | Node.js, Express.js, JWT, bcrypt |
| Database | PostgreSQL, Sequelize ORM |
| Security | bcrypt, Parameterized Queries, Helmet |
| APIs | Z39.50, Email Service, JWT Auth |

## 📁 هيكل المشروع

```
digital-library-system/
├── backend/
├── frontend/
├── database/
├── docs/
└── docker-compose.yml
```

## 🚀 البدء السريع

### المتطلبات
- Node.js v16+
- PostgreSQL 12+
- npm أو yarn

## 📄 الترخيص

MIT License
