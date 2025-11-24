# Day 34 — GUI Quiz App with API
[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2034-Open%20Folder-blue)](../day-34/main.py)
## 📘 Table of contents

* [Concepts Learned](#concepts-learned)
* [Challenges](#challenges)
* [Solutions / Insights](#solutions--insights)
* [Next steps](#next-steps)
---
## Concepts Learned

* **Separation of concerns (OOP)**:  
`Question (data) → QuizBrain (logic/state) → QuizInterface (presentation)`

* **Dependency Injection**:
Pass a QuizBrain instance into QuizInterface(quiz) instead of creating it inside the UI.

* **Event-driven UI with Tkinter**:    
Callbacks via command=..., non-blocking delays with after(ms, func, *args).

* **State hygiene for widgets**:  
Centralized set_buttons_enabled(True/False) controlling state = NORMAL, DISABLED.

* **Score update timing**:
Move label refresh to give_feedback (right after check_answer) so the last answer is reflected immediately.

* **Image lifecycle in Tkinter**:  
Keep PhotoImage on self to prevent garbage collection.

* **Constants & correctness**:  
Use NORMAL, DISABLED (not string typos like "normale").

* **Type hints & signatures**:
`get_next_question(self, *_)` plays nice with after; understood PyCharm’s optional *args quirk.

## Challenges

* **PyCharm warning on after’s `*args`**:  
Annoying inspector message despite correct code.

* **Buttons double-click race**:  
Potential for rapid second click before disable.

* **End-of-quiz score mismatch**:  
Label lagging one step behind on the very last question.

## Solutions / Insights

* **Silenced after warnings**:
Use `*()` or `lambda: self.get_next_question()` or accept `*_` in the handler.

* **Race fixed**:  
Disable buttons immediately in `true_pressed`/`false_pressed`, not later.

* **Final score always correct**:  
Update score label inside give_feedback (and show final summary on the canvas).

* **Cleaner, scalable UI control**:  
Kept answer_buttons list and looped to apply state changes—easy to extend later.

## Next Steps

* Shuffle & Reset

* Add optional shuffle (and seed) in `QuizBrain.__init__` and a reset() method.

* Add a “Play again” button in the UI that calls quiz.reset(shuffle=True) → get_next_question().

### Keyboard Shortcuts (UX)

Bind <Right> → True, <Left> → False via self.window.bind.

### Tiny Refactors

Extract `_update_score_label()` and constants: `FEEDBACK_DELAY_MS`, `QUESTION_WIDTH`.

### Stretch (when ready)

Settings dialog (number of questions, difficulty).  
Multiple choice layout (4 buttons) with randomized options.  
Simple network guardrails if you refetch from an API (timeouts, retry).