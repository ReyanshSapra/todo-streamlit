import streamlit as st
from datetime import datetime

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(layout="centered", page_title="To-Do List", page_icon="📝")

st.title("📝 To-Do List")
st.markdown("Add tasks, mark them complete, or delete them!")

new_task = st.text_input("Add Tasks below...", key="new_task_input")

if st.button("Add Task", key="add_task_button"):
    if new_task.strip():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.session_state.tasks.append({
            "task": new_task.strip(),
            "completed": False,
            "timestamp": current_time
        })
        st.rerun() 
    else:
        st.warning("Please enter a task!")

st.markdown("---")

if not st.session_state.tasks:
    st.info("No tasks yet! Add one above.")
else:
    for i, task_item in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])

        with col1:
            is_completed = st.checkbox(f" ", value=task_item["completed"], key=f"checkbox_{i}")
            if is_completed != task_item["completed"]:
                st.session_state.tasks[i]["completed"] = is_completed
                st.rerun() 

        with col2:
            task_display = task_item["task"]
            if task_item["completed"]:
                st.markdown(f"<p style='text-decoration: line-through; color: grey;'>{task_display} <br><small>{task_item['timestamp']}</small></p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p>{task_display} <br><small>{task_item['timestamp']}</small></p>", unsafe_allow_html=True)

        with col3:
            if st.button("Delete", key=f"delete_{i}"):
                del st.session_state.tasks[i]
                st.rerun() 

st.markdown("---")
st.warning("If you close the app, all tasks will be deleted!")
