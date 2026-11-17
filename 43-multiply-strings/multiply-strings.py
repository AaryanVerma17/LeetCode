class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        q_len, w_len = len(num1), len(num2)
        z_arr = [0] * (q_len + w_len)
        for idx_a in range(q_len - 1, -1, -1):
            for idx_b in range(w_len - 1, -1, -1):
                val_p = int(num1[idx_a]) * int(num2[idx_b])
                pos_x, pos_y = idx_a + idx_b, idx_a + idx_b + 1
                acc_s = val_p + z_arr[pos_y]
                z_arr[pos_y] = acc_s % 10
                z_arr[pos_x] += acc_s // 10
        offset = 0 if z_arr[0] != 0 else 1
        return "".join(map(str, z_arr[offset:]))