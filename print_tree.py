import os

def print_tree(root, prefix="", exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = set()
    try:
        entries = sorted(os.listdir(root))
    except PermissionError:
        # 読み取り権限がない場合はスキップ
        return
    # 除外するディレクトリをフィルタリング
    entries = [entry for entry in entries if entry not in exclude_dirs]
    last_index = len(entries) - 1
    for i, entry in enumerate(entries):
        path = os.path.join(root, entry)
        connector = "└─" if i == last_index else "├─"
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "   " if i == last_index else "│  "
            print_tree(path, prefix + extension, exclude_dirs)

if __name__ == "__main__":
    # 出力したいルートディレクトリ
    root_dir = r"C:\project\project"
    # 除外したいフォルダ（必要に応じて）
    exclude = {"migrations", "__pycache__", "venv","staticfiles",".git","django-summernote","static","media","logs","summernote","objects","wheelhouse","node_modules","assets","android"}  
    print_tree(root_dir, "", exclude)
