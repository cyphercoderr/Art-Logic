def string_to_binary_array(text):
    text = text.split("@")[0][:4] if "@" in text else text[:4]
    binaries = text.encode("utf-8")
    binary_array = [format(byte, "08b") for byte in binaries]
    zeros = 4 - len(text)
    padded_zeros = "".join(["0"] * 8 * zeros)
    start = 0
    end = 8
    while zeros:
        binary_array.append(padded_zeros[start:end])
        start = end
        end = end + 8
        zeros = zeros - 1
    return binary_array[::-1]


def encode(email):
    raw_binary = string_to_binary_array(email)
    output = []
    count = len(raw_binary[0])
    i = 0
    while count:
        for character in raw_binary:
            output.append(character[i])
        i = i + 1
        count = count - 1
    return int("".join(output), 2)


if __name__ == "__main__":
    print(encode("darkcoder.eng@gmail.com"))
