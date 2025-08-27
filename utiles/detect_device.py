def detect_device(page):
    if page.width >= 1200:
        return "desktop"
    elif page.width >= 650:
        return "tablet"
    else:
        return "mobile"