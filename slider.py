import matplotlib.pyplot as plt
import matplotlib.widgets as wg
import numpy as np

plt.figure(figsize=(6, 8))

plt.subplots_adjust(left=0.1, bottom=0.25)
plt.axis([-10, 10, -6, 16])
plt.xticks(range(-10, 11))
plt.yticks(range(-6, 17))
plt.grid()
plt.axhline(0, linewidth=1.5, color='black')
plt.axvline(0, linewidth=1.5, color='black')

# xを-10から+10まで、100ステップでつくる
x = np.linspace(-10, 10, 100)

# yはxの2次関数
a, p, q = 1, 0, 0
y = a * (x - p)**2 + q

# 関数の式をタイトル表示
plt.title('$y=a(x-p)^2+q$', fontsize=14)

# plot() の戻り値の第1要素を line で受け取る
line, = plt.plot(x, y, linewidth=2)

# スライダの位置
ax_a = plt.axes([0.1, 0.15, 0.8, 0.04])  # type: ignore
ax_p = plt.axes([0.1, 0.10, 0.8, 0.04])  # type: ignore
ax_q = plt.axes([0.1, 0.05, 0.8, 0.04])  # type: ignore
# スライダの設定
slider_a = wg.Slider(ax_a, 'a', -4, 4, valinit=a, valstep=0.05)  # type: ignore
slider_p = wg.Slider(ax_p, 'p', -4, 4, valinit=p, valstep=0.05)  # type: ignore
slider_q = wg.Slider(ax_q, 'q', -4, 4, valinit=q, valstep=0.05)  # type: ignore


# スライダーの変化に応じてグラフを再描画する関数
def update(val):
    sa = slider_a.val
    sp = slider_p.val
    sq = slider_q.val
    # line は plt.plot() の戻り値
    line.set_ydata(sa * (x - sp)**2 + sq)


# スライダーが変化したときに再描画する関数をセットしておく
slider_a.on_changed(update)
slider_p.on_changed(update)
slider_q.on_changed(update)
# グラフを表示して終了
plt.show()
