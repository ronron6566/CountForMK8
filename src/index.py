import cv2
import pytesseract

# 画像の読み込み
image = cv2.imread('result_screen.jpg')

# 画像の前処理（必要に応じて）
# ...

# テキストの検出
# 例: 輪郭検出
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# テキストの認識
# Tesseractの初期化
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

points = []

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # テキスト領域の抽出
    roi = image[y:y+h, x:x+w]
    # テキストの認識
    text = pytesseract.image_to_string(roi, config='--psm 6')
    # ポイントの抽出
    try:
        points.append(int(text))
    except ValueError:
        pass

# 点数の表示
for point in points:
    print(point)
