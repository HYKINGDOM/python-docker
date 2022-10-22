import os
import time

from pathlib import Path

DIRECTORIES = {
    "图片": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
             ".heif", ".psd"],
    "文档": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
             ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
             ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
             "pptx", ".csv", ",pdf"],
    "压缩文件": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "影音": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
             ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "文本": [".txt", ".in", ".out"],
    "编程": [".py", ".html5", ".html", ".htm", ".xhtml", ".c", ".cpp", ".java", ".css"],
    "可执行程序": [".exe"],
}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def auto_organize(dirval):
    # 整理对应的文件夹下的文件
    for entry in os.scandir(dirval):
        if entry.is_dir():
            # 如果是文件夹则跳过
            continue
        file_path = Path(dirval + "\\" + entry.name)
        file_format = file_path.suffix.lower()
        # 避免后缀大小写判断问题，全转为小写
        if file_format in FILE_FORMATS:
            directory_path = Path(dirval + "\\" + FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_curr_path = entry.path
            file_curr_name = entry.name
            if file_path.samefile(entry.path):
                file = os.path.splitext(file_curr_name)
                millis = int(round(time.time() * 1000))
                filename, type = file
                new_file_name = str(millis)
                file_new_path = str(file_curr_path).replace(filename,new_file_name)
                os.rename(file_curr_path, file_new_path)
                print(file_curr_name, '======>', str(millis) + type)
                file_curr_name = str(millis) + type
            else:
                print(file_curr_name)
            file_path.rename(directory_path.joinpath(file_curr_name))

    try:
        os.mkdir(dirval + "\\" + "其他文件")
    except:
        pass

    for dir in os.scandir(dirval):
        try:
            if dir.is_dir():
                # 删除空文件夹
                os.rmdir(dir)
            else:
                temp = str(Path(dir)).split('\\')
                # 分割文件路径
                path = '\\'.join(temp[:-1])
                print(path + '\\其他文件\\' + str(temp[-1]))
                os.rename(str(Path(dir)), path + '\\其他文件\\' + str(temp[-1]))
        except:
            pass


if __name__ == "__main__":
    auto_organize(r"L:\迅雷下载")
