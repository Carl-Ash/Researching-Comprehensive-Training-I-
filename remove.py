import json
import os
import random
import sys
from pathlib import Path


PLACEHOLDER = "<<$ target $>>"


def read_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_file_lines(filepath, lines):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def process_function_item(item):
    namespace = item["namespace"]
    relative_path = item["completion_path"]
    src_path = Path("Source_Code") / relative_path

    body_start, body_end = item["body_position"]  # assumed 1-based
    intra_class = item["dependency"]["intra_class"]
    intra_file = item["dependency"]["intra_file"]
    cross_file = item["dependency"]["cross_file"]

    start_idx = body_start - 1  # to 0-based
    end_idx = body_end

    if not src_path.exists():
        print(f"⚠️ 文件不存在，跳过: {src_path}")
        return

    lines = read_file_lines(src_path)
    indent = item.get("indent", 4)
    placeholder_line = f"{' ' * indent}{PLACEHOLDER}\n"

    no_deps = not (intra_class or intra_file or cross_file)

    if no_deps:
        total_lines = end_idx - start_idx
        if total_lines <= 1:
            # 整个 body 替换为占位符
            lines[start_idx:end_idx] = [placeholder_line]
        else:
            mid = start_idx + total_lines // 2
            if random.choice([True, False]):
                # 删除上半部 → 用占位符替代上半，保留下半
                lines[start_idx:mid] = [placeholder_line]
            else:
                # 删除下半部 → 用占位符替代下半，保留上半
                lines[mid:end_idx] = [placeholder_line]
    else:
        # 有依赖：整个 body 替换为占位符
        lines[start_idx:end_idx] = [placeholder_line]

    # 生成 _remove 文件
    new_path = src_path.parent / (src_path.stem + "_remove" + src_path.suffix)
    write_file_lines(new_path, lines)
    print(f"✅ 已生成: {new_path}")


def main(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data if isinstance(data, list) else [data]

    for item in items:
        try:
            process_function_item(item)
        except Exception as e:
            print(f"❌ 处理 {item.get('namespace', 'unknown')} 时出错: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python remove.py <input.json>")
        sys.exit(1)

    json_path = sys.argv[1]
    if not os.path.isfile(json_path):
        print(f"错误: 找不到 JSON 文件 {json_path}")
        sys.exit(1)

    main(json_path)
