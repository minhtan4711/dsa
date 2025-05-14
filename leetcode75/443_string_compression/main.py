class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n == 0:
            return 0

        read_ptr = 0
        write_ptr = 0

        while read_ptr < n:
            current_char = chars[read_ptr]
            count = 0

            while read_ptr < n and chars[read_ptr] == current_char:
                read_ptr += 1
                count += 1

            chars[write_ptr] = current_char
            write_ptr += 1

            if count > 1:
                count_str = str(count)
                for digit_char in count_str:
                    chars[write_ptr] = digit_char
                    write_ptr += 1

        return write_ptr
