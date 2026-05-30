import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
from ultralytics import YOLO

MODEL_PATH = "runs/detect/foods_model/weights/best.pt"

NUTRITION = {
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
    "干煸四季豆": {"calorie": 90, "protein": 2.5, "fat": 5.0, "carb": 9.0},
}


@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


def count_dishes(results, model):
    dish_count = {}
    for r in results:
        if r.boxes is None or len(r.boxes) == 0:
            continue
        for cls_id in r.boxes.cls:
            name = model.names[int(cls_id)]
            dish_count[name] = dish_count.get(name, 0) + 1
    return dish_count


def calc_nutrition(dish_count, single_weight):
    rows = []
    total_cal = total_pro = total_fat = total_carb = 0

    for name, cnt in dish_count.items():
        n = NUTRITION[name]
        cal = round(n["calorie"] * cnt * single_weight / 100)
        pro = round(n["protein"] * cnt * single_weight / 100, 1)
        fat = round(n["fat"] * cnt * single_weight / 100, 1)
        carb = round(n["carb"] * cnt * single_weight / 100, 1)

        total_cal += cal
        total_pro += pro
        total_fat += fat
        total_carb += carb

        rows.append({
            "菜品": name,
            "份数": cnt,
            "热量(千卡)": cal,
            "蛋白质(g)": pro,
            "脂肪(g)": fat,
            "碳水(g)": carb,
        })

    return rows, {
        "总热量(千卡)": total_cal,
        "总蛋白质(g)": round(total_pro, 1),
        "总脂肪(g)": round(total_fat, 1),
        "总碳水(g)": round(total_carb, 1),
    }


def main():
    st.set_page_config(
        page_title="食堂菜品营养识别",
        page_icon="🍽️",
        layout="wide",
    )

    st.title("🍽️ 食堂菜品识别 & 营养热量计算")
    st.caption("上传餐盘图片，自动框选菜品并估算营养成分")

    with st.sidebar:
        st.header("参数设置")
        conf = st.slider("置信度阈值", 0.1, 0.9, 0.5, 0.05)
        single_weight = st.number_input("单份重量(克)", min_value=50, max_value=500, value=150, step=10)
        st.divider()
        st.markdown("**支持识别 17 类菜品**")
        for name in NUTRITION:
            st.text(f"• {name}")

    uploaded = st.file_uploader("上传菜品图片", type=["jpg", "jpeg", "png", "webp"])

    if uploaded is None:
        st.info("请在上方选择一张食堂餐盘图片开始识别")
        example_path = "runs/detect/foods_model/val_batch1_labels.jpg"
        try:
            st.image(example_path, caption="识别效果示例（带框标注）", use_container_width=True)
        except Exception:
            pass
        return

    image = Image.open(uploaded).convert("RGB")
    col_orig, col_result = st.columns(2)

    with col_orig:
        st.subheader("原图")
        st.image(image, use_container_width=True)

    with st.spinner("正在识别菜品..."):
        model = load_model()
        results = model.predict(source=np.array(image), conf=conf, verbose=False)
        annotated = results[0].plot()
        annotated_rgb = annotated[:, :, ::-1]

    with col_result:
        st.subheader("识别结果")
        st.image(annotated_rgb, use_container_width=True)

    dish_count = count_dishes(results, model)

    if not dish_count:
        st.warning("未检测到菜品，请尝试更换图片或降低置信度阈值")
        return

    rows, totals = calc_nutrition(dish_count, single_weight)

    st.subheader("各菜品营养明细")
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.subheader("总营养摄入")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("总热量", f"{totals['总热量(千卡)']} 千卡")
    m2.metric("总蛋白质", f"{totals['总蛋白质(g)']} g")
    m3.metric("总脂肪", f"{totals['总脂肪(g)']} g")
    m4.metric("总碳水", f"{totals['总碳水(g)']} g")


if __name__ == "__main__":
    main()
