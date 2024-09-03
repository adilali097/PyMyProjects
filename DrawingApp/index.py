import tkinter as tk
from tkinter import colorchooser, filedialog, simpledialog
from PIL import Image, ImageDraw, ImageTk
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.create_widgets()
        
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
        self.setup_bindings()
        
    def create_widgets(self):
        self.toolbar = tk.Frame(self.root, bg='lightgrey')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self.color_button = tk.Button(self.toolbar, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT)
        
        self.size_button = tk.Button(self.toolbar, text="Brush Size", command=self.choose_brush_size)
        self.size_button.pack(side=tk.LEFT)
        
        self.undo_button = tk.Button(self.toolbar, text="Undo", command=self.undo)
        self.undo_button.pack(side=tk.LEFT)
        
        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_image)
        self.save_button.pack(side=tk.LEFT)
        
        self.load_button = tk.Button(self.toolbar, text="Load", command=self.load_image)
        self.load_button.pack(side=tk.LEFT)
        
        self.brush_color = 'black'
        self.brush_size = 5
        self.last_x, self.last_y = None, None
        self.undo_stack = []
        self.redo_stack = []
        
    def setup_bindings(self):
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color
        
    def choose_brush_size(self):
        size = simpledialog.askinteger("Brush Size", "Enter brush size:", initialvalue=self.brush_size)
        if size:
            self.brush_size = size
    
    def paint(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.brush_color, width=self.brush_size)
            self.draw.line((self.last_x, self.last_y, x, y), fill=self.brush_color, width=self.brush_size)
            self.last_x, self.last_y = x, y
        else:
            self.last_x, self.last_y = event.x, event.y
    
    def reset(self, event):
        self.last_x, self.last_y = None, None
    
    def undo(self):
        # Implement undo functionality
        pass
    
    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.image.save(file_path)
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])
        if file_path:
            self.image = Image.open(file_path)
            self.draw = ImageDraw.Draw(self.image)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
