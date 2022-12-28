# take input - ignore case/outer spaces - return media type
def main():
    file = suf(input("File name: ").casefold().strip())
    print(mime(file))

# sep suffix
def suf(x):
    end = x.rpartition(".")[2]
    return "." + end


# match suffix to media type
def mime(n):
    match n:
        case ".gif":
            return("image/gif")
        case ".jpg" | ".jpeg":
            return("image/jpeg")
        case ".png":
            return("image/png")
        case ".pdf":
            return("application/pdf")
        case ".txt":
            return("text/plain")
        case ".zip":
            return("application/zip")
        case _:
            return("application/octet-stream")

main()