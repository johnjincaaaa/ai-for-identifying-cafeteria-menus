from ultralytics import YOLO
import json

# 加载你训练好的 17 类菜品模型
model = YOLO("runs/detect/foods_model/weights/best.pt")

# ===================== 17类菜品营养数据（已补全）=====================
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

# 单份重量（克）
single_weight = 150

if __name__ == '__main__':
    # 打开摄像头实时识别
    results = model.predict(source=0, show=True, conf=0.5)

    # 统计识别到的菜品
    dish_count = {}
    for r in results:
        for cls_id in r.boxes.cls:
            dish_name = model.names[int(cls_id)]
            dish_count[dish_name] = dish_count.get(dish_name, 0) + 1

    # ===================== 输出营养结果 =====================
    print("\n" + "=" * 50)
    print("🍽️ 食堂菜品识别 & 营养热量计算")
    print("=" * 50)

    total_cal = 0
    total_protein = 0.0
    total_fat = 0.0
    total_carb = 0.0

    for name, cnt in dish_count.items():
        data = nutrition[name]

        cal = data["calorie"] * cnt * single_weight / 100
        pro = data["protein"] * cnt * single_weight / 100
        fat = data["fat"] * cnt * single_weight / 100
        carb = data["carb"] * cnt * single_weight / 100

        total_cal += cal
        total_protein += pro
        total_fat += fat
        total_carb += carb

        print(f"✅ {name} ×{cnt} 份")
        print(f"   热量：{round(cal)} 千卡")
        print(f"   蛋白质：{round(pro, 1)}g  脂肪：{round(fat, 1)}g  碳水：{round(carb, 1)}g\n")

    print("🔥 总摄入营养")
    print(f"总热量：{round(total_cal)} 千卡")
    print(f"总蛋白质：{round(total_protein, 1)}g")
    print(f"总脂肪：{round(total_fat, 1)}g")
    print(f"总碳水化合物：{round(total_carb, 1)}g")
    print("=" * 50)