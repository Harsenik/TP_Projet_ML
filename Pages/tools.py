import streamlit as st
import textwrap

# Set up page configuration
st.set_page_config(page_title="Streamlit Tool Showcase", layout="wide")

# App Title
st.title("Streamlit Component Showcase with Visual Examples")
st.write("Explore examples of all Streamlit tools with descriptions, working examples, and code snippets. See a live preview of each tool right in the app.")

# Tabs for organization
tabs = st.tabs(["Text Components", "Input Widgets", "Media", "Layouts", "Other Tools"])

# Helper function for displaying examples with visual previews
def show_example(description, code, render_function):
    # Visual Example
    st.markdown(f"### Visual Example")
    render_function()
    
    # Description and Code
    st.markdown(f"**Description:** {description}")
    st.markdown("**Code:**")
    code_snippet = textwrap.dedent(code).strip()
    st.code(code_snippet, language="python")
    st.button("Copy Code", key=code_snippet)  # Placeholder for copy button

# Text Components Tab
with tabs[0]:
    st.header("Text Components")
    
    show_example(
        "Display a large header for section titles.",
        """
        st.header("A Large Header")
        """,
        lambda: st.header("A Large Header")
    )
    
    show_example(
        "Use Markdown for rich text formatting like **bold**, *italicized*, or [links](https://streamlit.io).",
        """
        st.markdown("Markdown is **bold**, *italicized*, or has [links](https://streamlit.io).")
        """,
        lambda: st.markdown("Markdown is **bold**, *italicized*, or has [links](https://streamlit.io).")
    )
    
    show_example(
        "Render Python code blocks with syntax highlighting.",
        """
        st.code("print('Hello, Streamlit!')", language="python")
        """,
        lambda: st.code("print('Hello, Streamlit!')", language="python")
    )
    
    show_example(
        "Render mathematical equations using LaTeX syntax.",
        """
        st.latex(r"a^2 + b^2 = c^2")
        """,
        lambda: st.latex(r"a^2 + b^2 = c^2")
    )

# Input Widgets Tab
with tabs[1]:
    st.header("Input Widgets")
    
    show_example(
        "Create a text input field for user data.",
        """
        name = st.text_input("Enter your name:")
        """,
        lambda: st.text_input("Enter your name:")
    )
    
    show_example(
        "Add a checkbox for toggling options.",
        """
        agree = st.checkbox("I agree to the terms and conditions")
        """,
        lambda: st.checkbox("I agree to the terms and conditions")
    )
    
    show_example(
        "Select a single option from a group using radio buttons.",
        """
        choice = st.radio("Pick an option:", ["Option 1", "Option 2", "Option 3"])
        """,
        lambda: st.radio("Pick an option:", ["Option 1", "Option 2", "Option 3"])
    )
    
    show_example(
        "Use a slider to pick a numeric value.",
        """
        value = st.slider("Choose a value:", 0, 100, 50)
        """,
        lambda: st.slider("Choose a value:", 0, 100, 50)
    )

# Media Tab
with tabs[2]:
    st.header("Media")
    
    show_example(
        "Display an image with an optional caption.",
        """
        st.image("https://via.placeholder.com/300", caption="Sample Image")
        """,
        lambda: st.image("https://via.placeholder.com/300", caption="Sample Image")
    )
    
    show_example(
        "Play an audio file directly in the app.",
        """
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        """,
        lambda: st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    )
    
    show_example(
        "Embed a video that users can play.",
        """
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        """,
        lambda: st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    )

# Layouts Tab
with tabs[3]:
    st.header("Layouts")
    
    show_example(
        "Create side-by-side layouts using columns.",
        """
        col1, col2 = st.columns(2)
        with col1:
            st.write("This is Column 1")
        with col2:
            st.write("This is Column 2")
        """,
        lambda: (
            st.columns(2)[0].write("This is Column 1"),
            st.columns(2)[1].write("This is Column 2"),
        )
    )
    
    show_example(
        "Add collapsible sections with expanders.",
        """
        with st.expander("Expand for more info"):
            st.write("This is inside an expander.")
        """,
        lambda: st.expander("Expand for more info").write("This is inside an expander.")
    )


# Other Tools Tab
with tabs[4]:
    st.header("Other Useful Tools")
    
    show_example(
        "Display a progress bar for tasks.",
        """
        st.progress(70)
        """,
        lambda: st.progress(70)
    )

    
    show_example(
        "Show a spinner while waiting for a task to complete.",
        """
        with st.spinner("Loading..."):
            st.success("Task completed!")
        """,
        # Correct usage: No lambda needed, directly execute with block
        lambda: (
            st.spinner("Loading..."),
            st.success("Task completed!")
        )
    )
    
    show_example(
        "Render error, warning, or info messages.",
        """
        st.error("This is an error message.")
        st.warning("This is a warning message.")
        st.info("This is an informational message.")
        """,
        lambda: (
            st.error("This is an error message."),
            st.warning("This is a warning message."),
            st.info("This is an informational message.")
        )
    )