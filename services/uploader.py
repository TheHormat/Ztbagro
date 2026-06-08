class Uploader:

    @staticmethod
    def upload_photo_for_service(instance, filename):
        return f"service/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_about(instance, filename):
        return f"about/{instance.slug}/{filename}"

    @staticmethod
    def upload_video_for_index(instance, filename):
        return f"video/{instance.slug}/{filename}"

    @staticmethod
    def upload_logo_for_index(instance, filename):
        return f"logo/{instance.slug}/{filename}"
    @staticmethod
    def upload_slider_image_for_index(instance, filename):
        return f"slider/{instance.slug}/{filename}"

    @staticmethod
    def upload_image_for_sidebar(instance, filename):
        return f"sidebar/{instance.slug}/{filename}"

    @staticmethod
    def upload_image_for_favicon(instance, filename):
        return f"favicon/{instance.slug}/{filename}"

    @staticmethod
    def upload_image_for_pages_slider(instance, filename):
        return f"pagesSlide/{instance.slug}/{filename}"