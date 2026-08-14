import json
import os
from datetime import datetime

DATA_FILE = "prompts.json"


def load_prompts():
    # main.py 파일이 있는 절대 경로를 기준으로 prompts.json 위치 지정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "prompts.json")
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f" 파일 로드 중 오류 발생: {e}")
            return []
    else:
        print(" prompts.json 파일을 찾을 수 없습니다.")
        return []


def save_prompts(prompts):
    """프롬프트 데이터를 파일에 저장합니다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)


def clear_screen():
    """터미널 화면을 정리합니다."""
    os.system("cls" if os.name == "nt" else "clear")


def print_prompt_summary(prompt):
    """프롬프트 한 줄 요약 출력"""
    fav_status = "★" if prompt.get("is_favorite", False) else " "
    tags = ", ".join(prompt.get("tags", []))
    tag_str = f" [{tags}]" if tags else ""
    print(
        f"[{prompt['id']}] [{fav_status}] [{prompt['category']}] {prompt['title']}{tag_str}"
    )


def add_prompt(prompts):
    print("\n--- [새 프롬프트 추가] ---")
    print("💡 (이전으로 돌아가시려면 '0'을 입력하세요.)")
    
    title = input("\n제목: ").strip()
    
    # '0' 입력 시 메인 메뉴로 복귀
    if title == '0':
        print(" 새 프롬프트 추가를 취소하고 메인 메뉴로 돌아갑니다.")
        return

    category = input("카테고리 (예: 텍스트 생성, 이미지 생성, 페르소나 등): ").strip()
    content = input("프롬프트 내용: ").strip()
    tags_input = input("태그 (쉼표로 구분, 예: 파이썬,디버깅): ").strip()
    
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]

    # 새로운 ID 부여 (기존 ID의 최대값 + 1)
    new_id = max([p.get("id", 0) for p in prompts], default=0) + 1

    new_prompt = {
        "id": new_id,
        "title": title,
        "category": category if category else "미분류",
        "content": content,
        "tags": tags,
        "is_favorite": False
    }

    prompts.append(new_prompt)

    # prompts.json 파일에 자동 저장
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "prompts.json")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=2)
        print(f"\n '{title}' 프롬프트가 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"\n 저장 중 오류가 발생했습니다: {e}")


def list_prompts(prompts):
    """전체 프롬프트 목록을 조회합니다."""
    print("\n===  전체 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in prompts:
        print_prompt_summary(p)


def view_by_category(prompts):
    """카테고리별로 프롬프트를 조회합니다."""
    print("\n===  카테고리별 조회 ===")
    categories = sorted(list(set(p["category"] for p in prompts)))
    if not categories:
        print("등록된 카테고리가 없습니다.")
        return

    print("존재하는 카테고리:", ", ".join(categories))
    target_category = input("조회할 카테고리명 입력: ").strip()

    filtered = [p for p in prompts if p["category"] == target_category]
    if not filtered:
        print(f"'{target_category}' 카테고리에 해당하는 프롬프트가 없습니다.")
        return

    print(f"\n[{target_category}] 카테고리 목록:")
    for p in filtered:
        print_prompt_summary(p)


def search_prompts(prompts):
    """제목, 내용, 태그에서 키워드로 검색합니다."""
    print("\n===  키워드 검색 ===")
    keyword = input("검색어 입력: ").strip().lower()
    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []
    for p in prompts:
        in_title = keyword in p["title"].lower()
        in_content = keyword in p["content"].lower()
        in_tags = any(keyword in t.lower() for t in p.get("tags", []))
        if in_title or in_content or in_tags:
            results.append(p)

    if not results:
        print(f"'{keyword}' 검색 결과가 없습니다.")
        return

    print(f"\n검색 결과 ({len(results)}건):")
    for p in results:
        print_prompt_summary(p)


def list_favorites(prompts):
    """즐겨찾기된 프롬프트만 조회합니다."""
    print("\n=== ★ 즐겨찾기 목록 ===")
    favs = [p for p in prompts if p.get("is_favorite", False)]
    if not favs:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
        return

    for p in favs:
        print_prompt_summary(p)


def view_detail(prompts):
    """특정 프롬프트의 상세 내용을 조회하고 관리합니다."""
    print("\n===  프롬프트 상세 보기 ===")
    try:
        prompt_id = int(input("조회할 프롬프트 ID 입력: "))
    except ValueError:
        print(" 숫자로 된 ID를 입력해주세요.")
        return

    prompt = next((p for p in prompts if p["id"] == prompt_id), None)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    fav_str = "★ (즐겨찾기)" if prompt.get("is_favorite", False) else "☆ (일반)"
    print("\n" + "=" * 40)
    print(f"ID       : {prompt['id']}")
    print(f"제목     : {prompt['title']}")
    print(f"카테고리 : {prompt['category']}")
    print(f"태그     : {', '.join(prompt.get('tags', []))}")
    print(f"즐겨찾기 : {fav_str}")
    print(f"생성일시 : {prompt.get('created_at', '-')}")
    print("-" * 40)
    print("내용:")
    print(prompt["content"])
    print("=" * 40)

    print("\n[작업 선택] 1. 즐겨찾기 토글 | 2. 프롬프트 삭제 | 0. 이전으로")
    sub_choice = input("선택 > ").strip()

    if sub_choice == "1":
        prompt["is_favorite"] = not prompt.get("is_favorite", False)
        save_prompts(prompts)
        status = "등록" if prompt["is_favorite"] else "해제"
        print(f" 즐겨찾기가 {status}되었습니다.")
    elif sub_choice == "2":
        confirm = input("정말 삭제하시겠습니까? (y/N): ").strip().lower()
        if confirm == "y":
            prompts.remove(prompt)
            save_prompts(prompts)
            print(" 프롬프트가 삭제되었습니다.")


def main():
    prompts = load_prompts()

    while True:
        print("\n" + "=" * 35)
        print(" 🚀 프롬프트 관리자 (Prompt Manager)")
        print("=" * 35)
        print("1. 새 프롬프트 추가")
        print("2. 전체 프롬프트 목록 보기")
        print("3. 카테고리별 조회")
        print("4. 키워드 검색")
        print("5. 즐겨찾기 목록 보기")
        print("6. 프롬프트 상세 보기 / 관리")
        print("0. 프로그램 종료")
        print("=" * 35)

        choice = input("메뉴 번호 선택 > ").strip()

        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            list_prompts(prompts)
        elif choice == "3":
            view_by_category(prompts)
        elif choice == "4":
            search_prompts(prompts)
        elif choice == "5":
            list_favorites(prompts)
        elif choice == "6":
            view_detail(prompts)
        elif choice == "0":
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break
        else:
            print("\n 잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()

CATEGORY_MAP = {
    "1": "개발",
    "2": "디자인",
    "3": "기획"
}

def select_category(prompts):
    """카테고리 목록을 보여주고 선택한 카테고리의 프롬프트를 필터링하여 조회하는 함수"""
    # 등록된 모든 카테고리 중복 없이 추출
    categories = list(set(p.get("category", "미분류") for p in prompts if p.get("category")))
    
    if not categories:
        print("등록된 카테고리가 없습니다.")
        return

    print("\n--- [카테고리 목록] ---")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
        
    choice = input("\n조회할 카테고리 번호를 입력하세요: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_cat = categories[int(choice) - 1]
        print(f"\n [{selected_cat}] 카테고리 프롬프트 목록:")
        
        filtered_prompts = [p for p in prompts if p.get("category") == selected_cat]
        for p in filtered_prompts:
            print_prompt_summary(p)
    else:
        print("올바른 번호를 입력해 주세요.")
add_prompt()
print_prompt_summary()
list_prompts()
view_by_category()
search_prompts()
list_favorites()
view_detail()