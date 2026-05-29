import ctypes

buffer = ctypes.create_string_buffer(10)

data = b"AAAAAAAAAAAAAAAAAAAA"

try:
    ctypes.memmove(buffer, data, len(data))
    print(buffer.raw)
except Exception as e:
    print("Eroare:", e)