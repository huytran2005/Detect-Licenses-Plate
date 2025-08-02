from ultralytics import YOLO
import cv2
import torch

# Kiểm tra xem GPU có sẵn không
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# Tải mô hình YOLOv8
model = YOLO('best.pt').to(device)

# Đọc hình ảnh đầu vào
img_path = 'khong-chi-ngu-quy-xe-may-bien-so-sanh-gia-khung-khong-kem-3.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img, (400, 500))


results = model(img)

for result in results:
    p = result.plot()
    cv2.imshow("YOLOv8 Detection", p)
    cv2.waitKey(0)

cv2.destroyAllWindows()

coordinates = []
for result in results:
    boxes = result.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        confidence = box.conf[0]
        class_id = box.cls[0]
        coordinates.append({
            'x1': int(x1),
            'y1': int(y1),
            'x2': int(x2),
            'y2': int(y2),
            'confidence': float(confidence),
            'class_id': int(class_id)
        })

