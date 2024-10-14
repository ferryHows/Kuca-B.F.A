#wishRock_getDream.py의 오류를 수정하기 위해 만들었으나 수정되지 않아서
#사실상 wishRock_getDream.py과 똑같은 파일. 코드는 다르나 작동 상으로 다른 점이 없음

# scene_8에서 scene_9으로 넘어갈 때 next_button이 사라지지않는 오류를 해결했으나, 
# next_button을 사라지게 하기 위해 작성한 코드 중에서
# 실제로 작동되는 코드와 불필요해서 삭제 가능한 코드를 구분 못 하겠음.
# 교수님 도움 필요.
# if next_button()
#    next_button.place_forget()으로 사라지게 했으나 이 코드를 여기저기 남발해둔 상태.

#wishRock_10.py

import tkinter as tk
from tkinter import PhotoImage, Text, ttk
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
from PIL import Image, ImageTk  # Pillow 라이브러리 사용

entry_1 = None
entry_8 = None
generate_button = None
voice_generated = False  # 목소리 생성 여부를 나타내는 변수
inactivity_timer = None  # 비활동 타이머
next_button = None

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
    if inactivity_timer is not None:  # 기존 타이머가 있을 경우 취소
        window.after_cancel(inactivity_timer)
    inactivity_timer = window.after(30000, reset_to_scene_1)  # 30초 후 scene_1로 리셋

# 비활동 상태를 감지하고 타이머 리셋
def reset_to_scene_1():
    global scene_num, voice_generated, entry_1, generate_button, entry_8, next_button
    if voice_generated:  # 목소리가 생성된 경우에만 리셋
        scene_num = 1  # scene_1으로 돌아감
        load_scene(f"scene_{scene_num}.png")  # 첫 장면 로드
        voice_generated = False  # 목소리 생성 상태 초기화
        
        # scene_1로 돌아가기 전에 입력 박스와 버튼 숨기기
        if entry_1:
            entry_1.place_forget()
        if generate_button:
            generate_button.place_forget()
        if entry_8:
            entry_8.place_forget()
        if next_button:
            next_button.place_forget()

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

#씬 17 기능
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
#씬 8 기능
def create_dream_input_text_button():
    global canvas, entry_8, scene_num, next_button
    if scene_num ==8:
    # Text 위젯 생성 (관객의 꿈 입력 박스)
        entry_8 = Text(
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
        entry_8.place(
            relx=0.5,  # X 중심 위치
            rely=0.4,  # Y 위치
            anchor='center',  # 중앙 기준
            width=875.0,
            height=124.0
        )
            # 중앙 정렬을 위한 태그 설정
        entry_8.tag_configure("center", justify='center')

    # 사용자가 입력할 때마다 중앙 정렬을 적용하는 함수
    def center_text(event):
        entry_8.tag_add("center", "1.0", "end")

    # Text 위젯에 입력 이벤트 바인딩
    entry_8.bind("<KeyRelease>", center_text)

    # Button 스타일 설정
    style = ttk.Style()
    style.configure("TButton",
                    background="#C2A6A8",  # 버튼 배경색
                    foreground="#3D2A2D",  # 버튼 글자색
                    borderwidth=3,
                    relief="ridge")  # 스타일

    # Button 생성 (꿈 입력 후 다음 씬으로 넘어가기)
    next_button = ttk.Button(
        canvas,
        text="꿈을 들려주세요.",  # 버튼 텍스트
        style="TButton",  # 버튼 스타일
        command=next_scene_from_dream  # 버튼 클릭 시 호출될 함수
    )
    next_button.place(
        relx=0.5,  # X 중심 위치
        rely=0.55,  # Y 위치
        anchor='center',  # 중앙 기준
        width=875.0,
        height=44.0
    )

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

# 다음 씬으로 넘어가는 함수 (scene_8에서 사용)
def next_scene_from_dream():
    global scene_num, entry_8, next_button
    text = entry_8.get("1.0", "end-1c").strip()  # 입력된 텍스트 가져오기

    if text:  # 텍스트가 비어있지 않은 경우에만 씬 전환
        scene_num = 9  # scene_9로 변경
        load_scene(f"scene_{scene_num}.png")  # 다음 장면 로드

        # 입력 박스와 버튼 숨기기
        entry_8.place_forget()
        next_button.place_forget() # next_button을 숨김
    else:
        # 텍스트 박스가 비어있을 경우 경고 메시지 표시
        print("꿈을 입력해주세요.")  # 콘솔에 경고 메시지 출력
        # 필요에 따라 메시지를 GUI로 표시하는 방법을 추가할 수 있습니다.

# 장면 전환 함수
def next_scene(event=None):
    global scene_num, entry_1, entry_8, generate_button, next_button

    if 0 <= scene_num < 8 or 9 <= scene_num < 17:
        scene_num += 1
        load_scene(f"scene_{scene_num}.png")  # 다음 장면 로드
        
        # scene_17에서만 텍스트 입력 버튼 생성
        if scene_num == 17:
            create_input_text_button()

        elif scene_num == 8:
            create_dream_input_text_button() # 꿈 입력 박스 생성
            next_button.place(relx=0.5, rely=0.8, anchor='center')  # scene_8에서 버튼 보이기
      
        else:
            # scene_9에 도달했을 때 다음 버튼 숨기기
            if scene_num == 9:
                entry_8.place_forget()
                next_button.place_forget()  # next_button을 숨김            
            # scene_17에서 1로 돌아갈 때, scene_8에서 9로 넘어갈 때 입력 박스와 버튼 숨기기
            if entry_1:
                entry_1.place_forget()
            if generate_button:
                generate_button.place_forget()
            if entry_8:
                entry_8.place_forget()
            if next_button:
                next_button.place_forget()

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
