from block_md import markdown_to_html_node, extract_title
import os, shutil, sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    static_dir = "./static/"
    public_dir = "./docs"
    source_copying(static_dir, public_dir)
    generate_pages_recursive("content", "template.html", "docs",basepath)


def source_copying(source_dir,target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    for filename in os.listdir(source_dir):
        original_path = os.path.join(source_dir,filename)
        new_path = os.path.join(target_dir,filename)
        print(f"Moving {original_path} to {new_path}")
        if os.path.isfile(original_path):
            shutil.copy(original_path,new_path)
        else:
            source_copying(original_path,new_path)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_data = f.read()
    with open(template_path) as f:
        template_data = f.read()
    md_from_data = markdown_to_html_node(from_data) 
    md_from_html = md_from_data.to_html()
    title = extract_title(from_data) 
    template_data = template_data.replace("{{ Title }}", title)
    template_data = template_data.replace("{{ Content }}", md_from_html)
    template_data = template_data.replace('href="/', f'href="{basepath}')
    template_data = template_data.replace('src="/', f'src="{basepath}')
    dir_name = os.path.dirname(dest_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_data)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for content in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, content) 
        if os.path.isfile(file_path) and file_path.endswith(".md"):
            new_file_name = content.replace(".md",".html")
            new_dest_dir_path = os.path.join(dest_dir_path, new_file_name)
            generate_page(file_path, template_path, new_dest_dir_path, basepath)
        elif os.path.isdir(file_path):
            new_dest_dir_path = file_path.replace("content", "docs")
            generate_pages_recursive(file_path, template_path, new_dest_dir_path, basepath)




if __name__ == "__main__":
    main()
