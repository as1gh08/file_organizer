import os
import shutil


def get_expansion(file: str) -> str:
    if "." in file:
        index = file.rfind(".")
        try:
            return file, file[index:]

        except TypeError:
            return None  # If index = None we do exception
    return None


def organize_file(file: str, expansion: str, path: str) -> bool:
    file_expansions: dict = {
        ".txt": "Text_Files",
        ".exe": "Exe_Files",
        ".bat": "Bat_Files",
        ".dll": "Dll_Files",
        ".c": "C_Files",
        ".cpp": "Cpp Files",
        ".py": "Python Files",
        ".php": "Php Files",
        ".css": "CSS Files",
        ".html": "HTML Files",
        ".png": "Png Images",
        ".jpg": "JPG Images",
        ".jpeg": "JPEG Images",
        ".mp4": "MP4 Videos",
        ".mp3": "MP3"

    }
    if file_expansions.get(expansion) != None:
        try:
            os.mkdir(f"{path}\\{file_expansions.get(expansion)}")
        except FileExistsError:
            pass
        shutil.copy(f"{path}\\{file}",
                    f"{path}\\{file_expansions.get(expansion)}")
        os.remove(f"{path}\\{file}")
        return True
    try:
        os.mkdir(f"{path}\\Other")
    except FileExistsError:
        pass
    shutil.copy(f"{path}\\{file}",
                f"{path}\\Other")
    os.remove(f"{path}\\{file}")
    return False


if __name__ == "__main__":
    path: str = input("Print path:\n")
    files: list = os.listdir(fr"{path}")
    for i in files:
        if get_expansion(i) != None:
            organize_file(file=get_expansion(
                i)[0], expansion=get_expansion(i)[1], path=fr"{path}")
