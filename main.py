import pyautogui
from time import sleep

def perform_actions():
    # Cấu hình an toàn và hiệu quả
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.1  # Giảm thời gian chờ giữa các thao tác
    
    try:
        # Cuộn xuống dưới
        pyautogui.moveTo(1754, 148, duration=0.3)
        pyautogui.scroll(-10000)
        print("✓ Đã cuộn xuống dưới")
        
        # Nhấp vào nút rời nhóm
        pyautogui.moveTo(1586, 1018, duration=0.3)
        pyautogui.click()
        print("✓ Đã nhấp vào nút rời nhóm")
        
        # Chọn rời nhóm trong im lặng
        pyautogui.moveTo(1165, 540, duration=0.2)
        pyautogui.click()
        print("✓ Đã chọn rời nhóm trong im lặng")
        
        # Xác nhận rời nhóm
        pyautogui.moveTo(1133, 641, duration=0.2)
        pyautogui.click()
        print("✓ Đã xác nhận rời nhóm")
        
        return True
    except pyautogui.FailSafeException:
        print("\n⚠️ Đã kích hoạt cơ chế an toàn - Di chuyển chuột vào góc màn hình để dừng")
        return False
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        return False

def main():
    print("\n=== Tự động rời nhóm ===")
    print("• Di chuyển chuột vào góc màn hình để dừng")
    print("• Nhấn Ctrl+C để thoát")
    print("• Nhấn Enter để thực hiện")
    
    while True:
        try:
            input("\nNhấn Enter để bắt đầu...")
            if perform_actions():
                print("\n✓ Thao tác hoàn tất")
            
        except KeyboardInterrupt:
            print("\n\nChương trình đã được dừng bởi người dùng")
            break

if __name__ == "__main__":
    main()