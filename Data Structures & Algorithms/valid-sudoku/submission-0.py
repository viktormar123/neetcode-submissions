class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def confirm_digit_dict(nums: List[str]) -> bool:
            digit_dict = {}
            for idx, num in enumerate(nums):
                if num != '.':
                    if num not in digit_dict:
                        digit_dict[num] = True
                    else:
                        return False
            else:
                return True

                
        for row_idx, row in enumerate(board):
            col = [board[_][row_idx] for _ in range(9)]
            
            ninth_col_res = row_idx % 3 # 0 for columns 0-2, 1 for columns 3-5, 2 for columns 6-8 
            ninth_row_res = row_idx // 3 # 0 for rows 0-2, 1 for rows 3-5, 2 for rows 6-8
                # easy to shift the quadrant box, we simply add 3*ninth_row_res to the first input, and similar for the second  
            ninth = [] 
            for i in range(3):
                for j in range(3):
                    ninth.append(board[i+3*ninth_row_res][j+3*ninth_col_res])
        
            valid_row = confirm_digit_dict(row)
            valid_col = confirm_digit_dict(col)
            valid_ninth = confirm_digit_dict(ninth)

            valid = valid_row * valid_col * valid_ninth
            if valid == False:
                return False
        else:
            return True
