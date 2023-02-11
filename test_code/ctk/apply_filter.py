def apply_filter(image, filter):
    if filter == "blur":
        return image.filter(ImageFilter.BLUR)
    elif filter == "gaussian_blur":
        return image.filter(ImageFilter.GaussianBlur)
    elif filter == "contour":
        return image.filter(ImageFilter.CONTOUR)
    elif filter == "detail":
        return image.filter(ImageFilter.DETAIL)
    elif filter == "edge_enhance":
        return image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == "edge_enhance_more":
        return image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == "emboss":
        return image.filter(ImageFilter.EMBOSS)
    elif filter == "find_edges":
        return image.filter(ImageFilter.FIND_EDGES)
    elif filter == "smooth":
        return image.filter(ImageFilter.SMOOTH)
    elif filter == "smooth_more":
        return image.filter(ImageFilter.SMOOTH_MORE)
    elif filter == "sharpen":
        return image.filter(ImageFilter.SHARPEN)
    else:
        return image
