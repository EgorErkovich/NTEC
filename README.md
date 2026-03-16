# 🛒 NTEC Shop — backend‑проект (Django 1.11 + PostgreSQL + Celery + Redis + Nginx)

Проект представляет собой минимальный e‑commerce backend с товарами, производителями и заказами.  
Реализованы CRUD‑эндпоинты, загрузка CSV‑файлов, асинхронная обработка через Celery, триггеры PostgreSQL для расчёта итоговой цены, а также инфраструктура на Docker с Nginx как reverse‑proxy и HTTPS.

---

## 📌 API (краткое описание)

### **Manufacturers**
- `GET /api/manufacturers/` — список производителей  
- `POST /api/manufacturers/` — создать производителя  
- `GET /api/manufacturers/{id}/` — получить производителя  
- `PUT /api/manufacturers/{id}/` — обновить производителя  
- `PATCH /api/manufacturers/{id}/` — частичное обновление  
- `DELETE /api/manufacturers/{id}/` — удалить производителя  

---

### **Orders**
- `GET /api/orders/` — список заказов  
- `POST /api/orders/` — создать заказ  
- `GET /api/orders/{id}/` — получить заказ  
- `PATCH /api/orders/{id}/set_status/` — изменить статус заказа  
- `PATCH /api/orders/{id}/update_items/` — обновить товар и количество (только если статус = `new`)  

---

### **Products**
- `GET /api/products/` — список товаров  
- `POST /api/products/` — создать товар  
- `GET /api/products/{id}/` — получить товар  
- `PUT /api/products/{id}/` — обновить товар  
- `PATCH /api/products/{id}/` — частичное обновление  
- `DELETE /api/products/{id}/` — удалить товар  

---

### **File Upload + Celery**
- `POST /api/upload-products/` — загрузка CSV‑файла для импорта товаров  
- `GET /api/import-tasks-status/{task_id}/` — статус фоновой задачи обработки файла  

---

## 🚀 Запуск проекта

```bash
docker-compose up --build
```
 ## 🔗 Полезные ссылки
 - Swagger UI: https://localhost/swagger/

 - ReDoc: https://localhost/redoc/

 - API root: https://localhost/api/

 - Admin: https://localhost/admin/