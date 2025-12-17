"""
Plotly Visualizations for F1 Dashboard
"""

import plotly.graph_objects as go
import plotly.express as px


def create_bar_chart(data, x_col, y_col, title):
    """Create bar chart for driver statistics"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[d[x_col] for d in data],
            y=[d[y_col] for d in data],
            marker=dict(
                color="#EF4444",
                line=dict(color="#991B1B", width=1),
            ),
            hovertemplate="<b>%{x}</b><br>" + y_col + ": %{y}<extra></extra>",
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title=x_col,
        yaxis_title=y_col,
        template="plotly_dark",
        plot_bgcolor="#111827",
        paper_bgcolor="#1F2937",
        font=dict(color="#F3F4F6"),
        height=400,
        margin=dict(l=50, r=50, t=80, b=100),
    )

    fig.update_xaxes(tickangle=-45)

    return fig


def create_comparison_chart(data, metric):
    """Create comparison chart for multiple drivers"""
    fig = go.Figure()

    colors = ["#EF4444", "#F97316", "#FBBF24", "#34D399", "#60A5FA", "#A78BFA"]

    for idx, driver in enumerate(data[:6]):
        fig.add_trace(
            go.Bar(
                name=driver["name"].split()[-1],
                x=[metric],
                y=[driver[metric]],
                marker_color=colors[idx % len(colors)],
            )
        )

    fig.update_layout(
        title=f"Top 6 Drivers - {metric.replace('_', ' ').title()}",
        template="plotly_dark",
        plot_bgcolor="#111827",
        paper_bgcolor="#1F2937",
        font=dict(color="#F3F4F6"),
        height=400,
        barmode="group",
    )

    return fig


def create_hash_table_visual(hash_table):
    """Create visualization for hash table"""
    buckets = []
    for idx, bucket in enumerate(hash_table.get_table()):
        bucket_info = {
            "bucket": f"Bucket {idx}",
            "count": len(bucket),
            "items": ", ".join([item["key"].split()[-1] for item in bucket])
            if bucket
            else "Empty",
        }
        buckets.append(bucket_info)

    return buckets


def create_tree_visualization(sorted_drivers):
    """
    Create simple tree structure visualization
    Returns formatted text for tree display
    """
    if len(sorted_drivers) < 7:
        return "Not enough drivers for tree visualization"

    tree_text = f"""
    Root: {sorted_drivers[0]['name']} ({sorted_drivers[0]['points']} pts)
    ├── Left: {sorted_drivers[1]['name']} ({sorted_drivers[1]['points']} pts)
    │   ├── {sorted_drivers[3]['name']} ({sorted_drivers[3]['points']} pts)
    │   └── {sorted_drivers[4]['name']} ({sorted_drivers[4]['points']} pts)
    └── Right: {sorted_drivers[2]['name']} ({sorted_drivers[2]['points']} pts)
        ├── {sorted_drivers[5]['name']} ({sorted_drivers[5]['points']} pts)
        └── {sorted_drivers[6]['name']} ({sorted_drivers[6]['points']} pts)
    """
    return tree_text