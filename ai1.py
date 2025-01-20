class CornerPriorityAI(nekoAI):
    def __init__(self):
        super().__init__()

    def evaluate(self, board, player):
        """
        評価関数：
        角の位置を高く評価し、角の隣接位置を中程度に評価する
        """
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        adjacent_to_corners = [(1, 0), (0, 1), (6, 7), (7, 6), (6, 0), (7, 1), (0, 6), (1, 7)]

        score = 0

        # 角の位置を評価
        for corner in corners:
            if board[corner[0]][corner[1]] == player:
                score += 100  # 角を取ったら高評価
            elif board[corner[0]][corner[1]] == -player:
                score -= 100  # 相手が角を取ったら低評価

        # 角の隣接位置を評価
        for adj in adjacent_to_corners:
            if board[adj[0]][adj[1]] == player:
                score += 10  # 隣接位置を取ったら中評価
            elif board[adj[0]][adj[1]] == -player:
                score -= 10  # 相手が隣接位置を取ったら低評価

        return score

    def get_best_move(self, board, player):
        """
        角を取ることを最優先にする手を選ぶ
        """
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

        # 最初に角を取れる手を探す
        for corner in corners:
            if board[corner[0]][corner[1]] == 0:  # 角が空いている場合
                return corner

        # 角の隣接位置を優先
        adjacent_to_corners = [(1, 0), (0, 1), (6, 7), (7, 6), (6, 0), (7, 1), (0, 6), (1, 7)]
        for adj in adjacent_to_corners:
            if board[adj[0]][adj[1]] == 0:  # 隣接位置が空いている場合
                return adj

        # それ以外の最適手を評価関数に基づいて選ぶ
        return super().get_best_move(board, player)
