import os
import random

def count_files(directory_path):
    # 指定されたディレクトリ内のすべてのファイルとサブディレクトリを取得
    all_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    return len(all_files)

def remove_random_files(directory_path, target_count):
    # ディレクトリ内のすべてのファイルを取得
    all_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # PNG画像のみをフィルタリング
    png_files = [f for f in all_files if f.lower().endswith('.png')]

    # 現在のファイル数が目標数未満の場合は何もしない
    current_count = len(png_files)
    if current_count <= target_count:
        print(f"現在のファイル数 ({current_count}) が目標数 ({target_count}) 以下です。")
        return

    # ランダムにファイルを削除
    files_to_remove = random.sample(png_files, current_count - target_count)
    for file_name in files_to_remove:
        file_path = os.path.join(directory_path, file_name)
        os.remove(file_path)
        print(f"{file_name} を削除しました。")

if __name__ == "__main__":
    directory_path = R"C:\Users\k3o2u\WorkSpace\ThemaB\image_converter\dataset\group_B"

    # 指定した数までファイル数を減らす
    target_count = 3
    remove_random_files(directory_path, target_count)

    file_count = count_files(directory_path)
    print(f"{directory_path} 内のファイルの数は {file_count} です。")