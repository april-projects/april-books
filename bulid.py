import os

# 获取当前目录
current_directory = os.getcwd()

# 生成Markdown表格
table_content = "| 名称 | 描述 | 京东 | 当当 |\n|------|------|----|----------|\n"

# 使用os.walk遍历目录结构
for folder_path, _, files in os.walk(current_directory):
    for file_name in files:
        # 仅处理后缀为.pdf或.md的文件，并过滤README.md文件
        if file_name.endswith(('.pdf', '.md')) and file_name.lower() != 'readme.md':
            # 获取文件名（去掉后缀）
            file_base_name, _ = os.path.splitext(file_name)

            # 生成相对路径的超链接
            file_relative_path = os.path.relpath(os.path.join(folder_path, file_name))
            file_link = f"[{file_base_name}]({file_relative_path})"

            # 生成超链接
            jd_link = f"[{file_base_name}]()"
            dangdang_link = f"[{file_base_name}]()"

            # 生成Markdown表格行
            table_content += f"| {file_link} | **描述** | {jd_link} | {dangdang_link} |\n"

# 写入到README.md
with open("README.md", "w") as readme_file:
    readme_file.write(table_content)

print("README.md generated successfully.")