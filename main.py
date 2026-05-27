from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")

    # 关键修复：workers=0 关闭多进程，彻底解决页面文件错误
    model.train(
        data="data.yaml",
        epochs=30,
        imgsz=640,
        batch=8,
        patience=8,
        name="two_food_model",
        workers=0  # 👈 加上这个！
    )