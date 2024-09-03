# Kuca-B.F.A
2024 Kuca B.F.A (Digital Semina2)

## CD List
- GitHub: `ferryHows@gmail.com`로 로그인
- 2024 건국대학교 현대미술학과 졸업전시 디지털세미나2 (2학기 신개설 계정)
- **리포지토리 이름**: `<Kuca-B.F.A>` - 디지털세미나2 졸업전시 작업백업용

## Process Note

### 1. 새로운 리포지토리 생성
1. GitHub에서 리포지토리 생성
2. GitHub에 로그인한 후, 오른쪽 상단의 `+` 버튼을 클릭하고 `New repository`를 선택합니다.
3. 리포지토리 이름을 `ferryhows`로 설정합니다.
4. 선택적으로 설명을 추가하고, `Initialize this repository with a README`를 체크합니다.
5. `Create repository` 버튼을 클릭하여 리포지토리를 생성합니다.

### 2. VSCode에서 Git 설정

- **VSCode에서 프로젝트 폴더 열기**
  - VSCode를 열고, `File > Open Folder...`를 선택하여 작업할 프로젝트 폴더를 엽니다.

- **터미널에서 Git 초기화**
  - VSCode의 터미널을 열고 (단축키: `Ctrl + `), 다음 명령어를 입력하여 로컬 Git 저장소를 초기화합니다:
  
    ```bash
    git init
    ```

### 3. 파일 추가 및 커밋

- **파일 추가**
  - 프로젝트 폴더에 파일을 추가하거나 수정합니다.

- **변경 사항 확인**
  - VSCode의 Source Control 사이드바를 클릭하여 변경 사항을 확인합니다.
  
- **파일 스테이징 및 커밋**
  - 터미널에서 변경된 파일을 Git에 추가하고 커밋합니다:
  
    ```bash
    git add .
    git commit -m "Initial commit"
    ```

### 4. 변경 사항 푸시

- **변경 사항 푸시**
  - 커밋한 변경 사항을 원격 저장소에 푸시합니다:
  
    ```bash
    git push -u origin main
    ```

## 이후 작업

- **수정 사항 커밋 및 푸시**: 파일을 수정한 후에는 다시 `git add .`, `git commit -m "message"`, `git push` 명령어를 사용하여 변경 사항을 관리합니다.
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









