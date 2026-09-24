import streamlit as st

st.title("🚀 Getting Started")

st.markdown("Complete these steps before beginning the lab exercises.")

st.markdown("---")

st.header("Step 1: Log in to Snowflake")

st.info("""
Open your Snowflake URL and log in using SSO.
""")

st.markdown("---")

st.header("Step 2: Find your assigned number")

st.markdown("""
Each participant has a pre-assigned number and workspace. Find your name below and note your **number** — 
you'll use it throughout the entire lab.
""")

st.dataframe(
    {
        "#": [f"{i:02d}" for i in range(1, 49)],
        "Name": [
            "Aberin, MariaPaz",
            "Ambacher, Matt",
            "Bachani, Mamta",
            "Cadiz, Francis",
            "Canlas, Rachelle",
            "Carroll, Michael",
            "Chang, David",
            "Che, Claire",
            "Chen, Anthony",
            "Chhabra, Shriya",
            "Chow, Alice Kit Ling",
            "Chow, Ron",
            "Dave, Ketul",
            "Delos Santos, Roanna",
            "Fleck, Vidya",
            "Gonzales, Sally",
            "Haid, Daniel",
            "Han, Herbert",
            "Jha, Rakhi",
            "Karpal, Raghav",
            "Khamsi, Bahram",
            "Kim, Taeyoung",
            "Komarov, Dmitriy",
            "Lam, Astrid",
            "Lau, Alice",
            "Luo, Jack",
            "Medina, Carolina",
            "Narayanan, Syam Prakash",
            "Narodenko, Oksana",
            "Natividad, Marilou",
            "Onifade, Oluwanifemi",
            "Pualengco, Roberto",
            "Rathbone, Luke",
            "Saeed, Hiba",
            "Shahmardan, Amin",
            "Shi, Ming",
            "Shi, Yixin",
            "Sindgikar, Ameya",
            "Sun, Tianrong",
            "Tian, Janice",
            "Tran, Grace",
            "Wimmers, Robyn",
            "Wu, Kevin",
            "Wu, Michael",
            "Yacas, Clifford",
            "Yazdi, Sara",
            "Zhang, Rui",
            "Zhu, Vanessa",
        ],
        "Role": [f"TU30_ZERO_TO_SNOWFLAKE_LAB_USER_{i:02d}" for i in range(1, 49)],
        "Schema": [f"RETAIL_BANKING_{i:02d}" for i in range(1, 49)],
    },
    use_container_width=True,
    hide_index=True,
)

st.warning("Use **your assigned number** in every `USE ROLE` and `USE SCHEMA` command throughout the lab.")

st.markdown("---")

st.header("Step 3: Keep this guide open")

st.markdown("""
Keep this browser tab open throughout the lab:

👉 **https://zero-to-sf-hol-rbc-sept28.streamlit.app**

Use the sidebar to navigate between sections. Each section has:
- A **concept intro** explaining what you'll learn
- **Numbered exercises** with SQL to copy and run
- A **CoCo Sneak Peek** showing how Cortex Code could do it for you
""")

st.markdown("---")

st.success("""
## ✅ You're ready!

Head to **Section 1: Snowflake UI Tour** to begin the lab.
""")
