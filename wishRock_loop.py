import tkinter as tk
from tkinter import PhotoImage, Text, ttk
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
from PIL import Image, ImageTk  # Pillow 라이브러리 사용

entry_1 = None
generate_button = None
voice_generated = False  # 목소리 생성 여부를 나타내는 변수
inactivity_timer = None  # 비활동 타이머

client = ElevenLabs(
    api_key="sk_c4e012b0f5bca4111c1ee2fb1db327a581e2a3475150f5ee",  # Defaults to ELEVEN_API_KEY
)

# 목소리 생성 함수
def generate_voice():
    global voice_generated
    text = entry_1.get("1.0", "end-1c")  # 입력된 텍스트 가져오기
    if text.strip():  # 공백이 아닌 경우에만 실행
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ",  # 원하는 목소리 ID 입력 (나 Jinie)
            model="eleven_multilingual_v2"
        )
        play(audio)  # 생성된 오디오 재생
        voice_generated = True  # 목소리가 생성되었음을 표시

# 비활동 타이머 함수
def start_inactivity_timer():
    global inactivity_timer
    inactivity_timer = window.after(30000, reset_to_scene_1)  # 30초 후 scene_1로 리셋

# 비활동 상태를 감지하고 타이머 리셋
def reset_to_scene_1():
    global scene_num, voice_generated, entry_1, generate_button
    if voice_generated:  # 목소리가 생성된 경우에만 리셋
        scene_num = 1  # scene_1으로 돌아감
        load_scene(f"scene_{scene_num}.png")  # 첫 장면 로드
        voice_generated = False  # 목소리 생성 상태 초기화
        
        # scene_1로 돌아가기 전에 입력 박스와 버튼 숨기기
        if entry_1:
            entry_1.place_forget()
        if generate_button:
            generate_button.place_forget()

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
        bd=2,
        bg="#D0A6A7",  # 텍스트 박스의 배경색
        fg="#3D2A2D",  # 텍스트 색
        highlightthickness=0,
        wrap='word',  # 단어 단위로 줄 바꿈
        font=("Arial Rounded MT Bold", 14),  # 다른 폰트 및 볼드체 설정
        relief="ridge",  # 테두리 스타일
        padx=10,  # 좌우 내부 여백
        pady=50   # 위아래 내부 여백 (중앙을 맞추기 위해 추가)
    )
    entry_1.place(
        relx=0.5,  # X 중심 위치
        rely=0.4,  # Y 위치
        anchor='center',  # 중앙 기준
        width=875.0,
        height=124.0
    )

    # 중앙 정렬을 위한 태그 설정
    entry_1.tag_configure("center", justify='center')

    # 사용자가 입력할 때마다 중앙 정렬을 적용하는 함수
    def center_text(event):
        entry_1.tag_add("center", "1.0", "end")

    # Text 위젯에 입력 이벤트 바인딩
    entry_1.bind("<KeyRelease>", center_text)

    # Button 스타일 설정
    style = ttk.Style()
    style.configure("TButton",
                    background="#C2A6A8",  # 버튼 배경색
                    foreground="#3D2A2D",  # 버튼 글자색
                    borderwidth=3,
                    relief="ridge")  # 스타일

    # Button 생성
    generate_button = ttk.Button(
        canvas,
        text="다 적은 후, 저를 눌러 들어보세요.",  # 버튼 텍스트
        style="TButton",  # 버튼 스타일
        command=generate_voice  # 버튼 클릭 시 호출될 함수
    )
    generate_button.place(
        relx=0.5,  # X 중심 위치
        rely=0.55,  # Y 위치
        anchor='center',  # 중앙 기준
        width=875.0,
        height=44.0
    )

    # 버튼에 대한 hover 효과
    def on_enter(e):
        generate_button['background'] = '#FFC300'  # 마우스 오버 시 색상 변경

    def on_leave(e):
        generate_button['background'] = '#E7BCBF'  # 마우스 아웃 시 원래 색상으로 돌아가기

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
    global scene_num, entry_1, generate_button
    if scene_num < 17:
        scene_num += 1
        load_scene(f"scene_{scene_num}.png")  # 다음 장면 로드
        
        # scene_17에서만 텍스트 입력 버튼 생성
        if scene_num == 17:
            create_input_text_button()
        else:
            # scene_1로 돌아갈 때 입력 박스와 버튼 숨기기
            if entry_1:
                entry_1.place_forget()
            if generate_button:
                generate_button.place_forget()
        
        start_inactivity_timer()  # 비활동 타이머 시작

# 첫 장면 로드
load_scene(scenes[0])

# 창 크기 변경 시 리사이즈
window.bind("<Configure>", resize_image)

# 클릭 시 다음 장면으로 이동
window.bind("<Button-1>", next_scene)

# 비활동 감지 이벤트 바인딩
window.bind("<Key>", lambda event: start_inactivity_timer())  # 키 입력 시 타이머 재시작
window.bind("<Motion>", lambda event: start_inactivity_timer())  # 마우스 움직임 시 타이머 재시작

# 메인 루프 실행
window.mainloop()
