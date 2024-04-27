import time
from typing import Tuple, Dict, Literal

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
AgGrid(df)
with st.sidebar:
    cols = st.columns(2)
    export_btn = cols[0]
    if cols[1].button(
            "清空对话",
            use_container_width=True,
    ):
        st.rerun()
export_btn.download_button(

    "导出记录",
    "Hi,wonderful apple",
    file_name=f"对话记录.md",
    mime="text/markdown",
    use_container_width=True,
)

def config_aggrid(
        df: pd.DataFrame,
        columns: Dict[Tuple[str, str], Dict] = {},
        selection_mode: Literal["single", "multiple", "disabled"] = "single",
        use_checkbox: bool = False,
) -> GridOptionsBuilder:
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_column("No", width=40)
    for (col, header), kw in columns.items():
        gb.configure_column(col, header, wrapHeaderText=True, **kw)
    gb.configure_selection(
        selection_mode=selection_mode,
        use_checkbox=use_checkbox,
        pre_selected_rows=st.session_state.get("selected_rows", [0]),
    )
    gb.configure_pagination(
        enabled=True,
        paginationAutoPageSize=False,
        paginationPageSize=10
    )
    return gb

data = {'姓名': ['张三', '李四', '王五'],
        '年龄': [18, 25, 30],
        '性别': ['男', '女', '男']}
doc = pd.DataFrame(data)
gb = config_aggrid(
    doc,
    {
        ("name","姓名"):{},
        ("age","年龄"): {},
        ("gender", "性别"):{},
    },
    "multiple",
)

df = pd.DataFrame(data)
grid_return = AgGrid(df, gb.build())
grid_return.get()
# new_df = grid_return["data"]
# st.write(new_df)

