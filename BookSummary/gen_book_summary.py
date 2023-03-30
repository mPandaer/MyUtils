import os;
import re;

# 搜索文件路径 并生成 
# - [01-基础架构：一条SQL查询语句是如何执行的？](./01-基础架构：一条SQL查询语句是如何执行的？.md)
# 只需要读取文件名就可以了 写入文件就可以了
def gen_summary_md_file(src_path,gen_path):
    fmt_str = "- [{}](./{})"
    head = "# Summary\n"
    md_re = re.compile(r".*\.md$")
    dirs = os.listdir(src_path)
    print(type(dirs))
    # print(dirs)
    md_files = []
    # md_files = md_re.findall(dirs)
    for name in dirs:
        if md_re.match(name):
            if("开篇" in name) :
                name = "00-" + name
            md_files.append(name)
    with open(gen_path + "SUMMARY.md","w",encoding="utf=8") as file:
        file.write(head)
        for name in md_files:
            title = name[:-3]
            line = fmt_str.format(title,name);
            # file.write(line)
            file.write(line + "\n")
    print("文件生成成功")


if __name__ == "__main__":
    src_path = "E:\\doc\\030-MySQL实战45讲\\"
    gen_path = "E:\\doc\\books\\my-firstbook\\src\\"
    gen_summary_md_file(src_path,gen_path)
    print("复制成功") 

