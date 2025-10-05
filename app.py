from flask import Flask, request, render_template_string

app = Flask(__name__)
history = []  # Danh sách lưu lịch sử kiểm tra

def is_prime(n):
    i = 2
    while i * i <= n and n % i != 0:
        i += 1
    return i * i > n and n > 1

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            n = int(request.form["number"])
            check = is_prime(n)
            result = f"{n} là số nguyên tố" if check else f"{n} không phải là số nguyên tố"
            history.append((n, "Nguyên tố" if check else "Không nguyên tố"))
        except:
            result = "Vui lòng nhập số nguyên hợp lệ."
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kiểm tra số nguyên tố</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body class="container mt-5">
        <h2 class="mb-4">🔍 Kiểm tra số nguyên tố</h2>
        <form method="post" class="mb-3">
            <input type="text" name="number" class="form-control" placeholder="Nhập số nguyên">
            <button type="submit" class="btn btn-primary mt-2">Kiểm tra</button>
        </form>
        {% if result %}
            <div class="alert alert-info">{{ result }}</div>
        {% endif %}
        <h4>Lịch sử kiểm tra:</h4>
        <ul class="list-group">
            {% for item in history %}
                <li class="list-group-item">{{ item[0] }} → {{ item[1] }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''', result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)

