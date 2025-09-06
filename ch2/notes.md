## 1. What is WSGI?

- **WSGI** = Web Server Gateway Interface.  
- It’s a **specification** that defines how Python web apps communicate with web servers (Apache, Nginx).  

### How WSGI works:
- User → Web server → WSGI → Python app → Response → Back to user.  
- The Python app is called a **WSGI callable**, usually a function that takes `environ` and `start_response`.  

### Key points:
- **Synchronous** → handles one request per worker at a time.  
- Best for **traditional web apps** (HTTP requests/responses).  
- Used by **Django, Flask**.  
- Django file: **`wsgi.py`**.  

---

## 2. What is ASGI?

- **ASGI** = Asynchronous Server Gateway Interface.  
- Newer standard that supports **both synchronous and asynchronous Python apps**.  

### How ASGI works:
- Like WSGI but **handles multiple requests concurrently** using **async/await**.  
- Supports **real-time communication**: WebSockets, HTTP/2, long-lived connections.  

### Key points:
- **Asynchronous** → multiple requests handled at the same time.  
- Ideal for **modern apps**: chat apps, live notifications, streaming, dashboards.  
- Backward compatible with synchronous apps.  
- Django file: **`asgi.py`**.  

---

## 3. WSGI vs ASGI (Quick Comparison)

- **Requests**:  
  - WSGI → One request at a time (sync)  
  - ASGI → Multiple requests concurrently (async)  

- **Use case**:  
  - WSGI → Normal websites  
  - ASGI → Real-time apps (chat, notifications)  

- **Protocols**:  
  - WSGI → HTTP only  
  - ASGI → HTTP + WebSockets + HTTP/2  

- **Concurrency**:  
  - WSGI → Multi-process or threads per worker  
  - ASGI → Async event loop (asyncio), threads optional  

- **Django file**:  
  - WSGI → `wsgi.py`  
  - ASGI → `asgi.py`  

- **App callable**:  
  - WSGI → Function (`environ`, `start_response`)  
  - ASGI → Coroutine (`scope`, `receive`, `send`)  

---

### Elevator Pitch (1 line each)
- **WSGI:** Sync bridge between Python app and web server, handles HTTP requests one by one.  
- **ASGI:** Async bridge, handles HTTP + WebSockets, ideal for real-time features.  
