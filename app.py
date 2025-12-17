"""
F1 Race Analytics Dashboard
Final Project - Pengantar Struktur Data dan Algoritma
"""

import streamlit as st
import pandas as pd
from data.data_loader import load_drivers
from algorithms.sorting import sort_drivers
from algorithms.searching import search_driver
from algorithms.hash_table import create_driver_hash_table
from algorithms.tree import create_driver_bst
from algorithms.recursive import factorial, fibonacci, sum_points, get_recursion_tree_visual
from utils.visualizations import (
    create_bar_chart,
    create_comparison_chart,
    create_hash_table_visual,
    create_tree_visualization,
)

# Page config
st.set_page_config(
    page_title="F1 Race Analytics",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for F1 theme
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1F2937;
        padding: 8px;
        border-radius: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #374151;
        border-radius: 8px;
        color: #D1D5DB;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #DC2626;
        color: white;
    }
    h1 {
        background: linear-gradient(90deg, #EF4444 0%, #F97316 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("# 🏎️ F1 Race Analytics Dashboard")
st.markdown("**Penerapan Struktur Data & Algoritma pada Data Formula 1**")
st.markdown("*Final Project - Pengantar Struktur Data dan Algoritma*")
st.markdown("---")

# Load data
drivers = load_drivers()

# Initialize session state
if "sorted_drivers" not in st.session_state:
    st.session_state.sorted_drivers = drivers
if "sort_time" not in st.session_state:
    st.session_state.sort_time = 0

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["📈 Sort Algorithms", "🔍 Search & Hash", "🌳 Tree Structure", "🔄 Recursive"]
)

# TAB 1: SORTING ALGORITHMS
with tab1:
    st.header("📈 Sorting Algorithms Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        sort_algo = st.selectbox(
            "Sort Algorithm",
            ["quick", "merge", "bubble"],
            format_func=lambda x: {
                "quick": "Quick Sort",
                "merge": "Merge Sort",
                "bubble": "Bubble Sort",
            }[x],
        )

    with col2:
        sort_metric = st.selectbox(
            "Sort By",
            ["points", "wins", "avgLapTime"],
            format_func=lambda x: {
                "points": "Points",
                "wins": "Wins",
                "avgLapTime": "Avg Lap Time",
            }[x],
        )

    with col3:
        st.metric(
            "Execution Time",
            f"{st.session_state.sort_time:.4f} ms",
            delta=None,
        )

    # Sort button
    if st.button("🚀 Sort Drivers", use_container_width=True, type="primary"):
        sorted_data, exec_time = sort_drivers(drivers, sort_algo, sort_metric)
        st.session_state.sorted_drivers = sorted_data
        st.session_state.sort_time = exec_time
        st.rerun()

    # Visualization
    st.plotly_chart(
        create_bar_chart(
            st.session_state.sorted_drivers[:6],
            "name",
            sort_metric,
            f"Top 6 Drivers by {sort_metric.replace('_', ' ').title()}",
        ),
        use_container_width=True,
    )

    # Data table
    st.subheader("Driver Rankings")
    df = pd.DataFrame(st.session_state.sorted_drivers)
    df.index = df.index + 1
    df.index.name = "Rank"
    st.dataframe(
        df[["name", "team", "points", "wins", "avgLapTime"]],
        use_container_width=True,
    )

# TAB 2: SEARCH & HASH
with tab2:
    st.header("🔍 Search Algorithms & Hash Table")

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        search_method = st.selectbox(
            "Search Method",
            ["binary", "linear"],
            format_func=lambda x: {
                "binary": "Binary Search",
                "linear": "Linear Search",
            }[x],
        )

    with col2:
        search_term = st.text_input("Driver Name", placeholder="e.g., Verstappen")

    with col3:
        st.write("")
        st.write("")
        search_button = st.button("🔎 Search", use_container_width=True, type="primary")

    # Search result
    if search_button and search_term:
        result = search_driver(drivers, search_term, search_method)
        if result:
            st.success("✅ Driver Found!")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Driver", result["name"])
            with col2:
                st.metric("Team", result["team"])
            with col3:
                st.metric("Points", result["points"])
            with col4:
                st.metric("Wins", result["wins"])
        else:
            st.error("❌ Driver not found")

    # Hash Table
    st.subheader("Hash Table Visualization")
    st.caption("Hash Function: `name.length % 10`")

    hash_table = create_driver_hash_table(drivers)
    buckets = create_hash_table_visual(hash_table)

    cols = st.columns(5)
    for idx, bucket_info in enumerate(buckets):
        with cols[idx % 5]:
            st.markdown(
                f"""
                <div style='background-color: #1F2937; padding: 10px; 
                border-radius: 8px; margin-bottom: 10px; border: 1px solid #374151;'>
                    <div style='color: #EF4444; font-weight: bold; 
                    font-size: 12px;'>
                        {bucket_info['bucket']}
                    </div>
                    <div style='color: #D1D5DB; font-size: 11px; 
                    margin-top: 5px;'>
                        {bucket_info['items']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# TAB 3: TREE STRUCTURE
with tab3:
    st.header("🌳 Binary Search Tree - Driver Rankings")

    st.info("BST organized by Points (descending). Each node represents a driver.")

    # Create BST
    bst = create_driver_bst(drivers)

    # Tree visualization
    st.subheader("Tree Structure")
    sorted_for_tree = sorted(drivers, key=lambda x: x["points"], reverse=True)
    tree_text = create_tree_visualization(sorted_for_tree)
    st.code(tree_text, language="text")

    # Traversals
    st.subheader("Tree Traversals")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Inorder Traversal**")
        st.caption("Left → Root → Right")
        inorder = bst.inorder_traversal()
        for idx, driver in enumerate(inorder, 1):
            st.write(f"{idx}. {driver['name']}")

    with col2:
        st.markdown("**Preorder Traversal**")
        st.caption("Root → Left → Right")
        preorder = bst.preorder_traversal()
        for idx, driver in enumerate(preorder, 1):
            st.write(f"{idx}. {driver['name']}")

    with col3:
        st.markdown("**Postorder Traversal**")
        st.caption("Left → Right → Root")
        postorder = bst.postorder_traversal()
        for idx, driver in enumerate(postorder, 1):
            st.write(f"{idx}. {driver['name']}")

# TAB 4: RECURSIVE
with tab4:
    st.header("🔄 Recursive Algorithms")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Factorial & Fibonacci")
        n = st.number_input("Input N:", min_value=0, max_value=15, value=5, step=1)

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Calculate Factorial", use_container_width=True):
                result = factorial(n)
                st.success(f"Factorial({n}) = **{result:,}**")

        with col_b:
            if st.button("Calculate Fibonacci", use_container_width=True):
                result = fibonacci(n)
                st.success(f"Fibonacci({n}) = **{result}**")

    with col2:
        st.subheader("Recursive Sum - Total Points")
        st.caption("Calculate total championship points using recursive algorithm")

        if st.button("Calculate Recursive Sum", use_container_width=True, type="primary"):
            total = sum_points(drivers)
            st.success(f"**Total Points (Recursive Sum) = {total:,}**")

    # Recursion Tree
    st.subheader("Recursion Tree Visualization")
    st.code(get_recursion_tree_visual(), language="text")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #9CA3AF; padding: 20px;'>
        <p>🏎️ F1 Race Analytics Dashboard | Powered by Streamlit & Python</p>
        <p style='font-size: 12px;'>
            Algorithms: Bubble Sort, Quick Sort, Merge Sort, Binary Search, 
            Linear Search, Hash Table, BST, Recursion
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)