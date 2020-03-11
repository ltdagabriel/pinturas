import re
from pathlib import Path

if __name__ == "__main__":

    a = Path("assets/")
    b = [x for x in a.glob("*") if x.is_dir()]


    file_name = "2020-03-11-"

    for i in b:
        c = i.name
        print(c)
        save_as = Path("_posts/") / (file_name + c + ".md")
        f = save_as.open("w")

        f.write("---\n")
        f.write("title: "+ re.sub("-", " ", c).capitalize() +"\n")
        f.write("categories:\n")
        f.write("  - Pintura\n")
        f.write("tags:\n")
        f.write("gallery:\n")
        for j in i.glob("*"):
            f.write("  - image_path: "+ str(j) +"\n")
            f.write("    url: "+ str(j) +"\n")
        f.write("---\n")