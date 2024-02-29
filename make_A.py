import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import random
import os

def generate_kanji_image(kanji, font_path, output_path):
    # 画像のサイズと背景色の設定
    image_size = (64, 64)
    background_color = "white"

    # フォントの読み込み
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    # 画像の生成
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)

    # テキストを描画
    text_position = (12, 12)
    draw.text(text_position, kanji, font=font, fill="black")

    # 画像の保存
    image.save(output_path, "PNG")

def main():
    # フォントのパスを指定
    font_path = R"C:\Windows\Fonts/SIMSUN.TTC"

    # 画像の保存先のディレクトリ
    save_directory = R"C:\Users\k3o2u\WorkSpace\ThemaB\image_converter\dataset\group_A"

    processed_files = set()  # 既に処理したファイルのセット

    while True:

        file_count = len([f for f in os.listdir(save_directory) if os.path.isfile(os.path.join(save_directory, f))])
        print(f"ファイルの数は {file_count} です。")

        if file_count >= 6763:
            print("目標のファイル数に達しました。プログラムを終了します。")
            break

        code_point = random.randint(0x4E00, 0x9FFF)
        char = chr(code_point)
        output_path = os.path.join(save_directory, f"{char}.png")

        # 既に同じ文字の画像が存在する場合や、同じ画像を再度保存する場合はスキップ
        if char in processed_files or os.path.exists(output_path):
            continue

        generate_kanji_image(char, font_path, output_path)
        processed_files.add(char)  # 処理したファイルをセットに追加

    # 生成した文字をCSVファイルに保存
    char_list = list(processed_files)  # 処理したファイルのセットをリストに変換
    df = pd.DataFrame({'character': char_list})
    df.to_csv('random_characters.csv', encoding='utf-8-sig', index=False)
    

if __name__ == "__main__":
    main()
