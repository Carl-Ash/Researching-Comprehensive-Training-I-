import sys
import subprocess
from pathlib import Path


OBF_SCRIPT = "C:\\Users\\16646\\Desktop\\research\\experiment\\base\\baseline.py"
SEARCH_ROOT = "Source_Code"


def main():
    obf_path = Path(OBF_SCRIPT)
    if not obf_path.exists():
        print(f"❌ 找不到 obf.py: {obf_path.resolve()}")
        sys.exit(1)

    root = Path(SEARCH_ROOT)
    if not root.exists():
        print(f"❌ 搜索目录不存在: {root.resolve()}")
        sys.exit(1)

    remove_files = list(root.rglob("*_remove.py"))
    if not remove_files:
        print("⚠️ 没有找到任何 *_remove.py 文件")
        return

    print(f"🔍 找到 {len(remove_files)} 个 _remove.py 文件，开始混淆...\n")

    for i, src in enumerate(remove_files, 1):
        print(f"[{i}/{len(remove_files)}] 处理: {src}")

        # 输出目录 = 文件所在目录
        output_dir = str(src.parent)

        # 自动输入：文件路径 + 输出目录
        input_text = f"{src}\n{output_dir}\n"

        try:
            result = subprocess.run(
                [sys.executable, str(obf_path)],
                input=input_text,
                text=True,
                capture_output=True,
                timeout=60
            )
            if result.returncode == 0:
                print(f"  ✅ 混淆完成（输出在 {output_dir}）")
            else:
                print(f"  ⚠️ obf.py 返回非零状态（可能有语法错误）")
                # 可选：打印错误
                # print("STDERR:", result.stderr)
        except Exception as e:
            print(f"  ❌ 调用失败: {e}")

    print("\n🎉 批量混淆完成！")


if __name__ == "__main__":
    main()
