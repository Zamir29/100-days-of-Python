from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score at the top right
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas configuration with text inside
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        # Buttons
        self.answer_buttons = []
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.answer_buttons.append(self.true_button)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.answer_buttons.append(self.false_button)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self, *_):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.set_buttons_enabled(True)
            # self.true_button.config(state="normal")
            # self.false_button.config(state="normal")
            # self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            total = len(self.quiz.question_list)
            # self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(
                self.question_text,
                text=f"Done!\nYou have reached the end of the questions\n\nFinal Score {self.quiz.score}/{total}")
            self.set_buttons_enabled(False)
            # self.true_button.config(state="disabled")
            # self.false_button.config(state="disabled")

    def true_pressed(self):
        self.set_buttons_enabled(False)
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.set_buttons_enabled(False)
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        # self.true_button.config(state="disabled")
        # self.false_button.config(state="disabled")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")

        self.window.after(1000, self.get_next_question, *())

    def set_buttons_enabled(self, enabled: bool) -> None:
        state = NORMAL if enabled else DISABLED
        for btn in self.answer_buttons:
            btn.config(state=state)