#wishRock_betterDream의 업그레이드 버전

#next_button의 위치가 아래로 쏠리는 오류를 수정
#next_button.place_forget()을 남발해서 center로 설정해둔 위치를 처음부터 까먹는 듯
#next_button.place_forget()울 사용하지 않고, hide_all_inputs()를 만들었음
#hide_all_inputs()는 씬 8과 씬 17에서만 사용되는 기능들을 다른 씬에서는 숨기는 기능
#씬 9일 때, 30초 이상 비활동 상태 감지 타이머가 작동되어 씬 1로 리셋 될 때 hide_all_inputs()가 작동되도록 설정함

#wishRock_11.py

import tkinter as tk
from tkinter import PhotoImage, Text, ttk
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
from PIL import Image, ImageTk
from pydantic import BaseModel

entry_1 = None
entry_8 = None
generate_button = None
voice_generated = False  # 목소리 생성 여부를 나타내는 변수
inactivity_timer = None  # 비활동 타이머
next_button = None

client = ElevenLabs(
    api_key="sk_c4e012b0f5bca4111c1ee2fb1db327a581e2a3475150f5ee",
)

# 목소리 생성 함수
def generate_voice():
    global voice_generated
    text = entry_1.get("1.0", "end-1c")
    if text.strip():
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ",
            model="eleven_multilingual_v2"
        )
        play(audio)
        voice_generated = True

# 비활동 타이머 함수
def start_inactivity_timer():
    global inactivity_timer
    if inactivity_timer is not None:
        window.after_cancel(inactivity_timer)
    inactivity_timer = window.after(30000, reset_to_scene_1)

# 비활동 상태를 감지하고 타이머 리셋
def reset_to_scene_1():
    global scene_num, voice_generated, entry_1, generate_button, entry_8, next_button
    if voice_generated:
        scene_num = 1
        load_scene(f"scene_{scene_num}.png")
        voice_generated = False
        hide_all_inputs()

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("WishRock")
window.geometry("1280x720")
window.minsize(640, 360)
window.configure(bg="#FFFFFF")

# 전체화면 모드 활성화
window.attributes("-fullscreen", True)

# ESC 키로 전체화면 모드 해제
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

# 기본 변수들 설정
scene_num = 1
scenes = [f"scene_{i}.png" for i in range(1, 18)]

# 캔버스 설정
canvas = tk.Canvas(window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
canvas.pack(fill="both", expand=True)

# 경로 설정
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\yesju\OneDrive\바탕 화면\wishRock")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 숨기기 기능
def hide_all_inputs():
    """모든 입력 요소와 버튼 숨기기."""
    if entry_1:
        entry_1.place_forget()
    if generate_button:
        generate_button.place_forget()
    if entry_8:
        entry_8.place_forget()
    if next_button:
        next_button.place_forget()

#씬 17 기능
def create_input_text_button():
    global canvas, entry_1, generate_button
    entry_1 = Text(
        bd=2,
        bg="#D0A6A7",
        fg="#3D2A2D",
        highlightthickness=0,
        wrap='word',
        font=("Arial Rounded MT Bold", 14),
        relief="ridge",
        padx=10,
        pady=50
    )
    entry_1.place(
        relx=0.5,
        rely=0.4,
        anchor='center',
        width=875.0,
        height=124.0
    )

    entry_1.tag_configure("center", justify='center')
    entry_1.bind("<KeyRelease>", lambda event: entry_1.tag_add("center", "1.0", "end"))

    style = ttk.Style()
    style.configure("TButton", background="#C2A6A8", foreground="#3D2A2D", borderwidth=3, relief="ridge")

    generate_button = ttk.Button(
        canvas,
        text="다 적은 후, 저를 눌러 들어보세요.",
        style="TButton",
        command=generate_voice
    )
    generate_button.place(
        relx=0.5,
        rely=0.55,
        anchor='center',
        width=875.0,
        height=44.0
    )
#씬 8 기능
def create_dream_input_text_button():
    global canvas, entry_8, next_button
    entry_8 = Text(
        bd=2,
        bg="#D0A6A7",
        fg="#3D2A2D",
        highlightthickness=0,
        wrap='word',
        font=("Arial Rounded MT Bold", 14),
        relief="ridge",
        padx=10,
        pady=50
    )
    entry_8.place(
        relx=0.5,
        rely=0.4,
        anchor='center',
        width=875.0,
        height=124.0
    )
     # 중앙 정렬을 위한 태그 설정
    entry_8.tag_configure("center", justify='center')
    entry_8.bind("<KeyRelease>", lambda event: entry_8.tag_add("center", "1.0", "end"))
    # Button 스타일 설정
    style = ttk.Style()
    style.configure("TButton", background="#C2A6A8", foreground="#3D2A2D", borderwidth=3, relief="ridge")
    # Button 생성 (꿈 입력 후 다음 씬으로 넘어가기)
    next_button = ttk.Button(
        canvas,
        text="꿈을 들려주세요.",
        style="TButton",
        command=next_scene_from_dream
    )
    next_button.place(
        relx=0.5,
        rely=0.55,
        anchor='center',
        width=875.0,
        height=44.0
    )

def load_scene(scene_name):
    image_path = f"C:/Users/yesju/OneDrive/바탕 화면/wishRock/{scene_name}"
    try:
        img = Image.open(image_path)

        
        # 창 크기에 맞춰 리사이즈
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        resized_image = img.resize((window_width, window_height))
        tk_image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor="nw", image=tk_image)
        canvas.image = tk_image  # 이미지 참조 유지
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
# 창 크기 변경 시 리사이즈
def resize_image(event):
    load_scene(f"scene_{scene_num}.png")
# 다음 씬으로 넘어가는 함수 (scene_8에서 사용)
def next_scene_from_dream():
    global scene_num, entry_8
    text = entry_8.get("1.0", "end-1c").strip()

    if text:
        scene_num = 9
        load_scene(f"scene_{scene_num}.png")
        hide_all_inputs()  # 모든 입력 요소와 버튼 숨김
    else:
        print("꿈을 입력해주세요.")
# 장면 전환 함수
def next_scene(event=None):
    global scene_num
    if 0 <= scene_num < 8 or 9 <= scene_num < 17:
        scene_num += 1
        load_scene(f"scene_{scene_num}.png")

        if scene_num == 17:
            create_input_text_button()
        elif scene_num == 8:
            create_dream_input_text_button()
        elif scene_num == 9:
            hide_all_inputs()  # scene_9로 넘어갈 때 입력 박스와 버튼 숨김

        start_inactivity_timer()

# 첫 장면 로드
load_scene(scenes[0])

# 창 크기 변경 시 리사이즈
window.bind("<Configure>", resize_image)

# 클릭 시 다음 장면으로 이동
window.bind("<Button-1>", next_scene)

# 비활동 감지 이벤트 바인딩
window.bind("<Key>", lambda event: start_inactivity_timer())
window.bind("<Motion>", lambda event: start_inactivity_timer())

# 메인 루프 실행
window.mainloop()
