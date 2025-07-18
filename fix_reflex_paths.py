import os
import re
from pathlib import Path
import importlib.util

# 1. 读取 yue_in/rxconfig.py 中的 deploy_url
def load_deploy_url(config_path="yue_in/rxconfig.py"):
    spec = importlib.util.spec_from_file_location("rxconfig", config_path)
    rxconfig = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rxconfig)
    return rxconfig.config.deploy_url

# 2. 替换 HTML 中以 "/" 开头的资源路径
def fix_paths_in_html(deploy_url, html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    if deploy_url == ".":
        # 变成 ./xxx
        new_content = re.sub(r'=(["\'])/([^"\']+)', r'=\1./\2', content)
    else:
        deploy_url = deploy_url.rstrip("/")
        # 变成 /My_WebSite/xxx
        new_content = re.sub(r'=(["\'])/([^"\']+)', rf'=\1{deploy_url}/\2', content)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)

# 3. 扫描 public 文件夹下所有 html
def main():
    export_dir = Path("public")
    if not export_dir.exists():
        print("❌ public 文件夹不存在，请确认是否已解压导出文件")
        return

    try:
        deploy_url = load_deploy_url()
        print(f"📦 读取到 deploy_url = {deploy_url}")
    except Exception as e:
        print(f"⚠️ 无法读取 deploy_url：{e}")
        return

    html_files = list(export_dir.rglob("*.html"))
    if not html_files:
        print("⚠️ public 文件夹中未找到 HTML 文件")
        return

    for html_file in html_files:
        fix_paths_in_html(deploy_url, html_file)
        print(f"✅ 修复: {html_file}")

    print("🎉 所有路径已修复完成！")

if __name__ == "__main__":
    main()
