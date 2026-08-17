import streamlit as st

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="centered"
)

if "students" not in st.session_state:
    st.session_state.students = []

st.title("🎓 Student Management System")
st.write("A simple browser-based version of the Python Student Management System.")

menu = st.sidebar.radio(
    "Choose an operation",
    ["Add Student", "View Students", "Search Student", "Update Student", "Delete Student"]
)

if menu == "Add Student":
    st.header("Add Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    marks = st.text_input("Student Marks")

    if st.button("Add Student"):
        if not name or not roll or not marks:
            st.warning("Please fill in all fields.")
        elif any(s["roll"] == roll for s in st.session_state.students):
            st.warning("A student with this roll number already exists.")
        else:
            st.session_state.students.append({
                "name": name,
                "roll": roll,
                "marks": marks
            })
            st.success("Student Added Successfully!")

elif menu == "View Students":
    st.header("Student List")

    if not st.session_state.students:
        st.info("No students found.")
    else:
        for student in st.session_state.students:
            with st.container(border=True):
                st.write(f"**Name:** {student['name']}")
                st.write(f"**Roll:** {student['roll']}")
                st.write(f"**Marks:** {student['marks']}")

elif menu == "Search Student":
    st.header("Search Student")

    roll = st.text_input("Enter Roll Number to Search")

    if st.button("Search"):
        found = next(
            (s for s in st.session_state.students if s["roll"] == roll),
            None
        )

        if found:
            st.success("Student Found")
            st.write(f"**Name:** {found['name']}")
            st.write(f"**Roll:** {found['roll']}")
            st.write(f"**Marks:** {found['marks']}")
        else:
            st.warning("Student not found.")

elif menu == "Update Student":
    st.header("Update Student")

    roll = st.text_input("Enter Roll Number to Update")

    if st.button("Find Student"):
        found = next(
            (s for s in st.session_state.students if s["roll"] == roll),
            None
        )

        if found:
            st.session_state.update_roll = roll
            st.session_state.update_name = found["name"]
            st.session_state.update_marks = found["marks"]
        else:
            st.warning("Student not found.")

    if "update_roll" in st.session_state:
        new_name = st.text_input("New Name", value=st.session_state.update_name)
        new_marks = st.text_input("New Marks", value=st.session_state.update_marks)

        if st.button("Update Student"):
            for student in st.session_state.students:
                if student["roll"] == st.session_state.update_roll:
                    student["name"] = new_name
                    student["marks"] = new_marks
                    break

            del st.session_state.update_roll
            del st.session_state.update_name
            del st.session_state.update_marks
            st.success("Student Updated Successfully!")

elif menu == "Delete Student":
    st.header("Delete Student")

    roll = st.text_input("Enter Roll Number to Delete")

    if st.button("Delete Student"):
        found = next(
            (s for s in st.session_state.students if s["roll"] == roll),
            None
        )

        if found:
            st.session_state.students.remove(found)
            st.success("Student Deleted Successfully!")
        else:
            st.warning("Student not found.")

st.divider()
st.caption("Student Management System | Python + Streamlit")
