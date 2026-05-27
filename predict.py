from ultralytics import YOLO
import json

# 加载你训练好的模型
model = YOLO("runs/detect/two_food_model-4/weights/best.pt")

# 营养数据（番茄炒蛋、红烧肉）
nutrition = {
    "番茄炒蛋": {"calorie": 120, "protein": 8.0, "fat": 8.0, "carb": 5.0},
    "红烧肉": {"calorie": 260, "protein": 19.0, "fat": 22.0, "carb": 3.5}
}

# 单份重量
single_weight = 150  # 克

if __name__ == '__main__':
    # 开始预测（会自动打开摄像头/识别图片/显示结果）
    # 你也可以改成：source="test.jpg" 识别本地图片
    results = model.predict(source=0, show=True, conf=0.5)

    # 统计识别到的菜品
    dish_count = {}
    for r in results:
        for cls_id in r.boxes.cls:
            dish_name = model.names[int(cls_id)]
            dish_count[dish_name] = dish_count.get(dish_name, 0) + 1

    # 输出营养结果
    print("\n" + "=" * 50)
    print("🍽️ 识别结果 & 营养热量计算")
    print("=" * 50)

    total_cal = 0
    for name, cnt in dish_count.items():
        cal = nutrition[name]["calorie"] * cnt * single_weight / 100
        total_cal += cal
        print(f"✅ {name} × {cnt} 份 → 热量：{round(cal)} 千卡")

    print(f"\n🔥 总摄入热量：{round(total_cal)} 千卡")
    print("=" * 50)