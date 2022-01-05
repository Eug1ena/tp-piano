import pygame.midi
import time
from pygame.locals import *
import pygame
import sys

# 事前にGaragebandを立ち上げておく

# Pygame.midiを初期化
pygame.midi.init()
player = pygame.midi.Output(1)
player.set_instrument(1)

pygame.init()   # Pygameを初期化
screen = pygame.display.set_mode((400, 330))    # 画面を作成
pygame.display.set_caption("keyboard event")    # タイトルを作成

keys = []
pitches = []

# キーと音階の組を登録する
def add_key(key, pitch):
    keys.append(key)
    pitches.append(pitch)

add_key(K_a, 60);
add_key(K_w, 61);
add_key(K_s, 62);
add_key(K_e, 63);
add_key(K_d, 64);
add_key(K_f, 65);
add_key(K_t, 66);
add_key(K_g, 67);
add_key(K_y, 68);
add_key(K_h, 69);
add_key(K_u, 70);
add_key(K_j, 71);
add_key(K_k, 72);
add_key(K_o, 73);
add_key(K_l, 74);
add_key(K_p, 75);
add_key(K_SEMICOLON, 76);
add_key(K_COLON, 77);

# オクターブとトランスポーズの変量を定義
octave = 0
transpose = 0

# 使用方法を出力
print("")
print("操作方法:")
print(" ZXキー オクターブずつ変える")
print(" ↑↓キー 半音ずつ変える")
print(" Escキー 退出")
print("")
print("ピアノ:")
print("   W E   T Y U   O P")
print("  A S D F G H J K L ; :")
print("")

# キーの入力を監視し続ける
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # ESCキーならスクリプトを終了
        if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # キーを押したら音が鳴る
        for i in range(0, len(keys)):
            if event.type == KEYDOWN and event.key == keys[i]:
                player.note_on(pitches[i] + octave * 12 + transpose, 127)
            if event.type == KEYUP and event.key == keys[i]:
                player.note_off(pitches[i] + octave * 12 + transpose, 127)

        # 上下左右キーでトランスポーズ
        if event.type == KEYDOWN and event.key == K_x:
            octave += 1
            print("オクターブ " + str(octave) + " / " + "トランスポーズ " + str(transpose))
        if event.type == KEYDOWN and event.key == K_z:
            octave -= 1
            print("オクターブ " + str(octave) + " / " + "トランスポーズ " + str(transpose))
        if event.type == KEYDOWN and event.key == K_UP:
            transpose += 1
            print("オクターブ " + str(octave) + " / " + "トランスポーズ " + str(transpose))
        if event.type == KEYDOWN and event.key == K_DOWN:
            transpose -= 1
            print("オクターブ " + str(octave) + " / " + "トランスポーズ " + str(transpose))

        pygame.display.update()
