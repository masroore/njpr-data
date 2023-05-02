import os
from enum import IntEnum
from gzip import open as gz_open
from lzma import open as lz_open
from typing import Any


class StorageCompression(IntEnum):
    NONE = 0
    GZIP = 1
    LZMA = 2


class Storage(object):
    def __init__(self, base_folder: str, compression: StorageCompression):
        self._base_folder = os.path.abspath(base_folder)
        self.compression = compression
        if self.compression == StorageCompression.NONE:
            self._file_opener = open
            self._ext_suffix = None
        elif self.compression == StorageCompression.GZIP:
            self._file_opener = gz_open
            self._ext_suffix = ".gz"
        elif self.compression == StorageCompression.LZMA:
            self._file_opener = lz_open
            self._ext_suffix = ".xz"

    def resolve_apn_base_folder(self, apn: str) -> str:
        parts = apn.split("_", 2)
        path = os.path.join(self._base_folder, *parts)
        return path

    def save(self, apn: str, section: str, content: Any):
        self.save_file(apn, f"{apn}^{section}.json", content)

    def save_file(self, apn: str, filename: str, content: Any):
        nested_folder = self.resolve_apn_base_folder(apn)
        os.makedirs(nested_folder, exist_ok=True)
        file_path = os.path.join(nested_folder, filename)
        if self._ext_suffix:
            file_path += self._ext_suffix

        if isinstance(content, str):
            content = bytes(content, "utf-8")

        try:
            if self.compression == StorageCompression.GZIP:
                fp = gz_open(file_path, mode="wb", compresslevel=9)
            elif self.compression == StorageCompression.LZMA:
                fp = lz_open(file_path, mode="wb", preset=9)
            else:
                fp = open(file_path, "wb")

            fp.write(content)
        finally:
            fp.close()

    def load(self, apn: str, section: str) -> str | None:
        return self.load_file(apn, f"{apn}^{section}.json")

    def _append_suffix(self, filename: str) -> str:
        if self._ext_suffix and not filename.endswith(self._ext_suffix):
            filename += self._ext_suffix

        return filename

    def _remove_suffix(self, filename: str) -> str:
        if self._ext_suffix and filename.endswith(self._ext_suffix):
            return filename[: -len(self._ext_suffix)]

        return filename

    def load_file(self, apn: str, filename: str) -> str | None:
        nested_folder = self.resolve_apn_base_folder(apn)
        file_path = os.path.join(nested_folder, filename)
        file_path = self._append_suffix(file_path)
        if os.path.exists(file_path):
            with self._file_opener(file_path, "rb") as fp:
                file_content = fp.read().decode("utf-8")
                return file_content
        return None

    def exists(self, apn: str, section: str) -> bool:
        return self.file_exists(apn, f"{apn}^{section}.json")

    def file_exists(self, apn: str, filename: str) -> bool:
        nested_folder = self.resolve_apn_base_folder(apn)
        file_path = os.path.join(nested_folder, filename)
        file_path = self._append_suffix(file_path)
        return os.path.exists(file_path)

    def list_filenames_for_apn(self, apn: str) -> list[str]:
        apn_folder = self.resolve_apn_base_folder(apn)
        return [
            self._remove_suffix(os.path.basename(f))
            for f in os.listdir(apn_folder)
            if os.path.isfile(os.path.join(apn_folder, f))
        ]

    def list_sections_for_apn(self, apn: str) -> list[str]:
        filenames = self.list_filenames_for_apn(apn)
        sections = [os.path.splitext(f)[0].split("^", 1)[1] for f in filenames]
        return sections
