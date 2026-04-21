class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        v0, h0 = 0, 1
        v, h = v0, h0
        n = len(words[v0])

        # [0][1] -> [0][n] == [1][0] -> [n][0]
        # [1][2] -> [1][n] == [2][1] -> [n][1]
        # ...
        # [n][n-1]         == [n-1][n]
        while v<n:
            v, h = v0, h0
            # n = len(words[v0])
            while h<n:
                # if w1 and w2:
                if v0>len(words[v0])-1 or h0>len(words[v0])-1:
                    return False
                w1, w2 = words[v][h], words[h][v]
                print(w1,w2, v0)
                if w1!=w2:
                    return False
                h+=1
            
            h0+=1
            v0+=1
        return True


    def validWordSquare(self, words: List[str]) -> bool:
        v = 0
        n_filas = len(words)

        while v < n_filas:
            # PRIMERO: Verificar que el largo de la fila v 
            # sea igual al largo de la "columna" v
            col_len = 0
            while col_len < n_filas and v < len(words[col_len]):
                col_len += 1
            
            if len(words[v]) != col_len:
                return False

            # SEGUNDO: Comparar caracteres (saltando la diagonal)
            h = v + 1
            while h < len(words[v]):
                # No hace falta re-comprobar límites aquí por el paso anterior
                if words[v][h] != words[h][v]:
                    return False
                h += 1
                
            v += 1
        return True
