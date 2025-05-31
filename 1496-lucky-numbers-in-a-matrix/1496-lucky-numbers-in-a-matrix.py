class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result =[]
        for i in range(len(matrix)):
            row = matrix[i];
            min_row_val = min(row);
            min_col_index = row.index(min_row_val);

            is_max_in_col = all(matrix[r][min_col_index]<= min_row_val for r in range(len(matrix)));

            if is_max_in_col:
                result.append(min_row_val);
        return result;


