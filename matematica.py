
class Matematica:

    def ajustar_diagonal(self, linha, pivot):
        linha = [round(x / pivot, 4) for x in linha]
        return linha
 
    def escalonar(self, sistema):

        index = 0

        tam = len(sistema)

        for i in range(tam):


            index = i % tam

            print(index)

            pivot = sistema[index][index]

            if pivot != 1:
                sistema[index] = self.ajustar_diagonal(sistema[index], pivot)

            for j in range(len(sistema[index])-1):

                sistema[index][j] = (-(sistema[index][j]/pivot) * sistema[j][index]) + sistema[index][j]



        # for i in range(len(sistema)):
        #
        #     diag = sistema[i][i]
        #
        #     index = 0
        #
        #     for j in range(len(sistema[i])-1):
        #
        #         index += 1
        #
        #         if i == j:
        #             continue
        #
        #         sistema[j][i] = (diag * sistema[j][i]) - sistema[j][i]

            #print(i, index, sistema[i][index])
            #sistema[i][index] = (diag * sistema[i][index]) - sistema[i][index]



        return sistema
        
    # def escalonar(self, coeficientes):
    #
    #     self.row_reduce(coeficientes)
    #     return coeficientes
    #
    # def pivot(self, matrix, row):
    #     """
    #     Retorna a linha com o maior valor absoluto na coluna atual.
    #     Se todos os valores da coluna forem iguais a zero, retorna -1.
    #     """
    #
    #     max_value = 0
    #     max_row = -1
    #
    #     for i in range(row, len(matrix)):
    #         if abs(matrix[i][row]) > max_value:
    #             max_value = abs(matrix[i][row])
    #             max_row = i
    #
    #     return max_row
    #
    # def swap_rows(self, matrix, row1, row2):
    #     """ Troca as linhas row1 e row2 da matriz """
    #     matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    #
    # def row_reduce(self, matrix):
    #     """ Realiza o escalonamento da matriz """
    #     num_rows = len(matrix)
    #     num_cols = len(matrix[0])
    #
    #     for i in range(num_rows):
    #
    #         for linha in matrix:
    #             print(linha)
    #
    #         print()
    #
    #         pivot_row = self.pivot(matrix, i)
    #
    #         # Se todos os valores da coluna forem iguais a zero, passa para a próxima coluna
    #         if pivot_row == -1:
    #             continue
    #
    #         # Troca a linha atual pela linha com o maior valor absoluto na coluna atual
    #         self.swap_rows(matrix, i, pivot_row)
    #
    #         # Divide a linha atual pelo pivô
    #         pivot_value = matrix[i][i]
    #         for j in range(i, num_cols):
    #             matrix[i][j] /= pivot_value
    #
    #         # Zera os elementos abaixo do pivô na coluna atual
    #         for j in range(i+1, num_rows):
    #             factor = matrix[j][i]
    #             for k in range(i, num_cols):
    #                 matrix[j][k] -= factor * matrix[i][k]
    #
    #     return matrix
