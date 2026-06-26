class Solution:

    def encode(self, strs: List[str]) -> str:
        return f'{len(strs)}' + '_' + '","'.join(strs)

    def decode(self, s: str) -> List[str]:
        split_i = 0
        for i in range(len(s)):
            if split_i:
                continue
            if s[i] == '_':
                split_i = i
        prefix = s[:split_i]
        encoded = s[split_i+1:]
        return encoded.split('","') if prefix != '0' else []