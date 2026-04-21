class Solution:

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
