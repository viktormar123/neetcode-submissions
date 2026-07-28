class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def char_dict(string: str): # Returns a dict that maps char X to count of X in s:
            out_dict = {}
            for idx, char in enumerate(string):
                if char in out_dict:
                    out_dict[char] += 1
                else:
                    out_dict[char] = 0
            
            return out_dict
        
        seen_char_tuples = {} # maps a char dict (stored as sorted list tuple) to a list of indexes

        for idx, string in enumerate(strs):
            current_char_dict = char_dict(string)
            current_char_tuple = tuple(sorted(current_char_dict.items()))

            if current_char_tuple in seen_char_tuples:
                seen_char_tuples[current_char_tuple] += [idx]
            else:
                seen_char_tuples[current_char_tuple] = [idx]
        
        output_list = []
        for idx_list in seen_char_tuples.values():
            strs_list = [strs[idx] for idx in idx_list]
            output_list.append(strs_list)

        return output_list