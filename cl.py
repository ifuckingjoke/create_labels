import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from create_labels.GUI.ui import Application #type: ignore

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()