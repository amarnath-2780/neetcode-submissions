class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            # Pattern: [length] + [delimiter] + [content]
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        
        while i < len(s):
            # Find the position of the next delimiter starting from index i
            j = s.find('#', i)
            
            # The characters between i and j represent the length of the string
            length = int(s[i:j])
            
            # The actual string starts right after the '#'
            start = j + 1
            end = start + length
            
            # Extract the string and add to our list
            decoded_list.append(s[start:end])
            
            # Move the pointer to the start of the next encoded block
            i = end
            
        return decoded_list