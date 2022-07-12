
def bulild_index_package(package):
    template = "<a href=\"{relative_path}\">{name}</a>"
    data = {
        "name": package["name"],
        "relative_path": "/package/{}/".format(package["name"])
    }
    return template.format(**data)

def build_index(packages):
    template = "<!DOCTYPE html><html><body>{packages_html}</body></html>"
    packages_html = ""
    for i in packages:
        packages_html += "{}\n".format(bulild_index_package(i))
    data = {
        "packages_html": packages_html
    }
    return template.format(**data)

def build_package_page_package(package):
    template = "<a href=\"{file_path}/\">{name}</a>"
    data = {
        "file_path": "/package/{name}/{file}#{hash_type}:{hash_hex}".format(**package),
        "name": package["name"]

    }
    return template.format(**data)

def build_package_page(package):
    template = "<!DOCTYPE html><html><body>{packages}</body></html>"
    data = {
        "packages" : build_package_page_package(package)
    }
    return template.format(**data)