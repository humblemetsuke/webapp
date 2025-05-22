import streamlit as st
from streamlit import session_state

import functions


def add_todo():

    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()


st.title("My To Do Web App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label="enter", placeholder="Enter a new todo:",
              on_change=add_todo, key="new_todo")

print("Hello")

#st.session_state


