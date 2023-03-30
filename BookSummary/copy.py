# 将目标源文件复制到指定目录
import re
import os
import shutil
import gen_book_summary


def copy(src_path, gen_path, type="md"):
    # 把文件搜索出来
    files = os.listdir(src_path)
    md_files = []
    re_str = r'.*\.{}'.format(type)
    md_re = re.compile(re_str)
    for file_name in files:
        if md_re.match(file_name):
            src_file_path = src_path + file_name
            dec_file_path = gen_path + file_name
            shutil.move(src_file_path, dec_file_path)


def copy_image(src_path, gen_path):
    shutil.move(src_path, gen_path)


if __name__ == "__main__":
    src_path = "/Users/mac/Documents/030-MySQL实战45讲/"
    gen_path = "/Users/mac/Code/book/mysql-book/src/"
    gen_book_summary.gen_summary_md_file(src_path, gen_path)
    copy(src_path, gen_path)
    copy_image(src_path + "/images", gen_path + "/images")
