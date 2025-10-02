# # Listing all the files in a directory

# import os

# folder = "C:/Users/empre/OneDrive/Desktop/Python"
# items= os.listdir(folder)

# for i in items:
#     print(i)

# for j in items:
#     item_path = os.path.join(folder, j)
#     if os.path.isfile(item_path):
#         print(j)

# #Creating a QR Code

# import os
# import qrcode

# folder= "C:/Users/empre/OneDrive/Desktop/Python/QRCodes"
# os.makedirs(folder, exist_ok= True)
# data ="https://www.youtube.com/@learnwithladynisy"
# qr = qrcode.make(data)
# qrsave_path = os.path.join(folder, "ladynisy_qr.png")
# qr.save(qrsave_path)


# # Web Scraping
# import os
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.youtube.com/@learnwithladynisy/videos"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# video_links = []
# for a in soup.find_all('a', href= True):
#     href = a['href']
#     if '/watch' in href:
#         video_links.append(f"https://www.youtube.com{href}")
# for link in video_links:
#     print(link)


# # Tic Tac Toe Game
# def print_board(board):
#     # printing current game board
#     print(f"{board[0]}| {board[1]}| {board[2]}")
#     print("-----")
#     print(f"{board[3]}|{board[4]}|{board[5]}")
#     print("-----")
#     print(f"{board[6]}|{board[7]}|{board[8]}")

# def check_winner(board, player):
#     # checking winning combinations
#     winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
#                             [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#     for combo in winning_combinations:
#         if all(board[i] == player for i in combo):
#             return True
#     return False

# def tic_tac_toe():
#     board = [' ' for _ in range(9)]
#     current_player = 'X'
#     for turn in range(9):
#         print_board(board)
#         move = int(input(f"Player {current_player}, enter your move (0-8): "))
#         if board[move] == ' ':
#             board[move] = current_player
#             if check_winner(board, current_player):
#                 print_board(board)
#                 print(f"Player {current_player} wins!")
#                 return
#             current_player = 'O' if current_player == 'X' else 'X'
#         else:
#             print("Invalid move. Try again.")
#     print_board(board)
#     print("It's a draw!")

# if __name__=="__main__":
#     tic_tac_toe()


    


