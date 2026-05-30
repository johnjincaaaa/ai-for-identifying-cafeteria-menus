from ultralytics import YOLO

if __name__ == '__main__':
    # 用 nano 轻量模型（速度最快，适合你小数据集）
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=30,
        imgsz=640,
        batch=8,
        patience=8,
        name="foods_model",

        # ---------- 加速核心参数 ----------
        workers=0,          # Windows 必须0，防崩溃
        amp=True,           # 混合精度：省显存 + 提速 10–20%
        device=0,            # 强制用 GPU（有独显才生效）
        cos_lr=True,         # 余弦学习率：收敛更快、更稳
        augment=True,        # 开启默认增强（小数据防过拟合）
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=10,
        fliplr=0.5,
        mosaic=1.0,          # mosaic 增强（小数据必备）

        # 显存不够就开这个：模拟更大batch
        # accumulate=2,
    )