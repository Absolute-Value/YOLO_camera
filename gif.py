from PIL import Image
import os
import glob
import argparse

parser = argparse.ArgumentParser(description='gif')
parser.add_argument('--in_dir', type=str, default='outputs/2023-03-24', help='gifを作るフォルダ')
parser.add_argument('--in_file', type=str, default='*', help='見つけたいファイル名')
parser.add_argument('--out_file', type=str, default='2023-03-24_15.gif', help='出力ファイル名')
args = parser.parse_args()
 
# GIFアニメーションを作成
def create_gif(in_dir, in_filename, out_filename):
    path_list = sorted(glob.glob(os.path.join(*[in_dir, in_filename]))) # ファイルパスをソートしてリストする
    imgs = []                                                   # 画像をappendするための空配列を定義
 
    # ファイルのフルパスからファイル名と拡張子を抽出
    for i in range(len(path_list)):
        img = Image.open(path_list[i])                          # 画像ファイルを1つずつ開く
        imgs.append(img)                                        # 画像をappendで配列に格納していく
 
    # appendした画像配列をGIFにする。durationで持続時間、loopでループ数を指定可能。
    imgs[0].save(out_filename,
                 save_all=True, append_images=imgs[1:], optimize=False, duration=100, loop=0)
 
# GIFアニメーションを作成する関数を実行する
create_gif(in_dir=args.in_dir, in_filename=args.in_file, out_filename=args.out_file)