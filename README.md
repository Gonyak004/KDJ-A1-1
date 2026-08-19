# KDJ-A1-1

Python & git 기초

목차

[1. 프로그램 실행 및 설명](#1-프로그램-실행-및-설명)

[2. 실행 방법](#2-실행-방법)

[3. 기능 목록](#3-기능-목록)

[4. 프롬프트 카테고리](#4-프롬프트-카테고리)

[5. 커밋 및 브랜치 생성 및 병합 기록](#5-커밋-및-브랜치-생성-및-병합-기록)

##

### 1. 프로그램 실행 및 설명

프롬프트 관리자 (Prompt Manager)

>다양한 분야의 생성형 AI 프롬프트를 한곳에서 체계적으로 관리, 조회, 검색 및 즐겨찾기를 할 수 있는 파이썬 기반 CLI 프로그램입니다.

주요 기능

<img width="1096" height="255" alt="Image" src="https://github.com/user-attachments/assets/6c9a23dd-232d-4dd4-9c09-d9e27b5f37a8" />

1. 전체 프롬프트 목록 조회

   등록된 모든 프롬프트를 한눈에 확인
   즐겨찾기 여부(`★`/`☆`), ID, 제목, 카테고리 및 태그 정보 제공

3. 새 프롬프트 추가
    
    제목, 카테고리, 내용, 태그 입력 받아 `prompts.json`에 자동 저장
    작업 중 언제든지 `0` 입력 시 안전하게 이전 메인 메뉴로 복귀

4. 카테고리별/태그별 검색 및 필터링

    텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화 등 카테고리별 모아보기
    키워드 및 태그 기반 실시간 조회

5. 즐겨찾기 토글 및 모아보기

    자주 사용하는 핵심 프롬프트의 즐겨찾기(`is_favorite`) 상태 관리
    즐겨찾기 등록된 프롬프트만 필터링하여 확인

   ├── main.py           # 프로그램 메인 실행 및 제어 로직 (함수 모듈화)

   ├── prompts.json      # 프롬프트 데이터 저장용 JSON 파일

   └── README.md         # 프로젝트 안내 문서


기술 스택 및 요구 사항

Language: Python 3.10.7

Data Storage: JSON (prompts.json)

Environment: VS Code Terminal / Command Line Interface (CLI)

<img width="1047" height="15" alt="Image" src="https://github.com/user-attachments/assets/c46a076c-11ca-42d3-827b-68acc05ed5c4" />
<img width="1033" height="12" alt="Image" src="https://github.com/user-attachments/assets/2b343f80-3248-44f2-ab5b-b26d33eeff5a" />

## 프로그램 실행 방법

# 저장소 클론 #

    git clone [https://github.com/Gonyak004/KDJ-A1-1.git]

**Git clone 원격 저장소 터미널 실행 로그**

<img width="1086" height="130" alt="Image" src="https://github.com/user-attachments/assets/2bdb150f-3ced-4e61-8093-96c7e2486496" />

# 프로그램 실행 #

별도의 외부 라이브러리 설치 없이 파이썬 기본 환경에서 즉시 실행할 수 있습니다.

기본 등록 프롬프트 데이터 구성

<img width="1551" height="1044" alt="Image" src="https://github.com/user-attachments/assets/9549234f-0d4d-4c3e-a563-eb613bfda1b8" />

텍스트 생성: 블로그 포스팅용 원고 자동 작성 프롬프트

이미지 생성: 드랍 빈(Drop Bean) 커피 브랜드 광고 이미지 생성 프롬프트 (Midjourney)

영상 생성: 드랍 빈(Drop Bean) 커피 시네마틱 샷 비디오 생성 프롬프트 (Runway)

페르소나: 초보 심리 상담사를 위한 20년 경력의 AI 전문 심리 상담사

자동화: Make(Integromat)를 활용한 컴퓨터 견적 상담 워크플로우 (구글 폼 ➔ 구글 시트 ➔ 지메일)

##

### 2. 실행 방법

파이썬 프롬프트 관리자(main.py) 터미널 실행 방법입니다

1.VS Code 터미널 열기:단축키 사용.VS Code 상단 메뉴의 **[터미널] ➔ [새 터미널]**을 클릭하거나, 단축키 Ctrl + ~ (Mac: Cmd + ~)를 눌러 터미널 창을 엽니다.

2.현재 위치 파일 확인:선택 사항.터미널에 아래 명령어를 입력하여 현재 폴더에 main.py와 prompts.json 파일이 있는지 확인합니다.

    # Windows Command Prompt / PowerShell
    dir

    Mac / Linux / Git Bash
    ls

3.파이썬 프로그램 실행:핵심 명령어.터미널에 다음 명령어를 입력하고 **Enter**를 누르면 프로그램이 실행됩니다.Bashpython main.py

참고: Mac 또는 일부 환경에서는 python3 main.py로 입력해야 할 수 있습니다.

**실행 시 발생할 수 있는 오류 해결**

>python: command not found 에러 발생 시 컴퓨터에 파이썬이 설치되어 있지 않거나 환경 변수(PATH) 설정이 안 된 경우입니다. python3 main.py를 시도해 보거나 파이썬 재설치가 필요합니다.

>can't open file 'main.py' 에러 발생 시: 현재 터미널 위치가 프로젝트 폴더가 아닙니다. cd 폴더명 명령어로 main.py가 있는 폴더로 이동한 후 다시 실행하세요.

##

### 3. 기능 목록

1. 프롬프트 데이터 관리

      새 프롬프트 추가: 제목, 카테고리, 프롬프트 내용, 태그(쉼표 구분)를 받아 신규 ID를 자동 부여하여 저장

      JSON 파일 연동 (데이터 영속성): 모든 데이터는 prompts.json 파일에 자동 로드 및 저장되어 프로그램 재실행 후에도 보존

      이전 메뉴 복귀 (입력 취소): 추가 작업 중 0을 입력하면 데이터 저장 없이 안전하게 메인 메뉴로 복귀

<img width="512" height="456" alt="Image" src="https://github.com/user-attachments/assets/f88deb8f-5a79-47e4-a2ec-097e4d5ae03a" />

2. 조회 및 검색 기능 (Read & Search)

      전체 프롬프트 목록 조회: 등록된 모든 프롬프트를 한눈에 요약 출력 (즐겨찾기 상태 ★/☆, ID, 제목, 카테고리, 태그)

      카테고리별 필터링 조회: 등록된 카테고리(텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화 등)를 자동 추출하여 선택한 카테고리 항목만 모아보기

<img width="1040" height="373" alt="Image" src="https://github.com/user-attachments/assets/2e3d1cd1-5cba-4774-abc9-d0600fcb77c4" />

      태그 및 키워드 검색: 특정 키워드나 태그를 포함하는 프롬프트를 빠르게 탐색

3. 즐겨찾기(Favorite) 기능

      즐겨찾기 지정 및 해제 (토글): 자주 사용하는 핵심 프롬프트의 즐겨찾기 상태(is_favorite) 변경

      즐겨찾기 전용 목록 보기: ★ 표시된 프롬프트만 따로 필터링하여 조회

<img width="1036" height="341" alt="Image" src="https://github.com/user-attachments/assets/9ff560ee-fa3f-4587-9c2e-79634a68168d" />

4. 사용자 경험 및 시스템 안정성 (UX & Error Handling)

      직관적인 CLI 인터페이스: 대화형 번호 선택 메뉴 기반으로 손쉬운 조작

      예외 처리 및 튕김 방지
      잘못된 메뉴 번호/입력값 입력 시 안내 메시지 출력 후 재입력 유도

      데이터 누락 시 .get() 방식 활용 및 파일 로드 에러 방지

   <img width="1102" height="562" alt="Image" src="https://github.com/user-attachments/assets/2aafa6d7-4c40-4d92-bda5-e1b3bbb2f3f4" />

##

### 4. 프롬프트 카테고리

>이전 AI 도구 과제에 쓰인 프롬프트로 구성하였습니다.

1. 텍스트 생성 (Text Generation)

   개요: 블로그 원고, 마케팅 카피라이팅, 문서 요약, 이메일 교정, 정보 정리 등 문장 기반 콘텐츠를 생성하는 프롬프트

   주요 용도: ChatGPT, Claude, Gemini 등 LLM 활용 콘텐츠 작성

   프로젝트 내 예시: 블로그 포스팅용 1500자 원고 자동 작성 프롬프트

2. 이미지 생성 (Image Generation)

   개요: 화풍, 구도, 조명, 화질, 피사체 등을 시각적으로 구체화하여 이미지를 생성하는 프롬프트

   주요 용도: Midjourney, DALL-E 3, Stable Diffusion 등

   프로젝트 내 예시: 드랍 빈(Drop Bean) 커피 브랜드 광고 이미지 생성 영문 프롬프트

3. 영상 생성 (Video Generation)

   개요: 카메라 워킹(슬로모션, 줌), 프레임레이트, 연출 스타일에 맞춘 비디오 샷 생성 프롬프트

   주요 용도: Runway (Gen-2/Gen-3), Sora, Pika Labs 등

   프로젝트 내 예시: 드랍 빈(Drop Bean) 에스프레소 추출 4K 시네마틱 샷 비디오 프롬프트

4. 페르소나 (Persona)

   개요: AI에게 특정 직업, 경력, 성격, 행동 규칙을 지정하여 전문가 수준의 맞춤형 답변을 받도록 유도하는 프롬프트

   주요 용도: 1:1 맞춤 상담, 역할극(Role-play), 멘토링, 교육용 튜터

   프로젝트 내 예시: 초보 심리 상담사를 위한 20년 경력의 전문 수퍼바이저 AI 심리 상담사

5. 자동화 (Automation)

   개요: 노코드/저코드 툴(Make, Zapier, n8n) 및 API 연동 시 데이터를 처리하고 메일을 자동 발송하는 워크플로우 제어 프롬프트

   주요 용도: 업무 자동화, 데이터 수집 및 자동 파이프라인 구축

   프로젝트 내 예시: Make 활용 컴퓨터 견적 상담 워크플로우 (구글 폼 ➔ 구글 시트 ➔ 지메일 발송)

##

### 5. 커밋 및 브랜치 생성 및 병합 기록

1. 브랜치 및 병합 전략

      1. 작업 공간 분리 (Branch)
원본 코드가 망가지지 않도록, 용도에 따라 작업 공간을 나누어 개발했습니다.

**`main` 브랜치 (원본)**: 언제든지 에러 없이 실행되어야 하는 완성본 공간입니다.

**`feature/...` 브랜치 (작업실)**: '즐겨찾기'나 '뒤로 가기' 같은 새로운 기능을 만들 때, 원본에 영향을 주지 않기 위해 잠시 따로 만들어둔 '개인 작업실'입니다. 기능이 완벽해지면 그때 원본으로 합칩니다.

2. 안전하게 합치고 기록 남기기 (Merge)

      개인 작업실에서 만든 기능을 메인 원본으로 합칠 때, 단순히 덮어쓰지 않고 **"이 시점에 새로운 기능이 원본에 추가되었다"**는 발자국(Merge Commit)을 명확히 남겼습니다.

      추후 문제가 생겨도 언제, 어떤 기능이 추가되면서 합쳐졌는지 쉽게 추적할 수 있습니다. (`--no-ff` 병합 방식 사용)
      

**주요 커밋 내역 (Commit History)**

| 분류 | 커밋 메시지 (Commit Message) | 주요 작업 내용 |
| :--- | :--- | :--- |
| **Chore** | `최초 커밋: main.py 및 prompts.json 기본 틀 작성` | 프로젝트 실행 구조 및 기본 모듈 구성 |
| **Fix** | `수정: 메뉴 선택 및 입력값 예외 처리 로직 강화` | 입력값 오타 및 JSON 파일 로드 에러 방지 |
| **Data** | `데이터: 5가지 주제별(텍스트, 이미지, 영상, 페르소나, 자동화) 프롬프트 데이터 구성` | `prompts.json` 파일에 5종 핵심 데이터 구축 |
| **Feature** | `기능: 새 프롬프트 추가 시 0 입력으로 이전 메뉴 복귀 기능 구현` | 사용자 입력 취소 및 메인 메뉴 복귀 UX 개선 |
| **Feature** | `기능: 즐겨찾기 토글 및 상세 보기 기능 추가` | `feature/favorites-detail` 브랜치 내 기능 구현 |
| **Merge** | `Merge branch 'feature/favorites-detail'` | `--no-ff` 옵션을 활용한 메인 브랜치 병합 |
| **Docs** | `문서: README.md 작성 및 Git 관리 이력 정리` | 프로젝트 종합 안내 문서 작성 |

3. 시각화된 작업 흐름도 (Git Graph)

>중간에 가지가 옆으로 빠져나와(새 기능 개발) 작업을 마친 뒤 다시 큰 줄기(main)로 합쳐진 것을 한눈에 볼 수 있습니다.

<img width="1018" height="394" alt="Image" src="https://github.com/user-attachments/assets/cb15b7c3-85c2-47dc-98a3-4895e331f5b4" />
