import streamlit as st
import functions
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()
todos2 = functions.write_todos(todos)

st.title("Todo App")
st.header("Welcome to the app.")
st.text("these are your current todos below.")
st.text_input(label=" ",
              placeholder="Enter your todos here...",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()