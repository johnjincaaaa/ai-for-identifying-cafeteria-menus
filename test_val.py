from ultralytics import YOLO

# ===================== 加载训练好的模型 =====================
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

# 单份标准重量（克）
single_serving = 150

if __name__ == '__main__':
    # ===================== 测试图片（把这里改成你的图片路径） =====================
    IMAGE_PATH = r"D:\Python\dectrypto\006\q\crawl\2_5月24日_食堂菜品营养预测模型\dataset\images\val\n42.jpg"  # 👈 改成你要测试的图片名

    # 开始识别
    results = model.predict(
        source=IMAGE_PATH,
        save=True,  # 自动保存带框的结果图
        show=True,  # 自动弹出图片窗口
        conf=0.5  # 置信度阈值
    )

    # ===================== 统计识别结果 =====================
    dish_counter = {}
    for res in results:
        for cls in res.boxes.cls:
            dish_name = model.names[int(cls)]
            dish_counter[dish_name] = dish_counter.get(dish_name, 0) + 1

    # ===================== 营养计算 & 打印 =====================
    print("\n" + "=" * 60)
    print("🍽️  菜品识别结果 & 营养成分计算")
    print("=" * 60)

    total_cal = 0
    total_pro = 0
    total_fat = 0
    total_carb = 0

    for name, num in dish_counter.items():
        n = nutrition[name]

        cal = n["calorie"] * num * single_serving / 100
        pro = n["protein"] * num * single_serving / 100
        fat = n["fat"] * num * single_serving / 100
        carb = n["carb"] * num * single_serving / 100

        total_cal += cal
        total_pro += pro
        total_fat += fat
        total_carb += carb

        print(f"✅ {name} × {num} 份")
        print(f"   热量：{round(cal)} 千卡")
        print(f"   蛋白质：{round(pro, 1)}g  脂肪：{round(fat, 1)}g  碳水：{round(carb, 1)}g\n")

    print("🔥 总营养摄入")
    print(f"总热量：{round(total_cal)} 千卡")
    print(f"总蛋白质：{round(total_pro, 1)}g")
    print(f"总脂肪：{round(total_fat, 1)}g")
    print(f"总碳水：{round(total_carb, 1)}g")
    print("=" * 60)