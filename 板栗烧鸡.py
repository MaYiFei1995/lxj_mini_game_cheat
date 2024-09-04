import time
import threading
from pynput import keyboard, mouse

# 鼠标控制器
mouse_controller = mouse.Controller()  # 连续点击线程


def click_thread():
    for _ in range(110):
        mouse_controller.click(mouse.Button.left)
        time.sleep(0.05)  # 调整点击间隔


# 拖动线程
def drag_thread():
    initial_x, initial_y = mouse_controller.position  # 保存初始位置
    drag_distance = -200  # 负值表示向左拖动
    repetitions = 30  # 拖动重复次数
    steps = 5  # 拖动过程中的步数，越多越平滑
    step_x = drag_distance // steps

    for _ in range(repetitions):
        mouse_controller.press(mouse.Button.left)
        for _ in range(steps):
            mouse_controller.move(step_x, 0)
            time.sleep(0.01)  # 调整拖动速度
        mouse_controller.release(mouse.Button.left)
        mouse_controller.position = (initial_x, initial_y)  # 重置鼠标位置
        time.sleep(0.05)  # 每次拖动后的延迟


# 键盘监听器
def on_press(key):
    if key == keyboard.Key.ctrl_l:
        threading.Thread(target=click_thread).start()
    elif key == keyboard.Key.ctrl_r:
        threading.Thread(target=drag_thread).start()
    elif key == keyboard.Key.alt_l:
        exit(0)


if __name__ == "__main__":
    # 监听键盘事件
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
