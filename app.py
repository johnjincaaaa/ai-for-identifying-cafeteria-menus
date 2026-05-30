from ultralytics import YOLO
from flask import Flask, render_template, request, jsonify
import os
import uuid

# ===================== 初始化模型 =====================
model = YOLO("runs/detect/foods_model/weights/best.pt")

# ===================== 17类菜品营养数据 =====================
nutrition = {
    "番茄炒蛋": {"calorie": 120, "protein": 8.0, "fat": 8.0, "carb": 5.0},
    "红烧肉": {"calorie": 260, "protein": 19.0, "fat": 22.0, "carb": 3.5},
    "拍黄瓜": {"calorie": 25, "protein": 0.8, "fat": 0.2, "carb": 5.0},
    "米饭": {"calorie": 116, "protein": 2.7, "fat": 0.3, "carb": 25.6},
    "鸡腿": {"calorie": 180, "protein": 25.0, "fat": 8.0, "carb": 0.0},
    "凉拌海带丝": {"calorie": 30, "protein": 1.5, "fat": 0.5, "carb": 6.0},
    "口水鸡": {"calorie": 200, "protein": 22.0, "fat": 12.0, "carb": 1.0},
    "糖醋里脊": {"calorie": 180, "protein": 18.0, "fat": 8.0, "carb": 10.0},
    "宫保鸡丁": {"calorie": 190, "protein": 20.0, "fat": 9.0, "carb": 7.0},
    "炸鸡排": {"calorie": 280, "protein": 20.0, "fat": 20.0, "carb": 5.0},
    "鱼香肉丝": {"calorie": 160, "protein": 12.0, "fat": 9.0, "carb": 8.0},
    "清蒸鱼块": {"calorie": 120, "protein": 22.0, "fat": 3.0, "carb": 0.0},
    "回锅肉": {"calorie": 220, "protein": 12.0, "fat": 18.0, "carb": 3.0},
    "酸辣土豆丝": {"calorie": 80, "protein": 1.8, "fat": 0.5, "carb": 17.0},
    "麻婆豆腐": {"calorie": 150, "protein": 8.0, "fat": 10.0, "carb": 6.0},
    "炒青菜": {"calorie": 40, "protein": 1.5, "fat": 0.5, "carb": 7.0},
    "干煸四季豆": {"calorie": 90, "protein": 2.5, "fat": 5.0, "carb": 9.0}
}

# ===================== Flask 网页应用 =====================
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 单份重量
single_weight = 150


@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>🍽️ 食堂菜品营养识别系统</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: "Microsoft YaHei", sans-serif;
        }
        body {
            background: #f5f7fa;
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
        }
        .title {
            text-align: center;
            font-size: 26px;
            margin-bottom: 20px;
            color: #333;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .upload {
            text-align: center;
            padding: 20px;
        }
        #fileInput {
            padding: 8px 16px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        button {
            background: #4285f4;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #3367d6;
        }
        .result-img {
            max-width: 100%;
            border-radius: 8px;
            margin: 15px 0;
            display: none;
        }
        .result-box {
            line-height: 1.7;
            font-size: 15px;
        }
        .dish {
            padding: 10px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 8px;
        }
        .total {
            font-weight: bold;
            color: #d93025;
            font-size: 17px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="title">🍽️ 食堂菜品识别 & 营养热量计算</div>

    <div class="card">
        <div class="upload">
            <input type="file" id="fileInput" accept="image/*"><br>
            <button onclick="uploadImage()">开始识别</button>
        </div>
        <img id="resultImg" class="result-img">
        <div id="result" class="result-box"></div>
    </div>

    <script>
        function uploadImage() {
            let file = document.getElementById('fileInput').files[0];
            if (!file) {
                alert('请先选择图片');
                return;
            }
            let formData = new FormData();
            formData.append('image', file);

            fetch('/predict', {
                method: 'POST',
                body: formData
            }).then(res => res.json()).then(data => {
                document.getElementById('resultImg').src = data.image;
                document.getElementById('resultImg').style.display = 'block';

                let html = '';
                data.dishes.forEach(item => {
                    html += `<div class="dish">
                        ✅ ${item.name} × ${item.count}份<br>
                        热量：${item.cal} 千卡 | 蛋白质：${item.pro}g | 脂肪：${item.fat}g | 碳水：${item.carb}g
                    </div>`;
                });

                html += `<div class="total">
                    🔥 总热量：${data.total_cal} 千卡<br>
                    总蛋白质：${data.total_pro}g | 总脂肪：${data.total_fat}g | 总碳水：${data.total_carb}g
                </div>`;

                document.getElementById('result').innerHTML = html;
            });
        }
    </script>
</body>
</html>
    '''


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    unique_id = str(uuid.uuid4())
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_id + '.jpg')
    file.save(img_path)

    # 模型识别 + 自动保存带框的图片
    results = model.predict(
        source=img_path,
        save=True,  # 必须开，才会生成带框图片
        conf=0.5,
        project="static",
        name="predict"
    )

    # 带框图片的路径
    output_img_path = os.path.join("static/predict", os.path.basename(img_path))
    output_img_url = "/" + output_img_path.replace("\\", "/")

    # 统计菜品
    dish_count = {}
    for r in results:
        for cls_id in r.boxes.cls:
            name = model.names[int(cls_id)]
            dish_count[name] = dish_count.get(name, 0) + 1

    # 计算营养
    dishes = []
    total_cal = 0
    total_pro = 0
    total_fat = 0
    total_carb = 0

    for name, cnt in dish_count.items():
        n = nutrition[name]
        cal = round(n["calorie"] * cnt * single_weight / 100)
        pro = round(n["protein"] * cnt * single_weight / 100, 1)
        fat = round(n["fat"] * cnt * single_weight / 100, 1)
        carb = round(n["carb"] * cnt * single_weight / 100, 1)

        total_cal += cal
        total_pro += pro
        total_fat += fat
        total_carb += carb

        dishes.append({
            "name": name,
            "count": cnt,
            "cal": cal,
            "pro": pro,
            "fat": fat,
            "carb": carb
        })

    return jsonify({
        "image": output_img_url,
        "dishes": dishes,
        "total_cal": total_cal,
        "total_pro": total_pro,
        "total_fat": total_fat,
        "total_carb": total_carb
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)