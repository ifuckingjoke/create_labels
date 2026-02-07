def cofigure_main_grid(root):
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

def place_main_frames(content_frame, bottom_frame):
    content_frame.grid(row=0, column=0, sticky="nsew")
    bottom_frame.grid(row=1, column=0, sticky="se")