import cv2

capture = cv2.VideoCapture("./bug.mov") # 動画へのパス
fps = capture.get(cv2.CAP_PROP_FPS)
count = 0  # フレーム用カウンタ

while True:
    ret, frame = capture.read()
    if not ret:  # 読み込めなかった場合はループを抜ける
        break
    if int(count % fps) == 0:  # 1秒ごとにフレームを保存
        path_num = int(count // fps)
        cv2.imwrite(f"./images/{path_num:02}.png", frame)
    count += 1
