#wishRock.py의 업그레이드버전

#전체화면 모드가 가능해짐

#wishRock_2.py

import tkinter as tk
from tkinter import PhotoImage, Text, Button, Canvas
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path

entry_1 = None
generate_button = None

client = ElevenLabs(api_key="your-api-key")

def generate_voice():
    text = entry_1.get("1.0", "end-1c")
    if text.strip():
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ", 
            model="eleven_multilingual_v2"
        )
        play(audio)

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("WishRock")
window.geometry("1280x720")
window.minsize(640, 360)
window.configure(bg="#FFFFFF")

# 전체화면 모드 활성화 및 해제 기능
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

scene_num = 1
scenes = [f"scene_{i}.png" for i in range(1, 18)]

# Canvas 설정
canvas = tk.Canvas(window, bg="#FFFFFF", highlightthickness=0)
canvas.pack(fill="both", expand=True)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\yesju\OneDrive\바탕 화면\wishRock")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_widget_positions(event=None):
    """전체화면 모드에서 위젯의 크기와 위치를 조정하는 함수"""
    canvas_width = event.width
    canvas_height = event.height

    # 텍스트 상자 위치 및 크기 조정
    entry_1.place(x=canvas_width * 0.15, y=canvas_height * 0.45, 
                  width=canvas_width * 0.68, height=canvas_height * 0.12)
    
    # 버튼 위치 및 크기 조정
    generate_button.place(x=canvas_width * 0.15, y=canvas_height * 0.6, 
                          width=canvas_width * 0.68, height=canvas_height * 0.12)

def create_input_text_button():
    global entry_1, generate_button
    
    # 텍스트 입력 상자 설정
    entry_1 = Text(window, bd=0, bg="#E5D9CD", fg="#000000", highlightthickness=0)
    entry_1.place(x=189.0, y=316.0, width=875.0, height=84.0)

    # 버튼 설정
    generate_button_image = PhotoImage(file=relative_to_assets("sc17_Button.png"))
    generate_button = Button(window, image=generate_button_image, borderwidth=0, 
                             highlightthickness=0, command=generate_voice, relief="flat")
    generate_button.place(x=189.0, y=400.0, width=875.0, height=84.0)

    # 창 크기 조정 시 위젯 위치 업데이트
    window.bind("<Configure>", update_widget_positions)

def load_scene(scene_name):
    """주어진 이미지 파일을 캔버스에 로드하는 함수"""
    image_path = f"C:/Users/yesju/OneDrive/바탕 화면/wishU/{scene_name}"
    try:
        image = PhotoImage(file=image_path)
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.image = image
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")

def next_scene(event=None):
    """다음 장면으로 전환"""
    global scene_num
    if scene_num < 17:
        scene_num += 1
        if scene_num == 9:
            load_scene("scene_9.png")
            create_input_text_button()
        elif scene_num == 17:
            load_scene("scene_17.png")
            create_input_text_button()
        else:
            load_scene(f"scene_{scene_num}.png")

# 첫 장면 로드
load_scene(scenes[0])

# 클릭 시 다음 장면으로 이동
window.bind("<Button-1>", next_scene)

# 메인 루프 실행
window.mainloop()
