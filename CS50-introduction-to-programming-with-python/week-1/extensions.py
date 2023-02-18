def main():
    ex = str(input("File name: ")).lower().strip().split('.')[-1]
    print(file_name(ex))


def file_name(ex):
    if ex == "gif" or ex == "png":
        ex = "image/" + ex
        return ex
    elif ex == "jpg" or ex == "jpeg":
        ex = "image/" + "jpeg"
        return ex
    elif ex == "pdf" or ex == "zip":
        ex = "application/" + ex
        return ex
    elif ex == "txt":
        ex = "text/plain"
        return ex
    else:
        return "application/octet-stream"


main()