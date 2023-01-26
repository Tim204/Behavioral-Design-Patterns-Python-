from strategy_pattern import filter, compressors


class ImageStorage:
    def __init__(self, compressor, image_filter):
        self._compressor = compressor
        self._filter = image_filter

    def store(self, file_name):
        self._compressor.compress(file_name)
        self._filter.filter(file_name)


image = ImageStorage(compressors.JpegCompressor(), filter.BlackAndWhiteFilter())
image.store("photo")

