
def get_beauti_html(username: str):
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #f6f9fc;
                margin: 0;
                padding: 0;
                -webkit-font-smoothing: antialiased;
            }}
            .email-container {{
                max-width: 500px;
                margin: 40px auto;
                background: #ffffff;
                border-radius: 12px;
                box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
                overflow: hidden;
                border: 1px solid #eaedf2;
            }}
            .email-header {{
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                padding: 24px;
                text-align: center;
                color: #ffffff;
            }}
            .email-header h2 {{
                margin: 0;
                font-size: 20px;
                font-weight: 600;
                letter-spacing: -0.5px;
            }}
            .email-body {{
                padding: 32px 24px;
                color: #334155;
                font-size: 15px;
                line-height: 1.6;
            }}
            .email-body p {{
                margin: 0 0 16px 0;
            }}
            .badge {{
                display: inline-block;
                background: #f1f5f9;
                color: #475569;
                padding: 6px 12px;
                border-radius: 6px;
                font-size: 13px;
                font-weight: 500;
                margin-top: 8px;
            }}
            .email-footer {{
                background: #f8fafc;
                padding: 16px 24px;
                text-align: center;
                font-size: 13px;
                color: #94a3b8;
                border-top: 1px solid #eaedf2;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="email-header">
                <h2>Сообщение получено 🚀</h2>
            </div>
            <div class="email-body">
                <p>Здравствуйте, <strong>{username}</strong>!</p>
                <p>Ваше сообщение успешно доставлено. Спасибо за обратную связь! Я изучу информацию в ближайшее время</p>
                <p>Ожидайте ответ в течение нескольких часов.</p>
                <div class="badge">⏰ Время работы: 09:00 — 18:00</div>
            </div>
            <div class="email-footer">
                &copy; Андрей Лапко &bull; Backend Developer
            </div>
        </div>
    </body>
    </html>
    """