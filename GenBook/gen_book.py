"""
本脚本的作用是将需要阅读的md文件通过 mdbook 生成好看的文档
mdbook 需要一定的格式以及一个固定的文件 SUMMARY.md 固定的文件中有固定的格式
"""
import re
import os
import shutil


def get_mds_name(path):
    files_list = os.listdir(path)
    md_re = re.compile(r".*\.md")
    md_list = []
    for file_name in files_list:
        if md_re.match(file_name):
            md_list.append(file_name)
    return sorted(md_list)


def gen_summary_file(md_files_path, des_path):
    """
    用于生成SUMMARY.md文件
    :param md_files_path: md文件的目录 记得末尾的/
    :param des_path: SUMMARY.md文件要放置的目录 记得末尾的/
    """
    # 通过md_files_path获得md的文件名
    HEAD = "# SUMMARY"
    line_fmt = "- [{}]({})"
    md_list = get_mds_name(md_files_path)
    with open(os.path.join(des_path, "SUMMARY.md"), mode="w", encoding="utf-8") as file:
        file.write(HEAD + "\n")
        for md_name in md_list:
            file.write(line_fmt.format(md_name[:-3], f"./{md_name}") + "\n")
    print("SUMMARY.md文件生成成功")


def copy_md_file(src_path, des_path):
    """
    实现将一个地方的md文件复制到另一个地方
    :param src_path: md文件原地方
    :param des_path: md文件移动到的新地方
    :return: 暂无
    """
    md_list = get_mds_name(src_path)
    for md_name in md_list:
        src = os.path.join(src_path, md_name)
        des = os.path.join(des_path, md_name)
        shutil.copy(src, des)
    print("复制md文件完成")


def copy_images(src_path, des_path, dir="images"):
    """
    复制md文件中用到的文件
    :param src_path: md所在的目录
    :param des_path: md要去的目录
    :return: 暂无
    """
    shutil.copytree(os.path.join(src_path, dir), os.path.join(des_path, dir))
    print("图片复制完成")


def main(src, des, book_name):
    """
    执行主流程
    1. 通过命令利用 mdbook init 初始化一本书的结构
    2. 复制数据
        1. 生成SUMMARY.md文件
        2. 复制md源文件
        3. 迁移图片
    :return: 暂无
    """
    os.chdir(des)
    cmd = f"mdbook init {book_name}"
    os.system(cmd)
    des = os.path.join(des, book_name + "/src")
    gen_summary_file(src, des)
    copy_md_file(src, des)
    copy_images(src, des)
    print("全部流程都已经完成,查看文件是否正确")


if __name__ == '__main__':
    md_files_path = "/Users/mac/Documents/030-MySQL实战45讲/"
    des_path = "/Users/mac/Code/book"
    main(md_files_path, des_path, "mysql-book")
