import tkinter as tk
import numpy as np

GENERAL_DEBUG = True


class App(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.LEADER_BOARD_LIMIT = 10  # max 10 people shown on the leader board
        self.master = master

        #name of players participating in the test
        self.players = ['Ariya Rasekh', 'Brett Shepley', 'Emily Boice', 'Elias Khan', 'Zack Pouget', 'Sawyer King']

        #list of complete(1) & incomplete milestones(0)
        self.milestonesCompleted = [
            [0, 1, 1],
            [0, 0, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 0]
        ]

        #milestones for testing
        self.milestones = ['Test Button', 'Test Slidebar', 'Test Admin']

        #weight of each milestone
        self.milestone_weight = [10, 20, 30]

        #create a GUI tableframe and show the final score in it
        self.tableFrame = tk.Frame(self.master)
        self.tableFrame.pack(side='left', padx=20, pady=10)
        self.create_table(self.tableFrame)
        self.player_score = self.calculate_final_score()
        if GENERAL_DEBUG:   print(f"self.player_score: {self.player_score}")

        self.leader_board_Frame = tk.Frame(self.master, highlightbackground="blue", highlightthickness=2)
        self.leader_board_Frame.pack(side='right', padx=20)
        self.create_leader_board(self.leader_board_Frame)

    def calculate_final_score(self):
        """
        to calculate players final score based on milestone_weight
        :return: numpy array in this format -> [[final score of player1, player's name] , ... ]
        """

        final_score_list = []
        for user_number in range(len(self.players)):
            final_score = 0
            for milestone_number in range(len(self.milestones)):
                score = self.milestone_weight[milestone_number] if self.milestonesCompleted[user_number][
                    milestone_number] else 0
                final_score += score
            final_score_list.append([final_score, self.players[user_number]])

        final_score_array = np.array([i for i in final_score_list])
        return final_score_array

    def create_table(self, master):
        for i in range(len(self.players)):  # creating players
            tk.Label(master, text=self.players[i]).grid(row=i + 1, column=0)  # players

            for j in range(len(self.milestones)):
                completion_status_text = "not completed" if self.milestonesCompleted[i][j] == 0 else "completed"

                tk.Label(master, text=completion_status_text).grid(row=i + 1, column=j + 1)

        for i in range(len(self.milestones)):  # writing milestones
            tk.Label(master, text=self.milestones[i]).grid(row=0, column=i + 1)

    def create_leader_board(self, master):
        """
            gets unsorted player info [[final score, player 1], ... ]
            prints leader board
        """
        self.player_score = self.player_score[
            self.player_score[:, 0].argsort()[::-1]]  # sorting based on palyer score - decreasing
        for index, player_info in enumerate(self.player_score):
            if index == self.LEADER_BOARD_LIMIT:
                break

            if index == 0:
                tk.Label(master, justify="right", text=f"{index+1}. {player_info[1]}   {player_info[0]}",
                         fg='#FFD700').grid(column=0, row=index)

            elif index == 1:
                tk.Label(master, justify="right", text=f"{index+1}. {player_info[1]}   {player_info[0]}",
                         fg='#C0C0C0').grid(column=0, row=index)

            elif index == 2:
                tk.Label(master, justify="right", text=f"{index+1}. {player_info[1]}   {player_info[0]}",
                         fg='#CD7F32').grid(column=0, row=index)

            else:
                tk.Label(master, justify="right", text=f"{index+1}. {player_info[1]}   {player_info[0]}").grid(column=0,
                                                                                                             row=index)


if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()