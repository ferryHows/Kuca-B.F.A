#wishRock_hideInputs.py의 업그레이드 버전
#영어, 한글 두 가지 버전 제공

#wishRock_12.py

import tkinter as tk
from tkinter import PhotoImage, Text, ttk
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
from PIL import Image, ImageTk

# 전역 변수들 (아직 헷갈림. 잘 이해 못함. 근데 None으로 해두면 오류가 안떠서 일단 설정해둠)
entry_1 = entry_8 = generate_button = None
voice_generated = False
inactivity_timer = next_button = None
current_language = "ko"  # 기본 언어 한국어 설정
scene_num = 1  # 시작 씬 번호

#필수코드
# ElevenLabs API 클라이언트 설정
client = ElevenLabs(api_key="sk_c4e012b0f5bca4111c1ee2fb1db327a581e2a3475150f5ee")

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("WishRock")
window.geometry("1280x720")
window.configure(bg="#FFFFFF")
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))  # ESC로 전체화면 해제

# 경로 설정 (한글 문제 방지를 위해 경로를 영문으로 관리)
ASSETS_PATH = Path(r"C:/Users/yesju/OneDrive/바탕 화면/wishRock")

def relative_to_assets(path: str) -> Path:
    """경로를 반환하는 함수"""
    return ASSETS_PATH / path

# 음성 생성 함수
def generate_voice():
    global voice_generated
    text = entry_1.get("1.0", "end-1c").strip()
    if text:
        audio = client.generate(text=text, voice="Kp8K3ZlvqyVzkQBQ2IXJ", model="eleven_multilingual_v2")
        play(audio)
        voice_generated = True

# 비활동 타이머 설정(30초 이상 활동 감지 안되면 30초 짜리 타이머가 시작됨)
def start_inactivity_timer():
    global inactivity_timer
    if inactivity_timer:
        window.after_cancel(inactivity_timer)
    inactivity_timer = window.after(30000, reset_to_scene_1)

# 비활동 시 초기 화면으로 리셋(시작된 30초에서 비활동 끝까지 유지시 씬 1로 이동)
def reset_to_scene_1():
    global scene_num, voice_generated
    scene_num = 1
    voice_generated = False
    load_scene()
    hide_all_inputs()

# 모든 입력 필드 숨기기(씬8,17의 입력필드와 버튼은 다른 씬에서는 사라지도록)
def hide_all_inputs():
    if entry_1:
        entry_1.place_forget()
    if generate_button:
        generate_button.place_forget()
    if entry_8:
        entry_8.place_forget()
    if next_button:
        next_button.place_forget()

# 텍스트 입력 및 버튼 생성 (씬 17용)
def create_input_text_button():
    global entry_1, generate_button
    entry_1 = Text(bg="#D0A6A7", wrap='word', font=("Arial Rounded MT Bold", 14))
    entry_1.place(relx=0.5, rely=0.4, anchor='center', width=875, height=124)

    generate_button = ttk.Button(text="다 적은 후, 저를 눌러 들어보세요.", command=generate_voice)
    generate_button.place(relx=0.5, rely=0.55, anchor='center', width=875, height=44)

# 꿈 입력 필드 및 버튼 생성 (씬 8용)
def create_dream_input_text_button():
    global entry_8, next_button
    entry_8 = Text(bg="#D0A6A7", wrap='word', font=("Arial Rounded MT Bold", 14))
    entry_8.place(relx=0.5, rely=0.4, anchor='center', width=875, height=124)

    next_button = ttk.Button(text="꿈을 들려주세요.", command=next_scene_from_dream)
    next_button.place(relx=0.5, rely=0.55, anchor='center', width=875, height=44)

# 언어 선택 버튼 생성(씬 5용)
def create_language_selection():
    """씬 5: 언어 선택 버튼을 생성합니다."""
    ttk.Button(text="한국어", command=lambda: select_language("ko")).place(
        relx=0.4, rely=0.5, anchor='center', width=200, height=50)
    ttk.Button(text="English", command=lambda: select_language("eng")).place(
        relx=0.6, rely=0.5, anchor='center', width=200, height=50)

def select_language(lang):
    """언어를 선택한 후 다음 씬으로 이동합니다."""
    global current_language, scene_num
    current_language = lang
    scene_num += 1  # 언어 선택 후 다음 씬(6)으로 이동
    load_scene()  # 씬을 새로 로드합니다.
    start_inactivity_timer()  # 비활동 타이머 시작
    
# 이미지 로드 및 화면 표시 함수
def load_scene():
    scene_name = f"scene_{scene_num}_{current_language}.png"
    image_path = relative_to_assets(scene_name)

    print(f"Loading image from: {image_path}")  # 경로 확인용 출력

    try:
        img = Image.open(image_path)
        width, height = window.winfo_width() or 1280, window.winfo_height() or 720
        img_resized = img.resize((width, height))
        tk_image = ImageTk.PhotoImage(img_resized)

        canvas.create_image(0, 0, anchor="nw", image=tk_image)
        canvas.image = tk_image  # 참조 유지
        canvas.update()  # 강제 갱신
    except Exception as e:
        print(f"Error loading {scene_name}: {e}")

# 창 크기 변경 시 이미지 리사이즈
def resize_image(event):
    load_scene()

# 꿈 입력 후 다음 씬으로 이동
def next_scene_from_dream():
    global scene_num
    if entry_8.get("1.0", "end-1c").strip():
        scene_num = 9
        load_scene()
        hide_all_inputs()

# 다음 장면으로 이동(씬 5에서 언어선택 후 안넘어가는 오류 해결 위해 추가한 코드. 필수코드인지는 모르겠음)
def next_scene(event=None):
    global scene_num
    if scene_num == 5:
        create_language_selection()
    elif scene_num == 8:
        create_dream_input_text_button()
    else:
        scene_num += 1
        load_scene()
        hide_all_inputs()

    start_inactivity_timer()

# 캔버스 생성
canvas = tk.Canvas(window, bg="#FFFFFF", height=720, width=1280)
canvas.pack(fill="both", expand=True)

# 창 크기 변경 이벤트와 클릭 이벤트 바인딩
window.bind("<Configure>", resize_image)
window.bind("<Button-1>", next_scene)
window.bind("<Key>", lambda event: start_inactivity_timer())
window.bind("<Motion>", lambda event: start_inactivity_timer())

# 첫 장면 로드
load_scene()

# 메인 루프 실행
window.mainloop()
