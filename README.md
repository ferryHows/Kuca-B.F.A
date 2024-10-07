# Kuca-B.F.A
2024 Kuca B.F.A (Digital Semina2)
widow노트북으로 진행한 과정
## CD List
- GitHub: ferryHows@gmail.com로 로그인
- 2024 건국대학교 현대미술학과 졸업전시 디지털세미나2 (2학기 신개설 계정)
- **리포지토리 이름**: <Kuca-B.F.A> - 디지털세미나2 졸업전시 작업백업용

## ERROR List

- [ ] **tkDesigner 설치 시 Pillow error**

1. 가상 환경 설정: 가상 환경을 만들고 그 안에 필요한 패키지를 설치하면 충돌을 피할 수 있습니다.

'''bash
python -m venv myenv
myenv\Scripts\activate
pip install Pillow
'''


## Environment Setup Checklist

설치 목록 확인코드

'''bash
pip list
'''
- [ ] **Git 설치

- [ ] **Python 3.9 설치 확인**
  - [ ] Python 3.9 버전으로 설치해야 wheel for pillow 오류 나지 않음
  - [ ] 설치 과정에서 "Add Python to PATH" 옵션 체크
  - [ ] **"Install Now"** 버튼 클릭
  - [ ] Python 상위버전을 제거 후에 다시 재설치하는 경우, 시스템 환경변수 path에서 파이썬 경로가 39로 잘 저장되어있는지 확인하고, 상위버전의 경로가 남아있을 시 수정.

- [ ] **pip 설치**
  - [ ] get-pip.py 파일 다운로드
  - [ ] 관리자 권한으로 명령 프롬프트 열기
  - [ ] python get-pip.py 명령어 실행

- [ ] **elevenlabs 패키지 설치**
  - [ ] pip install elevenlabs 명령어 실행

- [ ] **tkDesigner , figma to tkDesigner 설치**
  - [ ] pillow 8.4.0 버전으로 설치
  - [ ] pip install tkdesigner 오류시 -> https://pypi.org/project/tkdesigner/1.0.7/ 직접설치하고, requirements.txt에서 pillow 8.4.0으로 수정하고 저장
  - [ ] gitClone 기능 이용해서 figma to tkd 다운로드 (https://github.com/ParthJadhav/Tkinter-Designer)
 
- [ ] **ffmpeg / ffplay / ffprob설치**
  - [ ] 실행시킬 프로젝트 파일이랑 같은 폴더에 있어야 함
  - [ ] 1. ffmpeg 공식 다운로드 홈페이지 : https://ffmpeg.org/download.html
  - [ ] 2. window builds용 빌드선택 -> 가장 최신&완전한 버전 다운로드

ffmpeg-master-latest-win64-gpl-shared.zip: 이 버전은 공유 라이브러리를 포함하고 있으며, 상대적으로 파일 크기가 작습니다. 이 버전은 기본적인 사용에는 충분하지만, 특정 기능이나 코덱 지원이 부족할 수 있습니다.

ffmpeg-master-latest-win64-gpl.zip: 이 버전은 더 많은 기능과 코드 지원을 포함하고 있으며, 파일 크기가 더 큽니다. 이 버전은 FFmpeg의 모든 기능을 사용할 수 있는 가장 완전한 버전입니다.
  
  - [ ] 3. 압축 파일 다운로드.

         제공되는 다운로드 링크 중 하나를 클릭하여 압축된 .zip 파일을 다운로드합니다. 파일 이름에는 ffmpeg-release-full.zip 같은 이름이 포함될 수 있습니다.
 
  - [ ] 4. 압축 해제

  - [ ] 5. 실행 파일 찾기

         압축을 푼 폴더 안에 bin 폴더가 있을 것입니다. 이 폴더 안에 ffmpeg.exe, ffplay.exe, ffprobe.exe 실행 파일이 들어 있습니다.
 
  - [ ] 6. 환경 변수 설정 (선택 사항)

        실행 파일을 명령 프롬프트에서 쉽게 접근할 수 있도록 하려면, bin 폴더의 경로를 시스템 환경 변수 PATH에 추가할 수 있습니다. 이렇게 하면 터미널에서 직접 ffmpeg, ffplay, ffprobe를 호출할 수 있습니다.

        - [ ] WINDOWS에서 환경 변수 추가 (선택 사항)

         - 제어판 -> '시스템' 또는 '시스템 및 보안' -> '고급 시스템 설정' -> '환경 변수' -> '시스템 변수' 목록에서 PATH 변수 선택 -> '편집' -> 새 항목으로 C:\ffmpeg\bin 추가 -> '적용'
           
## Helps

figma to tkdesigner

https://m.blog.naver.com/yug311861/222915865128

## Process Note

### 1. 새로운 리포지토리 생성
1. GitHub에서 리포지토리 생성
2. GitHub에 로그인한 후, 오른쪽 상단의 + 버튼을 클릭하고 New repository를 선택합니다.
3. 리포지토리 이름을 ferryhows로 설정합니다.
4. 선택적으로 설명을 추가하고, Initialize this repository with a README를 체크합니다.
5. Create repository 버튼을 클릭하여 리포지토리를 생성합니다.

### 2. VSCode에서 Git 설정

- **VSCode에서 프로젝트 폴더 열기**
  - VSCode를 열고, File > Open Folder...를 선택하여 작업할 프로젝트 폴더를 엽니다.

- **터미널에서 Git 초기화**
  - VSCode의 터미널을 열고 (단축키: Ctrl + ), 다음 명령어를 입력하여 로컬 Git 저장소를 초기화합니다:
  
    
bash
    git init


### 3. 파일 추가 및 커밋

- **파일 추가**
  - 프로젝트 폴더에 파일을 추가하거나 수정합니다.

- **변경 사항 확인**
  - VSCode의 Source Control 사이드바를 클릭하여 변경 사항을 확인합니다.
  
- **파일 스테이징 및 커밋**
  - 터미널에서 변경된 파일을 Git에 추가하고 커밋합니다:
  
    
bash
    git add .
    git commit -m "Initial commit"


### 4. 변경 사항 푸시

- **변경 사항 푸시**
  - 커밋한 변경 사항을 원격 저장소에 푸시합니다:
  
    
bash
    git push -u origin main


## 이후 작업

- **수정 사항 커밋 및 푸시**: 파일을 수정한 후에는 다시 git add ., git commit -m "message", git push 명령어를 사용하여 변경 사항을 관리합니다.
- **협업 및 코드 리뷰**: 다른 사람과 협업하거나 코드 리뷰가 필요할 경우, GitHub의 풀 리퀘스트 기능을 활용하세요.

# Instant Jinie Voice 

- **Setting**
  - 1. Python 패키지 설치 !반드시 Add Python to Path를 체크하고 설치!
   (1)Python 공식 웹사이트에서 최신 버전을 다운로드합니다.
   (2)설치 과정에서 "Add Python to PATH" 옵션을 반드시 체크합니다. pip명령어 사용을 위해
   (2-2) 설치옵션에 관하여
"Add Python to PATH" 옵션은 Python을 설치 후 명령 프롬프트에서 python 명령어를 인식하게 합니다.
"Use admin privileges" 옵션은 설치를 관리자 권한으로 실행할지 여부를 묻습니다. 시스템 폴더에 프로그램을 설치하거나, 다른 사용자에게 영향을 미치는 설정을 변경할 때 필요할 수 있습니다.
   (3)Install Now"**를 선택하고 설치가 완료될 때까지 기다립니다.

-**pip 설치확인**
관리자 권한으로 설치하려면, 다음 단계를 따르세요:

명령 프롬프트를 관리자 권한으로 실행:

시작 메뉴에서 "cmd"를 검색하세요.
검색 결과에서 "명령 프롬프트"를 오른쪽 클릭하고, "관리자 권한으로 실행"을 선택하세요.
get-pip.py 파일을 다시 실행:

관리자 권한으로 실행된 명령 프롬프트 창에서, 이전에 다운로드한 get-pip.py 파일을 실행하세요. 예를 들어:
'''bash
python get-pip.py
'''
이렇게 하면 pip가 제대로 설치될 가능성이 높습니다. 설치가 완료되면, pip 명령어를 사용하여 elevenlabs를 설치해 보세요:

'''bash
pip install elevenlabs
'''

##Figma to TkD

'''cmd
cd Tkinter-Designer
'''

'''cmd
cd gui
'''

'''cmd
python gui.py
'''

보통은 python3 gui.py로 열지만 오류가 있었으므로 특정 버전을 지정해서 오류를 피해가야하는게 아니라면 어지간하면 명령어는 중립적으로 작성.



