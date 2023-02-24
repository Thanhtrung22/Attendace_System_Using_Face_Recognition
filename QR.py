import cv2
from tkinter import *
from tkinter import filedialog
from pyzbar.pyzbar import decode
from PIL import Image,ImageTk
class QR:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Pannel")
        self.root.geometry("1366x768+0+0")
        
        bg1=Image.open(r"C:\Users\Admin\Python_Test_Projects\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        # Tạo nút Quét Mã QR
        self.scan_button = Button(root, text="Quét Mã QR", command=self.open_image)
        self.scan_button.pack(pady=10)

        # Tạo một khu vực để hiển thị kết quả
        self.result_label = Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def open_image(self):
        # Cho phép người dùng chọn một ảnh và trả về đường dẫn
        filename = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
        if filename:
            # Quét mã QR từ ảnh và hiển thị kết quả
            decoded = self.decode_qr_code(filename)
            if decoded:
                self.result_label.config(text="Kết quả: " + decoded)
            else:
                self.result_label.config(text="Không tìm thấy mã QR.")

    def decode_qr_code(self, filename):
        # Load ảnh và chuyển đổi sang grayscale
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Quét mã QR và trả về kết quả (nếu có)
        decoded = decode(gray)
        if decoded:
            return decoded[0].data.decode()
        else:
            return None
if __name__ == "__main__":
    root = Tk()
    object=QR(root)
    root.mainloop()
