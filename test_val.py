from ultralytics import YOLO

# 加载你训练好的模型
model = YOLO("runs/detect/two_food_model-4/weights/best.pt")

# 测试 val 验证集！
if __name__ == '__main__':
    # 自动测试你所有 val 图片
    results = model.val(
        data="data.yaml",    # 自动找到你的 val 文件夹
        imgsz=640,
        batch=1,
        save=True,           # 自动保存识别后的图片！
        save_txt=True        # 保存结果文本
    )

    # 直接输出考试成绩
    print("="*60)
    print("📊 模型在 val 验证集上的考试成绩：")
    print(f"✅ 精确率 mAP50 = {results.box.map50:.2f}")
    print(f"✅ 综合得分 mAP50-95 = {results.box.map:.2f}")
    print("="*60)