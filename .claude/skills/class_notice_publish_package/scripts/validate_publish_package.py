import json
import sys
from pathlib import Path


REQUIRED_FILES = [
    "主图.png",
    "副图1.png",
    "副图2.png",
    "副图3.png",
    "副图4.png",
    "副图5.png",
    "发布文案.md",
    "info.json",
]


def status(ok: bool) -> str:
    return "通过" if ok else "失败"


def exists_status(ok: bool) -> str:
    return "存在" if ok else "缺失"


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：python validate_publish_package.py <发布包目录>")
        return 2

    target = Path(sys.argv[1])
    missing = []

    print("【发布包校验】")
    print(f"目标目录：{target}")

    for name in REQUIRED_FILES:
        ok = (target / name).exists()
        if not ok:
            missing.append(name)
        print(f"{name}：{exists_status(ok)}")

    info_path = target / "info.json"
    title_ok = False
    content_ok = False
    break_ok = False
    tags_ok = False
    comment_ok = False

    if info_path.exists():
        try:
            info = json.loads(info_path.read_text(encoding="utf-8"))
            title = info.get("title")
            content = info.get("content")
            tags = info.get("tags")
            comment = info.get("comment")
            title_ok = isinstance(title, str) and bool(title.strip())
            content_ok = isinstance(content, str) and bool(content.strip())
            break_ok = isinstance(content, str) and "\n\n" in content
            tags_ok = isinstance(tags, list)
            comment_ok = isinstance(comment, str) and bool(comment.strip())
        except Exception as exc:
            print(f"info.json 解析失败：{exc}")

    print()
    print("【info.json 校验】")
    print(f"title：{status(title_ok)}")
    print(f"content：{status(content_ok)}")
    print(f"content 是否包含真实段落换行 \\n\\n：{status(break_ok)}")
    print(f"tags 是否为数组：{status(tags_ok)}")
    print(f"comment 是否存在：{status(comment_ok)}")

    print()
    print("【最终结论】")
    if not missing and title_ok and content_ok and break_ok and tags_ok and comment_ok:
        print("发布包可交给小红书发布插件读取。")
        return 0

    problems = []
    if missing:
        problems.append("缺失文件：" + "、".join(missing))
    if not title_ok:
        problems.append("title 为空或缺失")
    if not content_ok:
        problems.append("content 为空或缺失")
    if not break_ok:
        problems.append("content 不包含真实段落换行 \\n\\n")
    if not tags_ok:
        problems.append("tags 不是数组")
    if not comment_ok:
        problems.append("comment 为空或缺失")

    print("发布包未通过校验：" + "；".join(problems))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
