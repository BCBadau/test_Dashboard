import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Halaman Utama",page_icon="logo.png" ,layout="wide")

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your local image
image_path = "https://github.com/BCBadau/test_Dashboard/blob/main/logo.png"
base64_image = get_base64_image(image_path)

# Center Logo and Title with Styling
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{base64_image}" alt="Logo" style="width: 100px; margin-bottom: 20px;">
        <h1 style="color: rgb(46, 154, 255); font-size: 40px;">KPPBC TMP C NANGA BADAU</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
# Hide sidebar and toolbar
#[data-testid="stToolbar"] { display: none; }
hide_ui_style = """
    <style>
        [data-testid="stSidebar"] { display: none; }
        [data-testid="stToolbar"] { display: none; }
    </style>
"""
st.markdown(hide_ui_style, unsafe_allow_html=True)

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Halaman Utama"

# Function to navigate between pages
def navigate(page):
    st.session_state.current_page = page

# Custom menu bar with submenus
menu_html = """
    <style>
        /* Main menu bar styling */
        .menu-bar {
            background-color: rgb(4, 28, 77);
            display: flex;
            justify-content: center;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .menu-bar li {
            list-style: none;
            position: relative;
            padding: 10px 20px;
            display: inline-block;
        }

        .menu-bar a {
            text-decoration: none;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        .menu-bar a:hover {
            background-color: #007acc;
        }

        /* Submenu container */
        .submenu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            background-color: #333;
            list-style-type: none;
            padding: 10px;
            min-width: 160px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .submenu li {
            padding: 5px 0;
        }

        .submenu a {
            display: block;
            color: white;
            text-decoration: none;
        }

        .submenu a:hover {
            background-color: #555;
        }

        /* Show submenu on hover */
        .menu-bar li:hover .submenu {
            display: block;
        }
    </style>

    <ul class="menu-bar">
        <li><a href="#" onclick="navigatePage('Halaman Utama')">Halaman Utama</a></li>
        <li><a href="#" onclick="navigatePage('Penerimaan')">Penerimaan</a></li>
        <li>
            <a href="/VHD">Dashboard VHD</a>
            <ul class="submenu">
                <li><a href="/FORM_BCB/input_" onclick="navigatePage('Input VHD')">Input VHD</a></li>
                <li><a href="#" onclick="navigatePage('Input Multitrip')">Input Multitrip</a></li>
                <li><a href="#" onclick="navigatePage('Tutup/Perpanjang')">Tutup/Perpanjang</a></li>
            </ul>
        </li>
        <li><a href="#" onclick="navigatePage('Info')">Info</a></li>
    </ul>

    <script>
        function navigatePage(page) {
            document.querySelector('input[name="navigation_state"]').value = page;
            document.querySelector('form').submit();
        }
    </script>
"""

# Embed custom menu bar
st.markdown(menu_html, unsafe_allow_html=True)

# Hidden input form to handle page navigation
st.write(
    f"""
    <form>
        <input type="hidden" name="navigation_state" value="{st.session_state.current_page}">
    </form>
    """,
    unsafe_allow_html=True,
)

# Display content based on the selected page
if st.session_state.current_page == "Halaman Utama":
    st.title("Halaman Utama")
    st.write("Welcome to the main dashboard!")
elif st.session_state.current_page == "Input VHD":
    st.title("Input VHD")
    st.write("This is the input form page.")
elif st.session_state.current_page == "Input Multitrip":
    st.title("Input Multitrip")
    st.write("This is the Input Multitrip page.")
elif st.session_state.current_page == "Tutup/Perpanjang":
    st.title("Tutup/Perpanjang")
    st.write("Manage closing and extensions here.")
elif st.session_state.current_page == "Dashboard VHD":
    st.title("Dashboard VHD")
    st.write("Welcome to the VHD dashboard.")
elif st.session_state.current_page == "Info":
    st.title("Info Page")
    st.write("Here is some important information.")
