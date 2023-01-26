from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, file_name):
        pass


class JpegCompressor(Compressor):
    def compress(self, file_name):
        print(f"Compressing {file_name} using JPG")


class PngCompressor(Compressor):
    def compress(self, file_name):
        print(f"Compressing {file_name} using PNG")
