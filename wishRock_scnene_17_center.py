import tkinter as tk
from tkinter import PhotoImage, Text, ttk
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
from PIL import Image, ImageTk  # Pillow 라이브러리 사용

entry_1 = None
generate_button = None

client = ElevenLabs(
    api_key="sk_c4e012b0f5bca4111c1ee2fb1db327a581e2a3475150f5ee",  # Defaults to ELEVEN_API_KEY
)

# 목소리 생성 함수
def generate_voice():
    text = entry_1.get("1.0", "end-1c")  # 입력된 텍스트 가져오기
    if text.strip():  # 공백이 아닌 경우에만 실행
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ",  # 원하는 목소리 ID 입력 (나 Jinie)
            model="eleven_multilingual_v2"
        )
        play(audio)  # 생성된 오디오 재생

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("WishRock")
window.geometry("1280x720")
window.minsize(640, 360)  # 최소 크기 설정
window.configure(bg="#FFFFFF")

# 전체화면 모드 활성화
window.attributes("-fullscreen", True)

# ESC 키로 전체화면 모드 해제
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

# 기본 변수들 설정
scene_num = 1
scenes = [f"scene_{i}.png" for i in range(1, 18)]  # 장면 파일 리스트

# 캔버스 설정
canvas = tk.Canvas(window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
canvas.pack(fill="both", expand=True)

# 경로 설정
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\yesju\OneDrive\바탕 화면\wishRock")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_input_text_button():
    global canvas, entry_1, generate_button

    # Text 위젯 생성 (입력 박스)
    entry_1 = Text(
        bd=0,
        bg="#E5D9CD",  # 텍스트 박스의 배경색
        fg="#000000",  # 텍스트 색
        highlightthickness=0,
        wrap='word',  # 단어 단위로 줄 바꿈
        font=("Arial", 14),  # 글꼴 설정
        relief="flat"  # 테두리 제거
    )
    entry_1.place(
        relx=0.5,  # X 중심 위치
        rely=0.4,  # Y 위치
        anchor='center',  # 중앙 기준
        width=875.0,
        height=84.0
    )

    # 그림자 효과 추가를 위한 프레임
    shadow_frame = tk.Frame(canvas, bg="#d9d9d9", bd=0)
    shadow_frame.place(relx=0.5, rely=0.4, anchor='center', width=885.0, height=94.0)

    # Button 스타일 설정
    style = ttk.Style()
    style.configure("TButton",
                    background="#FFCC00",  # 버튼 배경색
                    foreground="#FFFFFF",  # 버튼 글자색
                    borderwidth=0,
                    relief="flat")  # 평평한 스타일

    # Button 생성
    generate_button = ttk.Button(
        canvas,
        text="Generate Voice",  # 버튼 텍스트
        style="TButton",  # 버튼 스타일
        command=generate_voice  # 버튼 클릭 시 호출될 함수
    )
    generate_button.place(
        relx=0.5,  # X 중심 위치
        rely=0.55,  # Y 위치
        anchor='center',  # 중앙 기준
        width=875.0,
        height=84.0
    )

    # 버튼에 대한 hover 효과
    def on_enter(e):
        generate_button['background'] = '#FFC300'  # 마우스 오버 시 색상 변경

    def on_leave(e):
        generate_button['background'] = '#FFCC00'  # 마우스 아웃 시 원래 색상으로 돌아가기

    generate_button.bind("<Enter>", on_enter)
    generate_button.bind("<Leave>", on_leave)

# 이미지 로드 및 리사이즈 함수
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

# 장면 전환 함수
def next_scene(event=None):
    global scene_num
    if scene_num < 17:
        scene_num += 1
        load_scene(f"scene_{scene_num}.png")  # 다음 장면 로드
        # 씬 17에서 텍스트 입력 버튼 생성
        if scene_num == 17:
            create_input_text_button()

# 첫 장면 로드
load_scene(scenes[0])

# 창 크기 변경 시 리사이즈
window.bind("<Configure>", resize_image)

# 클릭 시 다음 장면으로 이동
window.bind("<Button-1>", next_scene)

# 메인 루프 실행
window.mainloop()
