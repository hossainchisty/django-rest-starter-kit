# Deployment Guide

This guide covers the steps to deploy the Django REST Starter Kit to a production environment.

## Prerequisites

- Linux server (Ubuntu 22.04 LTS recommended)
- Python 3.10+
- PostgreSQL
- Redis
- Nginx
- Domain name pointing to your server

## 1. Server Setup

Update system packages:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl git -y
```

## 2. Database Setup

Create a PostgreSQL database and user:
```bash
sudo -u postgres psql

CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'strong_password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```

## 3. Application Setup

Clone the repository:
```bash
cd /var/www
sudo git clone https://github.com/yourusername/django-rest-starter-kit.git
sudo chown -R $USER:$USER django-rest-starter-kit
cd django-rest-starter-kit
```

Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/production.txt
```

## 4. Environment Configuration

Create `.env` file:
```bash
cp .env.example .env
nano .env
```

Update the following variables:
```ini
DEBUG=False
SECRET_KEY=your-super-secret-key-generated-python
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgres://myprojectuser:strong_password@localhost:5432/myproject
DJANGO_SETTINGS_MODULE=config.settings.production
```

## 5. Gunicorn Setup

Create a systemd service file for Gunicorn:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Content:
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/django-rest-starter-kit
ExecStart=/var/www/django-rest-starter-kit/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/var/www/django-rest-starter-kit/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable Gunicorn:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

## 6. Nginx Setup

Create Nginx server block:
```bash
sudo nano /etc/nginx/sites-available/myproject
```

Content:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/django-rest-starter-kit;
    }

    location /media/ {
        root /var/www/django-rest-starter-kit;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/django-rest-starter-kit/gunicorn.sock;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 7. SSL Certificate (Let's Encrypt)

Install Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
```

Obtain certificate:
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## 8. Final Steps

Run migrations and collect static files:
```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic
```

## Docker Deployment (Alternative)

For Docker deployment, ensure you have Docker and Docker Compose installed.

1. Update `docker-compose.yml` with production settings.
2. Run:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d --build
   ```

## Monitoring

- Check Gunicorn logs: `sudo journalctl -u gunicorn`
- Check Nginx logs: `sudo tail -f /var/log/nginx/error.log`
- Check Application logs: `tail -f logs/django.log`
