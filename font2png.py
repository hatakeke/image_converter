from PIL import Image, ImageDraw, ImageFont

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
    text_width, text_height = draw.textsize(kanji, font)
    print(f"幅×高さ＝{text_width}×{text_height}")
    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(text_position, kanji, font=font, fill="black")

    # 画像の保存
    image.save(output_path, "PNG")

    # 生成した画像を表示（確認用）
    image.show()

if __name__ == "__main__":
    # ユーザーに漢字を入力してもらう
    kanji = input("生成したい漢字を1文字入力してください: ")

    # フォントのパスを指定
    font_path = R"C:\Windows\Fonts/SIMSUN.TTC"  # フォントファイルのパスに変更してください

    # 画像の保存先パスを指定
    output_path = fR"C:\Users\k3o2u\WorkSpace\ThemaB\image_converter\conversion\target/{kanji}_font.png"

    # 画像の生成と保存
    generate_kanji_image(kanji, font_path, output_path)
