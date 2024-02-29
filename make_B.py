from PIL import Image
import os
import pandas as pd

def convert_jpg_to_png(input_path, output_directory):
    # 画像の存在を確認
    if not os.path.exists(input_path):
        print(f"{input_path} は存在しません。")
        return
    
    # 出力ディレクトリが存在しなければ作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 指定したディレクトリ内の全ての.jpg画像を処理
    for filename in os.listdir(input_path):
        if filename.endswith(".jpg"):
            filepath = os.path.join(input_path, filename)
            
            # 画像の読み込み
            try:
                image = Image.open(filepath)
            except Exception as e:
                print(f"{filepath} の読み込み中にエラーが発生しました: {e}")
                continue
            
            # 画像のサイズを取得
            width, height = image.size
            
            # 出力パスを設定して画像を保存
            output_path = os.path.join(output_directory, f"{filename.split('.')[0]}.png")
            try:
                image.save(output_path)
                print(f"{output_path} に変換して保存しました。")
            except Exception as e:
                print(f"{output_path} の保存中にエラーが発生しました: {e}")
            
            

if __name__ == "__main__":
    input_directory = R"C:\Users\k3o2u\WorkSpace\ThemaB\GAN_TestData\GanShinke"
    output_directory = R"C:\Users\k3o2u\WorkSpace\ThemaB\image_converter\dataset\group_B"
    
    convert_jpg_to_png(input_directory, output_directory)
